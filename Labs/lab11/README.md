# Lab 11 - Python and Flask

## Description

### Goal
The goal of this lab was utilize python and the flask dependencies to generate a website to take in users name and display it back to them on a welcome page.

---

### Technical

This application utilizes the Python library Flask and App to generate a website. Using specified routes, we are able to serve specific html content using our `layout.html` file as basic design and the `welcome.html` and `index.html` files to modify that basic layout script. Utilizing post methods and forms within our `index.html` file, we are able to capture our user input and pass it along to the `welcome.html` template. 

---

#### The structure
```
Python Flask App
│   web.py
│   routes.py
│   README.md
└───templates
│   │   layout.html
│   │   index.html
│   │   welcome.html
```
---

#### End note: 
```
This project has been a lot of fun for learning flask and its utilities.
```
---

## Getting Started

### Installing

To install and initialize this program, you can do it in 1 of 2 ways

* Method 1 (git): 
	* download the repository by running 
	 ```git clone https://github.com/JordanCWentland/it3080c-scripts.git```
	 * After this, navigate into: ```it3080c-scripts\labs\lab11```
	 * run script utilizing ```python web.py```
* Method 2 (download):
	* download the ```lab11``` folder from the [Labs folder](https://github.com/JordanCWentland/it3080c-scripts/tree/main/Labs). 
	 * run script utilizing ```python web.py```
---
### How to use the program

after running ```python web.py``` a web-server will by started on your machine at http://localhost:5001. By navigating to this page, you will be greeted with the application.


---

### Authors

Jordan Wentland for IT-3080c
