Fast-Food-Fast-API
FastFood API is a REST API that fetches that allows its user to order for food

[![Build Status](https://travis-ci.org/misatifelix/fast-food-fast-api.svg?branch=master)](https://travis-ci.org/misatifelix/fast-food-fast-api)


This is a list of resources for people who are new to contributing to open source.

Flask FAST FOOD FAST
This is a Flask Restful API for an app that allows customers to place orders

Installation and Setup
Clone the repo

git clone https://github.com/misatifelix/fast-food-fast-api.git

Switch the develop branch

git fetch origin develop

Navigate to the folder

cd Fast-Food-API

create a virual env

virtualenv venv

Activate the venv

source/venv/activate

Install the required packages

pip install -r requirements.txt

Launch the program
python run.py

Use Postman to the test the following endpoints

API Auth
Endpoint	Method	description
/api/v1/register	POST	add a new user
/api/v1/login	POST	User Login token
/api/v1/logout	POST	User logout
API Endpoints
# Endpoint	# Methods	# Description	Auth Required
/api/v1/foods	GET	list all foods	No
/api/v1/food/	GET	get a specific food	No
/api/v1/foods	POST	add a new food	Yes
/api/v1/foods/	PUT	edit the food-item	Yes
/api/v1/order/	GET	get a specific order	No
/api/v1/orders	POST	add a new order	Yes
/api/v1/order/	PUT	edit the order-status	Yes
/api/v1/orders	GET	list all orders	No
API DOCUMENTATION
PostMan Docs

HEROKU LINK
HEROKU API

Author
Felix Misati
