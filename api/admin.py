# Admin API Functions
from . import database

# Admin Functions
def is_admin(account_id):
    """Returns true if the account_id is an admin"""
    query = 'SELECT admin_id FROM admin WHERE admin_id = %s;'
    args = (account_id,)
    results = database.connection.get_data(query, args)

    return len(results) == 1

def list_admin_ids():
    """Lists all the admin ids"""
    query = 'SELECT admin_id FROM admin;'
    return database.connection.get_data(query, None)

def grant_admin(account_id):
    """Grants an account to be an administrator"""
    query = 'INSERT INTO admin(admin_id) VALUES( %s );'
    args = (account_id, )
    database.connection.save_data(query, args)

def revoke_admin(account_id):
    """Revokes the admin permissions for an account"""
    query = 'DELETE FROM admin WHERE admin_id = %s;'
    args = (account_id, )
    database.connection.save_data(query, args)
