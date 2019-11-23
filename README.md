# CSC 370 Assignment 3

## Overview
To connect to the database using Python an API was built to easily allow programmers to manpiulate data in the database. For example, to list all students in the database:

```python
import api.student
print(api.student.get_students())
```

## API Overview

An overview of the API is available in the api-overview.md file.

## Examples

Some examples are provided in this assignment to showcase the use of the API.

## Running the API
To connect to the PostgreSQL server, you must add your username and password in the _api/config.py_ file. Note: Do not commit your credentials to git. 

## Technical Details

### Database API Structure
The Database API is contained within the API folder. 

### Infrastructure
- config.py: All the configuration information required to connect to PostgreSQL is stored here.
- database.py: The **main** wrapper class used to execute statements on the database.
