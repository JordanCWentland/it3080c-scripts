# Lab 7 Wentlajc

The python script I created utilizes a pthon plugin called tabulate

First, install virtualenv
```bash
pip install virtualenv
```
Next, we will create a virtual environment to play around with the script.

```bash
virtualenv ~/venv/tabulate
source ~/tabulate/scripts/bin/activate
pip install tabulate
```

Next, you will want to clone this repository down using git to run our python script!
```bash
git clone https://github.com/JordanCWentland/it3080c-scripts/tree/main/Labs/Lab7
```
After this, you will want to navigate to our downloaded script 
```bash
cd Lab7
```
Once in this directory, you can run my script by typing 
```python
python3 lab7.py
```
What this will do is run the script and give sample output of tables with tabulate and initiate the interactive session of the script. 

Essentially, tabulate is a plugin that is utilized within python to make making tables even easier than ever. In my script, the following happens:

1.) The first table is a basic table output with headers 

2.) The second table is the same table, formatted for use with HTML. 

3.) the third use case is designed to generate a receipt of sale and making it look pretty through tabulate.


Thank you for trying out my script! Remember, close your interactive session by running the below code in your virtualenv
```bash
deactivate
```