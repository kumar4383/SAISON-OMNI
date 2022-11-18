# Saison-omni

Saison-omni search project is used to maintain food truck information.

## Tech Stack

Language : Python,
Framework : Django,
Database: Elasticsearch,
Hosted on : AWS

## Applicant Entity

```bash
Id : UUID
applicant: str (Name)
address: str (street address)
locationDescription : str
expirationDate : date
location : []
```

## Installation

Code base can be cloned from https://github.com/kumar4383/saison-omni.git

Kindly follow below process to run it locally

```bash
pip install pipenv
git clone https://github.com/kumar4383/saison-omni.git

cd saison-omni
pipenv shell
pipenv install

./runserver.sh

```

## Postman collection

https://www.getpostman.com/collections/222e9d1eadda765aac05

Rest end-points are pointing to AWS server if you run the project locally, you have to update the apis.
