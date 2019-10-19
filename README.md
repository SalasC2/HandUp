# Description
Handup is an application that makes it easier for nonprofits to get the help that they need.

# Initial Setup
### Make sure you have the latest python3 installed by running
``` python3 --version```
### Create an environment using 
``` python3 -m venv venv ```
### Activate venv using
```virtualenv venv```
### Install dependencies
``` pip install -r requirements.txt```
### Export flask app to run server using
``` export FLASK_APP=handup.py ```
### To run server 
``` flask run ```
#### 🤓 Congratulations! Your server is now running on [http://127.0.0.1:5000/ ](http://127.0.0.1:5000/) 

# Database Setup
### To create database
``` flask db init ```

### Run migrations
``` flask db migrate -m "Company Table" ```
``` flask db migrate -m "Need Table" ```

# Schema Design 
| Tables |  
|---|
|  Company | 
|  Need | 

_______

|Company|
|---|
|  compamy_name | 
|  company_vision  |
|  date_founded | 

_______

|Need|
|---|
|  supplies_needed | 
|  volunteers_needed  |
| money_needed |
| company_id| 