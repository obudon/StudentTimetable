DROP TABLE IF EXISTS users;

CREATE TABLE users
(
    user_id TEXT PRIMARY KEY,
    password TEXT NOT NULL
);

DROP TABLE IF EXISTS timetable;

CREATE TABLE timetable 
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    day TEXT NOT NULL,
    time TEXT NOT NULL,
    activity_type TEXT NOT NULL,
    course TEXT NOT NULL,
    location TEXT
);

INSERT INTO timetable ( day, time, activity_type, course, location)
VALUES     
    ("Monday", "9:00-10:00", "Lecture", "CS1117", "G_05"),
    ("Monday", "13:00-14:00", "Lecture", "CS1110", "C_WGB_107"),
    ("Monday", "14:00-15:30", "Activity", "Soccer", "Mardyke_Arena"),
    ("Tuesday", "11:00-12:00", "Lecture", "MA1002", "C_WGB_107"),
    ("Tuesday", "12:00-13:00", "Lecture", "CS1116", "C_WGB_107"),
    ("Tuesday", "14:00-14:00", "Lecture", "CS1117", "C_WGB_110"),
    ("Tuesday", "14:00-15:30", "Activity", "Tennis", "Mardyke_Arena"),
    ("Wednesday", "11:00-12:00", "Lecture", "MA1002", "C_WGB_107"),
    ("Wednesday", "13:00-14:00", "Lecture", "CS1110", "C_WGB_107"),
    ("Wednesday", "15:00-16:00", "Lecture", "CS1117", "C_WGB_110"),
    ("Wednesday", "14:00-15:30", "Activity", "Tennis", "Mardyke_Arena"),
    ("Thursday", "11:00-12:00", "Lecture", "MA1002", "C_WGB_107"),
    ("Thursday", "13:00-15:00", "Lecture", "CS1116", "C_WGB_110"),
    ("Thursday", "10:00-11:00", "Lab", "MA1002", "Home"),
    ("Thursday", "9:00-10:00", "Activity", "Tennis", "Mardyke_Arena"),
    ("Friday", "11:00-12:00", "Lecture", "CS1113", "Boole_2"),
    ("Friday", "13:00-14:00", "Lab", "CS1110", "C_WGB_110"),
    ("Friday", "14:00-15:00", "Lecture", "CS1113", "C_WGB_110"),
    ("Friday", "16:00-18:30", "Activity", "Soccer", "Mardyke_Arena");
    
DROP TABLE IF EXISTS createdtimetable; 

CREATE TABLE createdtimetable
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    day TEXT NOT NULL,
    time TEXT NOT NULL,
    activity_type TEXT NOT NULL,
    course TEXT NOT NULL,
    location TEXT
);


SELECT * FROM timetable;



