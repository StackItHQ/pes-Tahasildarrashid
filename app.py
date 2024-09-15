import gspread
from oauth2client.service_account import ServiceAccountCredentials
import mysql.connector
import time

# Google Sheets API setup
def get_google_sheet_data(sheet_url, credentials_json):
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name(credentials_json, scope)
    client = gspread.authorize(creds)
    sheet = client.open_by_url(sheet_url).sheet1
    data = sheet.get_all_records()
    return data

def update_google_sheet(sheet_url, credentials_json, db_data):
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name(credentials_json, scope)
    client = gspread.authorize(creds)
    sheet = client.open_by_url(sheet_url).sheet1
    
    # Get existing data from the sheet to check for duplicates
    existing_data = sheet.get_all_records()
    existing_ids = {row['id'] for row in existing_data}
    
    # Append new data if not already present (ignore if already present)
    for row in db_data:
        if row.get('id') not in existing_ids:
            sheet.append_row([row.get('id'), row.get('name'), row.get('email'), row.get('age')])
    
    print("Synchronized Google Sheets with MySQL data")

# MySQL database connection setup
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password",
        database="superjoin"
    )

def create_record(id, name, email, age):
    db_conn = get_db_connection()
    cursor = db_conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO students (id, name, email, age) VALUES (%s, %s, %s, %s)
        """, (id, name, email, age))
        db_conn.commit()
        print(f"Inserted record for id {id}")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        db_conn.close()

def read_record(id):
    db_conn = get_db_connection()
    cursor = db_conn.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM students WHERE id = %s", (id,))
        result = cursor.fetchone()
        return result
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        db_conn.close()

def update_record(id, name, email, age):
    db_conn = get_db_connection()
    cursor = db_conn.cursor()
    try:
        cursor.execute("""
            UPDATE students SET name=%s, email=%s, age=%s WHERE id=%s
        """, (name, email, age, id))
        db_conn.commit()
        print(f"Updated record for id {id}")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        db_conn.close()

def delete_record(id):
    db_conn = get_db_connection()
    cursor = db_conn.cursor()
    try:
        # Disable SQL_SAFE_UPDATES to allow deletions
        cursor.execute("SET SQL_SAFE_UPDATES = 0")
        
        # Perform the deletion based on the missing record's id
        cursor.execute("DELETE FROM students WHERE id = %s", (id,))
        
        # Print a log message that the record has been deleted
        print(f"Record with id {id} has been deleted from MySQL")

        # Optionally, re-enable SQL_SAFE_UPDATES
        cursor.execute("SET SQL_SAFE_UPDATES = 1")
        
        db_conn.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        db_conn.close()

def sync_mysql_to_google_sheet(sheet_url, credentials_json):
    db_conn = get_db_connection()
    cursor = db_conn.cursor(dictionary=True)
    
    try:
        cursor.execute("SELECT * FROM students")
        db_data = cursor.fetchall()
        update_google_sheet(sheet_url, credentials_json, db_data)
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        db_conn.close()

def sync_google_sheet_to_mysql(sheet_url, credentials_json):
    sheet_data = get_google_sheet_data(sheet_url, credentials_json)
    
    # Print sheet_data to debug
    print("Google Sheets Data:")
    for row in sheet_data:
        print(row)
    
    db_conn = get_db_connection()
    cursor = db_conn.cursor(dictionary=True)
    
    try:
        # Fetch existing data from MySQL
        cursor.execute("SELECT * FROM students")
        existing_records = cursor.fetchall()
        existing_ids = {record['id'] for record in existing_records}
        
        # Convert sheet data to a dictionary for easy lookup
        sheet_data_dict = {row['id']: row for row in sheet_data}
        
        # Identify records to insert or update
        for id, row in sheet_data_dict.items():
            if id in existing_ids:
                # Update existing records in MySQL
                existing_record = next(record for record in existing_records if record['id'] == id)
                if (existing_record['name'] != row['name'] or
                    existing_record['email'] != row['email'] or
                    existing_record['age'] != row['age']):
                    update_record(id, row['name'], row['email'], row['age'])
            else:
                # Insert new records into MySQL
                create_record(row['id'], row['name'], row['email'], row['age'])
        
        # Identify records that exist in MySQL but not in Google Sheets (those that were deleted)
        sheet_ids = set(sheet_data_dict.keys())
        for existing_record in existing_records:
            if existing_record['id'] not in sheet_ids:
                print(f"Deleting record with id {existing_record['id']} from MySQL as it was deleted in Google Sheets")
                delete_record(existing_record['id'])
        
        # Commit changes to the database
        db_conn.commit()
        print("Synchronized MySQL with Google Sheets data")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        db_conn.close()


def sync_data(sheet_url, credentials_json, interval=30):
    while True:
        sync_mysql_to_google_sheet(sheet_url, credentials_json)
        sync_google_sheet_to_mysql(sheet_url, credentials_json)
        print(f"Synchronization completed. Sleeping for {interval} seconds...")
        time.sleep(interval)

# Main function
if __name__ == "__main__":
    sheet_url = "https://docs.google.com/spreadsheets/d/1qIumHprfuEi8sf5W5Z8A4RtcLT8jJUf-WhEw6GMDNI4/edit?gid=0#gid=0"
    credentials_json = "C:/Users/tahas/OneDrive/Desktop/super_join/backend/credentials.json"
    
    # Start the synchronization process with a polling interval of 30 seconds
    sync_data(sheet_url, credentials_json, interval=30)
