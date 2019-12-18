# Welcome to the madbox data analytics
## Pre-requisite
### Installation
Makefile

docker
docker-compose
(docker and docker-compose are 2 different softwares they have the same name though)

ODBC (MySQL connector) to connect with tableau to the MySQL

### Disclaimer
Even though python and others are used, all of these have been dockerized so don't bother looking for what libraries you should install

## Show time
### How to run the application
```
make run
```

### Wait
Wait for about 2 minutes after all docker installation.

The Facebook Prophet can take a while so let the docker do his job for at least 5 minutes.

Be reassure this long installation step happens only once.
Next you want to run the application, it will take no time!

### Open up Tableau
In ./tableau you will find a DashBoard on the Metrics generated

### How to stop the application
```
make stop
```

## Stack
Database : MySQL
Programming Language : Python / Jupyter Notebook
Library :
- Forecast : Facebook Prophet
- Data Vizualisation : Tableau