valid = [student_name, Score, _count, max_value_1]
#2nd_place is an invalid name because python doesn't start with numbers.

exam_score = "A student's exam score is 90"
student_age = "A student's age is 20"
total_price = "The total price of a shopping cart #5000"

city_population = '1_250_000'
print(type(city_population))
temperature = '-3.5'
print(type(temperature))
#is_raining = your choice
#print(type(is_raining))
#middle_name = the "no value yet" value
#print(middle_name)
#school_name = your schools name
#print(school_name)

a = 10
b = a 
a = 20
#The final value of a and b is 20 and 10.
print(a, b)
#yes
#Remember python reads code line by line, so the first line say that a = 10, and then b = a, automatically b = 10.

#***prediction***
#1. "int"
#2. "float"
#3. "float"
#4. "bool"
#5. "string"
#6. "None"
print(type(7))
print(type(7.0))
print(type(7 + 2.5))
print(type(True))
print(type("7"))
print(type(None))
#none of the result surprised me, because i understand python type very well.

#predication
level = 1
Level = 2
LEVEL = 3
#(level + Level + LEVEL) = 6
print(level + Level + LEVEL)
#This show that python is case sensitive.

quantity_text = "12"
unit_price_text = "4.50"
quantity_text = int("12")
unit_price_text = float("4.50")
total_cost = quantity_text * unit_price_text
print(total_cost)
#The answer is a float because whatever type that mutiplies a float automatically becomes a float.
total_cost_text = str(total_cost)
print(type(total_cost_text)) 

#int("apple")
#print(int("apple"))
#ValueError because apple is a string and not an integer.
print(int("25"))
#This is because 25 is a number given in a string form, and can be conversed to an integer by using int.
#predict
#int(3.9) gives 3 because it doesn't round up.
#int(-3.9) gives -3 because it doesn't round up.
#float(5) give 5.0 because float are always in decimal form.
print(int(3.9))
print(int(-3.9))
print(float(5))

item_name = "Notebook"
price_text ="2.75"
quantity_text_9 = "4"
discount_percent = 10
is_member = True
price_text = float("2.75")
quantity_text_9 = int("4")
subtotal = price_text * quantity_text_9
print(subtotal)
discount_amount = subtotal - discount_percent / 100
print(discount_amount)
final_total = subtotal - discount_amount
print(final_total)
print(type(is_member))
