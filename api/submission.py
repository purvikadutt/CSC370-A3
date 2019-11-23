# Submission API Functions

from . import database

def list_submissions(worksheet_id):
    """List all the submissions for a worksheet"""
    query = 'SELECT * FROM submission WHERE worksheet_id=%s;'
    args = (worksheet_id,)
    return database.connection.get_data(query, args)

def delete_submission(submission_id):
    """Delete a submission by submission_id"""
    query = 'DELETE FROM submission WHERE submission_id=%s;'
    args = (submission_id,)
    database.connection.save_data(query, args)

def mark_submission(worksheet_id, submission_id, teacher_account_id, percentage, feedback, suggested_worksheet_id):
    """Mark a student's submission (Used by teachers)"""
    query = 'INSERT INTO marks VALUES( %s,%s,%s,current_time,%s,%s,%s );'
    args = (worksheet_id,submission_id,teacher_account_id,percentage,feedback,suggested_worksheet_id)
    database.connection.save_data(query, args)

def create_submission(worksheet_id, filename, student_account_id):
    """Create a new submission. (Used by admins)"""
    query = 'INSERT INTO submission VALUES ( DEFAULT,%s,%s,%s,current_time );'
    args = (worksheet_id, filename, student_account_id)
    database.connection.save_data(query, args)

def get_submission(worksheet_id, submission_id):
    """Get a specific submission"""
    query = 'SELECT * FROM submission WHERE worksheet_id=%s and submission_id=%s;'
    args = (worksheet_id,submission_id)
    return database.connection.get_data(query, args)
