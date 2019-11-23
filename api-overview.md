# API Overview

In total there are 58 API functions. The database API is broken into several modules for maintainability: 

- admin
    - is_admin
    - list_admin_ids
    - grant_admin
    - revoke_admin

- student 
    - get_student
    - list_students
    - update_grade
    - update_level
    - revoke_student
    - grant_student

- teacher
    - create_teacher
    - get_teachers
    - get_teacher
    - update_availability
    - add_level
    - delete_level
    - get_levels
    - add_category
    - delete_category
    - get_categories
    - grant_teacher
    - revoke_teacher

- person
    - create_person
    - delete_person
    - get_person
    - get_last_person
    - list_people
    - update_login
    - update_name
    - update_contact_info
    - update_country
    - update_preferred_language
    - add_known_language
    - remove_known_language
    - get_known_languages

- submission
    - list_submissions
    - create_submission
    - delete_submission
    - mark_submission
    - get_submission

- worksheet (WIP)
    - get_worksheet
    - get_worksheets
    - create_worksheet 
    - delete_worksheet 
    - update_name 
    - update_level 
    - update_category
    - add_language (TO DO)
    - delete_language (TO DO)
    - list_languages (TO DO)

- util
    - add_category
    - add_language
    - delete_category
    - delete_language
    - list_categories
    - list_languages
