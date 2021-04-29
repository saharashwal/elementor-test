My design is a python microservice that run periodicly every 30 minuets.
The microservice download the datasource at first and afterwords check if the sites are risky or not
based on the totalvirus API and wirting the results to the DB.

on AWS, i would use:
 - EC2 for my microservice
 - S3 for my datasource
 - MSSQL database
