from tabulate import tabulate

#Static GPA List 
print("##################\n USE CASE 1\n##################")
table = [["Jordan", "Male", "3.8"],["Janet", "Female", "4.2"],["James", "Male", "3.4"],["Hailey", "Female", "3.9"],["Tori", "Undisclosed", "4.5"]]
gpaHeaders =["name", "gender", "gpa"]
gpa = tabulate(table, gpaHeaders)
print(gpa)

#Turning tables into HTML format
print("##################\n USE CASE 2\n##################")
htmlOut = tabulate(table, gpaHeaders, tablefmt="html")
print(htmlOut)

#Generating a receipt in terminal
print("##################\n USE CASE 3\n##################")
x=0
total=0
print("Welcome to the ingredient order service!")
a = int(input("How much bread would you like to order?: "))
b = int(input("How much cheese would you like to order?: "))
c = int(input("How much Meat would you like to order?: "))
d = int(input("How many condiment sets would you like to order?: "))
table2 = [["Bread", .75, a],["Cheese", .50, b],["Meat", 1.0, c],["Condiments", .25, d],]
headers = ["Item", "Price","Quantity"]
test2 = tabulate(table2, headers,tablefmt="pretty")
while x <= 3:
    if x == 0:
        temp = (table2[x][1])*a
        total += temp
        x+=1
    elif x == 1:
        temp = (table2[x][1])*b
        total += temp
        x+=1
    elif x == 2:
        temp = (table2[x][1])*c
        total += temp
        x+=1
    elif x == 3:
        temp = (table2[x][1])*d
        total += temp
        x+=1
print(test2)
print(f"your total order is: ${total}")