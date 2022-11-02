# Lab 9
### Instructions
Using the Python code example we wrote to call a 3rd party API, and the Node code we used to create our own API, create a Python script that calls your Node API and returns a list of the widget names and their respective colors in an easy to read format, like:

```
Widget1 is blue.Widget2 is green.
```

Etc…

The best way to do this is to run your Node.JS script and python script on the same server. Run the node API server you created, then call it using localhost:3000 in your python script.

Formatting the output is important in this lab.

----
### Solution
For my solution, I created a simple API server utilizing JS and the instruction from [class module 10](https://it3038c.github.io/IT3038C/modules/10) and created a script to call upon the API server utilizing python. 

#### Python Code:
This first block of code serves to request the data from the API server hosted on port `3000` locally. This data is then ingested and stored as json data in the `data` variable
```python
import  json
import  requests

r = requests.get('http://localhost:3000')
data = r.json()
```
After this, we create a simple iteration script to iterate through `x` number of lines in the script while formatting our data appropriately. 
```python
i = 0
for  x  in  data:
	widgetX = data[i]
	print(widgetX['name']+' is '+widgetX['color'])
	i = i+1
```
#### Final Python Code:

```python
import  json
import  requests

r = requests.get('http://localhost:3000')
data = r.json()

i = 0
for  x  in  data:
	widgetX = data[i]
	print(widgetX['name']+' is '+widgetX['color'])
	i = i+1
```
#### Expected output:
```bash
widget1 is blue
widget2 is green
widget3 is black
widgetX is blue
```
---
### How to install
1. download the `lab9` folder from GitHub
2. extract the contents of the folder
3. Navigate to the directory via `cd lab9`
4. start the node server via `node api.js`
5. once the node server is running, run the python script by typing
	`python3 lab9.py`
---
### Author 
Jordan Wentland - Wentlajc
