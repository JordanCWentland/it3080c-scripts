

# Overwatch 2 Average Rank Calculator 

## Description

### Goal
This script was designed with the goal of allowing people to easily calculate their Overwatch 2 teams average rank for practicing purposes. This script utilizes Javascript with express and morgan as well as HTML to accomplish this task.

---

### Technical

This application utilizes the Javascript libraries Express and Morgan to serve up a static HTML webpage which is used to call upon a backend Javascript file which calculates the teams average SR based on the options provided in the drop down menus. 

---

#### The Javascript webserver: 
The webserver of this script is an exploration of both Morgan and Express for the creation of webpages and serving content to users. When this script is ran, it automatically imports the content from the /content folder and allows it to be queried and displayed dynamically. If additional pages were to be added, this webserver setup would be able to query those pages and make them accessible.

---

#### The Frontend:
The frontend of this script is a HTML file which contains many different < select > statements to handle the dropdown menu functionality. Each select is given a id value which is then queried upon to grab the current value of the dropdown option selected. This is where the backend comes ins. 

---

#### The Backend:
The backend of this script is once again a Javascript file. This script does not use any external libraries other than the default ones. This script serves to do all of the calculation for the average of the teams ranking. A button in the front end html calls upon this script by the following:
```
<input type="button" name="clickbtn" value="Submit" onClick="buttonPressed()" style="font-size: 19px"/>
```
When the button is pressed, the backend script pulls the ID values from the many 
< select > tags and then calculates the averages of these by comparing against a dictionary to turn the text into a value.

---

#### The structure
```
Overwatch 2 Calculator
│   main.js
│   package.json
│   README.md
└───Content
│   │   project2.html
│   └───jscript
│       │   calc.js
```
---

#### End note: 
```
This project is still a WIP and will undergo many changes. Next tasks include:
- [x] Prettify the code
- [backlog] Allow for a variable amount of players
- [wip] optimize the web flow
- [ ] mobile optimization
```
---

## Getting Started

### Installing

To install and initialize this program, you can do it in 1 of 2 ways

* Method 1 (git): 
	* download the repository by running 
	 ```git clone https://github.com/JordanCWentland/it3080c-scripts.git```
	 * After this, navigate into: ```it3080c-scripts\Project2\src```
	 * run ```npm install``` to install the script dependencies 
	 * run ```node main.js``` to start the webserver
* Method 2 (download):
	* download the ```src``` folder from the [Project 2 page](https://github.com/JordanCWentland/it3080c-scripts/tree/main/Project1). 
	* navigate into the src folder
	* run ```npm install``` to install the script dependencies
	* run ```node main.js``` to start the web-server
---
### How to use the program

after running ```node main.js``` a web-server will by started on your machine at http://localhost:8000/project2.html. By navigating to this page, you will be greeted with the HTML Front end. 

The dropdowns are labelled with the different Player identification and can be modified to adjust the calculator. Once you have selected the values you want from the dropdowns, click the ```submit``` button the calculate the teams average. 
Have fun!

---

### SAMPLE DATASET

The following data set below can be used to verify the output of the 
```
platinum 5
gold 5
platinum 2
gold 3
silver 1
```
This data set should return the value "platinum 5".

---

### Authors

Jordan Wentland for IT-3080c 
