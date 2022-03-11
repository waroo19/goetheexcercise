__author__ = "7076367, Vu"

#A1


#ver01(nicht endlosschleife)
import random
number = random.randint(-9,9)

count = 0

while number != -7 and number != 8 :
  
    number = random.randint(-9,9)
    count += 1

print("Zahl =", number, "Anzahl der Würfer =", count)

#ver02(endlosschleife)
import random
count = 1
i = 0
while i == 0 :
    number = random.randint(-9,9)
    if number == -7 or number == 8:
       break
    count += 1

print("Zahl =", number, "Anzahl der Würfer =", count)

#A2

#1
sum = 0
for x in range(3,24):
  if (x % 2) == 0:
     sum = sum + x
     print("Ergebnis =", sum)

#2

number = int(input("Geben Sie eine ganzzahlige Zahl ein"))
sum = 0
count = 0

if number > 0:
    for x in range(1, number + 1):
       sum += x
       count += 1
else:
      for x in range(1, number - 1, -1):
       sum += x
       count += 1


average = sum / count
print("Der Durchschnitt =", average)

#3


number = eval(input("Geben Sie eine ganzzahlige Zahl ein"))
count = 0
number_list = []
if number > 0:
    for x in range(1, number + 1):
       number_list.append(x)
       count += 1
else:
      for x in range(1, number - 1, -1):
       number_list.append(x)
       count += 1

if (count % 2) == 0:
    index_m = count//2
    index_n = count//2 - 1
    median = (number_list[index_m] + number_list[index_n]) / 2
else:
    median = number_list[count // 2] 


print("Median =", median)

#3
i = 0

while i == 0:
    ask_user = eval(input("Geben Sie 1 für R_Wert, 2 für die Anzahl der Infizierten und 3 für Quit"))
    #Eingabe 1
    if ask_user == 1:
     infection_cases_1 = eval(input("Anzahl der Fällen bei T1 ="))
     infection_cases_2 = eval(input("Anzahl der Fällen bei T2 ="))   
     r_value = infection_cases_2 / infection_cases_1
     print("R_Wert =", r_value)
    #Eingabe 2
    if ask_user == 2:
       out_value = eval(input("Ausgangsgröße ?"))
       rvalue = eval(input("R_Wert ?"))
       interation = eval(input("Interation ?"))
       infection_cases = out_value * rvalue ** interation
       print("Anzahl der Infizierten =", infection_cases)
    #Eingabe 3
    if ask_user == 3:
        print("Programm wird beendet")
        break   