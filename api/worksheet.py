# Worksheet API Functions

from . import database

def update_worksheet_level(level, worksheet_id):
    """ Update the level of a worksheet on the system"""
    query = 'UPDATE worksheet SET level = %s WHERE worksheet_id = %s;'
    args = (level, worksheet_id)
    database.connection.save_data(query, args)

def update_name(name, worksheet_id):
    """ Update the worksheet name on the system"""
    query = 'UPDATE worksheet SET name = %s WHERE worksheet_id = %s;'
    args = (name, worksheet_id)
    database.connection.save_data(query, args)

def update_worksheet_category(worksheet_id, category_id):
    """ Update the (worksheet) categories """
    query = 'UPDATE worksheet SET category_id=%s WHERE worksheet_id = %s;'
    args = (category_id, worksheet_id)
    database.connection.save_data(query, args)

def add_language(worksheet_id, language_id):
    """Add a language to table worksheet_languages"""
    query = "INSERT INTO worksheet_languages VALUES ( %s, %s );"
    args = (worksheet_id, language_id)
    database.connection.save_data(query, args)

def remove_language(worksheet_id, language_id):
    """Remove a language from table worksheet_languages"""
    query = "DELETE FROM worksheet_languages WHERE worksheet_id = %s and language_id = %s;"
    args = (worksheet_id,language_id)
    database.connection.save_data(query, args)

def get_worksheet_languages(worksheet_id):
    """Returns all languages for a worksheet"""
    query = "SELECT language_id FROM worksheet_languages WHERE worksheet_id = %s;"
    args = (worksheet_id)
    return database.connection.get_data(query, args)

def get_all_worksheets():
    """ List of all worksheet information """
    query = "SELECT * from worksheet;"
    return database.connection.get_data(query, None)

def get_worksheet_information(worksheet_id):
    """ Get worksheet information for particular worksheet """
    query = 'SELECT worksheet_id, name, filename, level, category_id, modified_by_account_id, modified_timestamp FROM worksheet WHERE worksheet_id = %s;'
    args = (worksheet_id)
    return database.connection.get_data(query, args)

def create_worksheet(name, filename, level, category_id, modified_by_account_id):
    """ Create a new worksheet in the system """
    query = 'INSERT INTO worksheet VALUES(DEFAULT,%s,%s,%s,%s,%s,current_time);'
    args = (name, filename, level, category_id, modified_by_account_id)
    database.connection.save_data(query, args)

def delete_worksheet(worksheet_id):
    """ Delete a worksheet from the system """
    query = 'DELETE from worksheet WHERE worksheet_id = %s;'
    args = (worksheet_id)
    database.connection.save_data(query, args)
