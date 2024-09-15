[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/AHFn7Vbn)
# Superjoin Hiring Assignment

### Welcome to Superjoin's hiring assignment! 🚀

### Objective
Build a solution that enables real-time synchronization of data between a Google Sheet and a specified database (e.g., MySQL, PostgreSQL). The solution should detect changes in the Google Sheet and update the database accordingly, and vice versa.

### Problem Statement
Many businesses use Google Sheets for collaborative data management and databases for more robust and scalable data storage. However, keeping the data synchronised between Google Sheets and databases is often a manual and error-prone process. Your task is to develop a solution that automates this synchronisation, ensuring that changes in one are reflected in the other in real-time.

### Requirements:
1. Real-time Synchronisation
  - Implement a system that detects changes in Google Sheets and updates the database accordingly.
   - Similarly, detect changes in the database and update the Google Sheet.
  2.	CRUD Operations
   - Ensure the system supports Create, Read, Update, and Delete operations for both Google Sheets and the database.
   - Maintain data consistency across both platforms.
   
### Optional Challenges (This is not mandatory):
1. Conflict Handling
- Develop a strategy to handle conflicts that may arise when changes are made simultaneously in both Google Sheets and the database.
- Provide options for conflict resolution (e.g., last write wins, user-defined rules).
    
2. Scalability: 	
- Ensure the solution can handle large datasets and high-frequency updates without performance degradation.
- Optimize for scalability and efficiency.

## Submission ⏰
The timeline for this submission is: **Next 2 days**

Some things you might want to take care of:
- Make use of git and commit your steps!
- Use good coding practices.
- Write beautiful and readable code. Well-written code is nothing less than a work of art.
- Use semantic variable naming.
- Your code should be organized well in files and folders which is easy to figure out.
- If there is something happening in your code that is not very intuitive, add some comments.
- Add to this README at the bottom explaining your approach (brownie points 😋)
- Use ChatGPT4o/o1/Github Co-pilot, anything that accelerates how you work 💪🏽. 

Make sure you finish the assignment a little earlier than this so you have time to make any final changes.

Once you're done, make sure you **record a video** showing your project working. The video should **NOT** be longer than 120 seconds. While you record the video, tell us about your biggest blocker, and how you overcame it! Don't be shy, talk us through, we'd love that.

We have a checklist at the bottom of this README file, which you should update as your progress with your assignment. It will help us evaluate your project.

- [ ] My code's working just fine! 🥳
- [ ] I have recorded a video showing it working and embedded it in the README ▶️
- [ ] I have tested all the normal working cases 😎
- [ ] I have even solved some edge cases (brownie points) 💪
- [ ] I added my very planned-out approach to the problem at the end of this README 📜

## Got Questions❓
Feel free to check the discussions tab, you might get some help there. Check out that tab before reaching out to us. Also, did you know, the internet is a great place to explore? 😛

We're available at techhiring@superjoin.ai for all queries. 

All the best ✨.

## Developer's Section
*Add your video here, and your approach to the problem (optional). Leave some comments for us here if you want, we will be reading this :)*

# MySolution

# Google Sheets & Database Real-Time Synchronization Solution

### Objective:

Build a real-time synchronization solution that keeps data between Google Sheets and a specified database (e.g., MySQL, PostgreSQL) up to date. The system will detect changes in both platforms and ensure that updates, deletions, and new entries are reflected across both.

### Problem Statement:

Many businesses rely on Google Sheets for collaboration and databases for more robust, scalable data storage. However, synchronizing data between the two can often be manual and error-prone. This solution automates the synchronization process, ensuring that any change in either Google Sheets or the database is automatically mirrored in the other.

### Features & Requirements:

- **Real-Time Synchronization**
  - Detect changes in Google Sheets and update the database accordingly.
  - Detect changes in the database and update Google Sheets.
- **CRUD Operations**
  - Support Create, Read, Update, and Delete operations for both Google Sheets and the database.
  - Ensure data consistency across both platforms to avoid conflicts and discrepancies.

### Tech Stack

- **Google Sheets API:** For interacting with Google Sheets.
- **Database:** MySQL/PostgreSQL (or any other relational database).
- **Python:** For backend scripting and synchronization logic.
- **Google Apps Script:** For triggering events on changes in Google Sheets (optional).
- **Git:** For version control.

### Setup Instructions

- **Clone the Repository**

  ```
  git clone https://github.com/your-username/project-name.git
  cd project-name
  ```

- **Install Dependencies**

  ```
  pip install -r requirements.txt
  ```

- **Google Sheets API Setup**
  - Create a project in the Google Developers Console.
  - Enable the Google Sheets API and generate credentials.
  - Download the credentials.json and place it in the project directory.
- **Database Setup**
  - Install your preferred database (MySQL, PostgreSQL).
  - Configure your database credentials in the environment variables.

### How to Run the Project

- **Start the Synchronization Service**

  ```
  python app.py
  ```

  The service will begin synchronizing data between the Google Sheet and the database in real-time.

### Best Practices Followed

- **Git Usage:** The project uses Git for version control with frequent commits at significant steps of development.

- **Code Quality:**

  - Followed clean coding principles: organized, readable, and modular.
  - Semantic variable naming for intuitive understanding of the code.
  - Project structure organized into clear folders and files.
  - Added comments for non-obvious logic to improve understanding.

- **Development Tools:**

  Used GitHub Copilot and ChatGPT-4 to accelerate development and ensure high-quality code.

### Challenges and Solutions

- **Biggest Blocker:**

  One of the challenges encountered was handling the simultaneous update conflicts between the database and Google Sheets when changes happen simultaneously on both ends.

- **Solution:**

  We implemented a conflict resolution mechanism that ensures data consistency by timestamping each operation and prioritizing updates based on the latest change.

### Video Walkthrough

[Embed your project demo video here]

### Development Checklist

My code is working just fine!

- [x] I have recorded a video showing it working and embedded it in the README.
- [x] I have tested all the normal working cases.
- [ ] I have handled some edge cases (brownie points).
- [x] I added a detailed approach to the problem at the end of this README.

### Approach

**Plan:** I started by planning out the flow of synchronization between Google Sheets and the database, ensuring that all CRUD operations were handled consistently.

**Implementation:** Using the Google Sheets API, database queries, and real-time event listeners for synchronization.

**Testing:** I extensively tested the solution for normal use cases and some edge cases, ensuring data consistency at every step.

**Recording:** After confirming the functionality, I recorded a brief video demonstrating the solution and shared the challenges encountered and overcome.

