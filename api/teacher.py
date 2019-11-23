# Test API Functions
# A simple example of an API implementation

from . import database
from . import person

def create_teacher(username, password, email, preferred_language,skype_id,name, phone_number, country,availability):
    """Create a new teacher account"""
    person.create_person(username,password,email,preferred_language,skype_id,name,phone_number,country)
    teacher_account_id = person.get_last()
    query = 'INSERT INTO teacher VALUES( %s,%s );'
    args = (teacher_account_id, availability)
    database.connection.save_data(query, args)

def revoke_teacher(teacher_account_id):
    """Revoke teacher permissions from an account"""
    query = 'DELETE FROM teacher WHERE teacher_account_id=%s;'
    args = (teacher_account_id,)
    database.connection.save_data(query, args)

def grant_teacher(account_id, availability):
    """Grant teacher permissions to a specific account"""
    query = 'INSERT INTO teacher VALUES( %s, %s);'
    args = (account_id, availability)
    database.connection.save_data(query, args)

def add_category(teach_id,cat_id):
    """Add a category to a specific teacher"""
    query = 'INSERT INTO teacher_categories VALUES( %s,%s );'
    args = (teach_id,cat_id)
    database.connection.save_data(query, args)

def remove_category(teach_id, cat_id):
    """Remove a category from a specific teacher"""
    query = "DELETE FROM teacher_categories WHERE teacher_account_id = %s and category_id  = %s;"
    args = (teach_id, cat_id)
    database.connection.save_data(query, args)

def get_categories(teach_id):
    """Returns all known languages of a person"""
    query = "SELECT category_id FROM teacher_categories WHERE teacher_account_id = %s;"
    args = (teach_id,)
    return database.connection.get_data(query, args)

def get_teachers():
    """Get all teachers"""
    query = "SELECT * FROM teacher JOIN person ON teacher.teacher_account_id=person.account_id;"
    return database.connection.get_data(query, None)

def update_availability(teach_id,avail_string):
    """Update the availability string of a teacher"""
    query = 'UPDATE teacher SET availability=%s WHERE teacher_account_id=%s;'
    args = (avail_string,teach_id)
    database.connection.save_data(query, args)

def add_level(teach_id,level):
    """Add a new level to a teacher account"""
    query = 'INSERT INTO teacher_levels(teacher_account_id,level) VALUES( %s,%s );'
    args = (teach_id,level)
    database.connection.save_data(query, args) 

def get_levels(teach_id):
    """Returns all levels of a teacher"""
    query = "SELECT level FROM teacher_levels WHERE teacher_account_id = %s;"
    args = (teach_id,)
    return database.connection.get_data(query, args)

def remove_level(teach_id,level):
    """Remove a level from a teacher"""
    query = "DELETE FROM teacher_levels WHERE teacher_account_id = %s and level = %s;"
    args = (teach_id, level)
    database.connection.save_data(query, args)

def get_teacher(teacher_account_id):
    """Get a specific teacher"""
    query = 'SELECT * FROM teacher JOIN person ON teacher.teacher_account_id=person.account_id WHERE teacher.teacher_account_id=%s;'
    args = (teacher_account_id,)
    return database.connection.get_data(query, args)

if __name__ == '__main__':
    main()