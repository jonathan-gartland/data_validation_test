[![Pytest Snowflake Loading](https://github.com/jonathan-gartland/data_validation_test/actions/workflows/python-app.yml/badge.svg)](https://github.com/jonathan-gartland/data_validation_test/actions/workflows/python-app.yml)
![Pytest](https://img.shields.io/badge/tested_with-pytest-46a2f1.svg)  

![Snowflake](https://img.shields.io/badge/-Snowflake-29B5E8?style=for-the-badge&logo=snowflake&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/postgresql-4169e1?style=for-the-badge&logo=postgresql&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![GitHub](https://img.shields.io/badge/-GitHub-%23181717?&style=for-the-badge&logo=GitHub&logoColor=white)
![GitHub-Actions](https://img.shields.io/badge/-GitHub%20Actions-%23181717?&style=for-the-badge&logo=GitHub%20Actions&logoColor=white)
![Linode](https://img.shields.io/badge/linode-00A95C?style=for-the-badge&logo=linode&logoColor=white)
![IntelliJ IDEA](https://img.shields.io/badge/IntelliJIDEA-000000.svg?style=for-the-badge&logo=intellij-idea&logoColor=white)  


# data_validation_test
<span style="font-size:22px;">
simple check that moving data from postgres to snowflake worked  
  
I wanted to practice with ![Snowflake](https://img.shields.io/badge/-Snowflake-29B5E8?style=for-the-badge&logo=snowflake&logoColor=white) and decided to use a ![PostgreSQL](https://img.shields.io/badge/postgresql-4169e1?style=for-the-badge&logo=postgresql&logoColor=white) sample database, dvdrental, as the source.  

I used the psycopg2 library to connect to the postgresql database, hosted on ![Linode](https://img.shields.io/badge/linode-00A95C?style=for-the-badge&logo=linode&logoColor=white),   and the 
snowflake-connector-python library to 
connect to the snowflake database.  

I created a simple script that moves data from the postgresql database to the snowflake database.  

I then created a test script that checks if the data was moved correctly.  

PyTest is the test runner. I wrote a quick validation that the same number of tables 
would be present in each resource. Once that was passing consistently, I added a paramaterized test to check row 
counts for a few tables, expecting the response to be the same in both environments.

Once I had the passing tests, I moved the tests to this project and added a github action to run the tests. 
The github action is triggered by a push or merge to the main branch, or can be run through the actions interface.  
</span>
