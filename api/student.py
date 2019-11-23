# Student API Functions

from . import database

def update_level(level, student_id):
    """ Update the level of the student on the system"""
    query = 'UPDATE student SET level = %s WHERE student_id = %s;'
    args = (level, student_id)
    database.connection.save_data(query, args)

def update_grade(grade, student_id):
    """ Update the grade of the student on the system"""
    query = 'UPDATE student SET grade = %s WHERE student_id = %s;'
    args = (grade, student_id)
    database.connection.save_data(query, args)

def get_all_students():
    """ List the data of all students"""
    query = "SELECT * FROM student JOIN person ON student.student_id=person.account_id;"
    return database.connection.get_data(query, None)

def get_student_information(student_id):
    """ Get student information for particular student """
    query = 'SELECT * FROM student JOIN person ON student.student_id=person.account_id WHERE student.student_id=%s;'
    args = (student_id)
    return database.connection.get_data(query, args)

def grant_student_access(account_id, grade, level):
    """Grants an account to be a student"""
    query = 'INSERT INTO student VALUES( %s, %s, %s );'
    args = (account_id, grade, level)
    database.connection.save_data(query, args)

def revoke_student_access(account_id):
    """Revokes the student permissions for an account"""
    query = 'DELETE FROM student WHERE student_id = %s;'
    args = (account_id)
    database.connection.save_data(query, args)

def create_student(username, password, email, preferred_language,skype_id,name, phone_number, country,availability, grade, level):
    person.create_person(username,password,email,preferred_language,skype_id,name,phone_number,country)
    student_id = person.get_last()
    query = 'INSERT INTO student VALUES( %s,%s, %s );'
    args = (student_id, grade, level)
    database.connection.save_data(query, args)
