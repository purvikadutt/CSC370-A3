# Util API Functions

from . import database

def list_categories():
    """List all avaiable categories"""
    query = "SELECT * FROM categories;"
    return database.connection.get_data(query, None)

def add_category(category_name):
    """Add a new category. Returns the category id"""
    query = 'INSERT INTO categories(name) VALUES( %s );'
    args = (category_name,)
    database.connection.save_data(query, args)

    cat_id_query = 'SELECT category_id FROM categories WHERE name = %s;'
    result = database.connection.get_data(cat_id_query, args)
    return result[0][0] # first row, first column

def delete_category(category_id):
    """Deletes a category"""
    query = 'DELETE FROM categories WHERE category_id = %s;'
    args = (category_id, )
    database.connection.save_data(query, args)

def list_languages():
    """List all available languages"""
    query = "SELECT * FROM languages;"
    return database.connection.get_data(query, None)

def add_language(language):
    """Add a new languages. Returns the language id"""
    query = 'INSERT INTO languages("language_name") VALUES( %s );'
    args = (language,)
    database.connection.save_data(query, args)

    lang_id_query = 'SELECT language_id FROM languages WHERE language_name = %s;'
    result = database.connection.get_data(lang_id_query, args)
    return result[0][0] # first row, first column

def delete_language(language_id):
    """Deletes a language"""
    query = 'DELETE FROM languages WHERE language_id = %s;'
    args = (language_id, )
    database.connection.save_data(query, args)
