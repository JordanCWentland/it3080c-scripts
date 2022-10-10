
# Overwatch 2 Average Rank Calculator 

## Description

### Goal
This python script is designed to help teams find an appropriate rank for scrimmaging other teams with the new ranking system. Utilizing no additional dependencies besides the base python package, this application creates a quick and efficient method for calculating the average rank. 

### Technical

More technically, this application takes players' ranking data such as "silver 1" or "diamond 2" and applies an arbitrary value for calculation purposes. In the case of a player who is silver 1, the value "silver" is given a score of 20 and the value 1 ends up being valued at 5. After this, the values are combined and stored in an array. When averaging the rank, these numbers are split back into 20 and 5 accordingly. The value 20 is used to look up the rank in the rank dictionary to determine the teams average rank and then the divisions are averaged and rounded to the nearest whole number to determine the division for the team.

This project is still a WIP and will undergo many changes. Down the pipeline is to turn this application into a web based app. 

## Getting Started

### Installing

* Simply download the Overwatch2SRcalculator.py file and run it. 

### How to use the program

* After running the program, you will be introduced to a prompt to enter data.
* Enter users rankings in the following format: (rank) (division) (eg. silver 1)
* acceptable rank inputs include: 
```
bronze 
silver
gold 
platinum
diamond
masters
grandmasters
```
* acceptable division inputs include:
```
1
2
3
4
5
```
* If an improper input is made, the program will prompt you for a proper input.
* Once the inputs for the ranks have been entered, the program will display your teams average ranking. 

### SAMPLE DATASET

If you are looking for a way to test the validity of the information, you can input the following data as a sample set:
```
gold 1 
gold 2
platinum 3 
platinum 1
diamond 1
```
This data set should return the value "Platinum 2".

### Goal for this script 

For this script's purpose, I wanted to help make my life as the Overwatch Club's Vice President easier by creating a tool to assist in this process rather than relying on guessing. Technically, I wanted to utilize arrays, lists, and functions more as I have not touched on these much. I want to continue development of this script, turning it more into a web application that can be utilized much easier overall. 

## Authors

Jordan Wentland for IT-3080c 