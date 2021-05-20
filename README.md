# UOCIS322 - Project 5 #
Brevet time calculator with AJAX and MongoDB!

## Overview

Store control times from Project 4 in a MongoDB database.

### What is in this repository

You have a minimal example of `docker-compose` in `DockerMongo`, using which you can connect a Flask app to MongoDB (as demonstrated in class). Refer to the lecture slides for more details on MongoDB and `docker-compose`. Solved `acp_times.py` file will be made available on Canvas under Files after the project due date.

## IMPORTANT NOTES

**MAKE SURE TO USE THE SOLUTION `acp_times.py` from Canvas for this project!**

**MAKE SURE TO KEEP YOUR FILES in `brevets`! REMOVE `DockerMongo` after you're done!**

## Getting started

You will reuse *your* code from Project 4 (and the solution `acp_times.py` file for consistency), meaning you will get rid of `DockerMongo` (it's just an example, like `minijax` in Project 3), and use ideas from it to make some changes.

Recall that you created a list of open and close control times using AJAX. In this project, you will add the following:

1. Add two buttons `Submit` and `Display` in the ACP calculator page.

2. Upon clicking the `Submit` button, the control times should be inserted into a MongoDB database.

3. Upon clicking the `Display` button, the entries from the database should be displayed in a new page.

Handle error cases appropriately. For example, Submit should return an error if no control times are input. One can imagine many such cases: you'll come up with as many cases as possible.

## Tasks

As always you'll turn in your `credentials.ini` using Canvas, which will point to your repository on GitHub, which should contain:

* `Dockerfile`

* `docker-compose.yml`

* The working application.

* A README.md file that includes not only identifying information (your name) but but also a revised, clear specification of the brevet control time calculation rules (you were supposed to do this for Project 4), with additional information regarding this project.

* An automated `nose` test suite with at least 2 test cases: at least one for the time calculator, and another for DB insertion and retrieval.

## Grading Rubric

* If your code works as expected: 100 points. This includes:
	* Front-end implementation (`Submit` and `Display`).
	
	* Back-end implementation (Connecting to MongoDB, insertion and selection).
	
	* AJAX interaction between the frontend and backend (AJAX for `Submit` and `Display`).
	
	* Updating `README` with a clear specification (including details from Project 4).
	
	* Writing at least 2 correct tests using nose (put them in `tests`, follow Project 3 if necessary), and all should pass.

* If the AJAX logic is not working, **10** points will be docked off. 

* If the logic to insert into or retrieve from the database is wrong, **30** points will be docked off.

* If the README is not clear or missing, up to **15** points will be docked off. 

* If any of the two test cases are incorrect or fail, up to **15** points will be docked off. 

* If none of the functionalities work, 30 points will be given assuming 
    * The `credentials.ini` is submitted with the correct URL of your repo, and
    * `Dockerfile` is present 
    * `docker-compose.yml` works/builds without any errors 

* If none of the functionalities work, 30 points will be given assuming `credentials.ini` is submitted with the correct URL of your repo, `Dockerfile` builds and runs without any errors, and `docker-compose.yml` is correct and works.

* If `docker-compose.yml` is missing, doesn't build or doesn't run, 10 points will be docked off.
    
* If `Dockerfile` is missing, doesn't build or doesn't run, 10 points will be docked off.
	
* If `credentials.ini` is not submitted or the repo is not found, 0 will be assigned.

## Credits

Michal Young, Ram Durairajan, Steven Walton, Joe Istas.