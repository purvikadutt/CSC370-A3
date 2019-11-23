# Person API Functions
from . import database

def create_person(username, password, email, preferred_language,skype_id,name, country,phone_number):
    """Creates a new person"""
    query = 'INSERT INTO person VALUES( DEFAULT,%s,%s,%s,%s,%s,%s,%s,%s );'
    args = (username,password,email,preferred_language,skype_id,name,country,phone_number)
    database.connection.save_data(query, args)

def get_last_person():
    """Gets the last person (sorted by account_id)"""
    query = 'SELECT account_id FROM person ORDER BY account_id DESC LIMIT 1;'
    result = database.connection.get_data(query, None)
    return result[0][0]

def get_person(account_id):
    """Get the information of a person"""
    query = "SELECT * FROM person WHERE account_id = %s;"
    args = (account_id,)
    return database.connection.get_data(query, args)[0] # First row

def delete_person(account_id): 
    """Delete a person"""
    query = "DELETE FROM person WHERE account_id = %s;"
    args = (account_id,)
    database.connection.save_data(query, args)

def list_people():
    """List all people in the database"""
    query = "SELECT * FROM person;"
    return database.connection.get_data(query, None)

def update_login(account_id, new_username, new_password):
    """Update the login information of a person"""
    query = "UPDATE person SET username = %s, password = %s WHERE account_id = %s;"
    args = (new_username, new_password, account_id)
    database.connection.save_data(query, args)

def update_name(account_id, new_name):
    """Update the name of a person"""
    query = "UPDATE person SET name = %s WHERE account_id = %s;"
    args = (new_name, account_id)
    database.connection.save_data(query, args)

def update_contact_info(account_id, new_phone_number, new_email_address, new_skype_id):
    """Update the contact information of a person"""
    query = "UPDATE person SET phone_number = %s, email_address = %s, skype_id = %s WHERE account_id = %s;"
    args = (new_phone_number, new_email_address, new_skype_id, account_id)
    database.connection.save_data(query, args)

def update_country(account_id, new_country):
    """Update the country of a person"""
    query = "UPDATE person SET country = %s WHERE account_id = %s;"
    args = (new_country, account_id)
    database.connection.save_data(query, args)

def update_preferred_language(account_id, preferred_language_id):
    """Update the preferred language of a person"""
    query = "UPDATE person SET prefered_language = %s WHERE account_id = %s;"
    args = (preferred_language_id, account_id)
    database.connection.save_data(query, args)

def add_known_language(account_id, language_id):
    """Add a known language from a person"""
    query = "INSERT INTO known_languages VALUES ( %s, %s );"
    args = (account_id, language_id)
    database.connection.save_data(query, args)

def remove_known_language(account_id, language_id):
    """Remove a known language from a person"""
    query = "DELETE FROM known_languages WHERE account_id = %s and language_id = %s;"
    args = (account_id,language_id)
    database.connection.save_data(query, args)

def get_known_languages(account_id):
    """Returns all known languages of a person"""
    query = "SELECT language_id FROM known_languages WHERE account_id = %s;"
    args = (account_id,)
    return database.connection.get_data(query, args)
