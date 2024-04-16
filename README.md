# Technical-Assignment---Engineering

1. Deploy a MySQL instance (in docker or using tools like MYSQL Workbench)loaded with e-commerce data 
(data used from - www.kaggle.com/datasets/carrie1/ecommerce-data)

2. Build a command to run SQL queries by name : 

- import mysql.connector by installing mysql-connector
- define a function to make the database connections and access the data from the table and Develop a CLI tool using Python that accepts parameters such as query name, time window, and country
- assign all the queries you want to execute to a variable as a dictionary

3. 3. Post-process the output to create derived variables/features (e.g., “Popular T-Shirt”). Why
are the features interesting? How would you know?

- define a post function to make any other operations on the data

4. Build a python package around this script - create a function for command-line execution (used argparse lib)

5. Run this against a MySQL database.
   
6. How will you manage this code? Design a SDLC process :
(a) Code versioning and standards - using code version tools like git 
(b) Product feature tracking - by creating multiple branches in the repository 
(c) Deployment - create different environments like Development, UAT and release
(d) Monitoring - make use of logs
(e) Datasets - train,test,split to validate the data
(f) Upstream and downstream Dependencies - using latest updated code and data
