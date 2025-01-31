-- SQL Exercises (With Answers)

-- 1. Retrieve all students who enrolled in 2023.
SELECT * FROM students
WHERE year(enrollmentdate) = 2023;

-- 2. Find students whose email contains 'gmail.com'.

SELECT * FROM students
WHERE Email LIKE '%gmail.com';


-- 3. Count how many students are enrolled in the database.

SELECT count(*) FROM students;


-- 4. Find students born between 2000 and 2005.

SELECT * FROM students
WHERE year(DateOfBirth) >= 2000 AND year(DateOfBirth) <= 2005;


-- 5. List students sorted by last name in descending order.

SELECT * FROM students
ORDER BY LastName DESC;


-- 6. Find the names of students and the courses they are enrolled in.
SELECT Students.FirstName, Students.StudentID, Students.LastName, Courses.CourseName
From Students
inner join Enrollments on Students.StudentID = Enrollments.StudentID
inner join Courses on Enrollments.courseid = Courses.courseid;


-- 7. List all students and their courses, ensuring students without courses are included (LEFT JOIN).

SELECT Students.FirstName, Students.StudentID, Students.LastName, Courses.CourseName, enrollments.courseid
From Students
left join Enrollments on Students.StudentID = Enrollments.StudentID
left join Courses on Enrollments.courseid = Courses.courseid;


-- 8. Find all courses with no students enrolled (LEFT JOIN).

SELECT  courses.coursename, courses.courseid
From courses
left join enrollments on courses.courseid = Enrollments.courseid
WHERE enrollments.courseid IS NULL;



-- 10. List courses and show the number of students enrolled in each course.

SELECT count(enrollments.StudentID), Courses.CourseName
From enrollments
Inner join courses on courses.CourseID = Enrollments.courseID
GROUP BY courses.coursename;

