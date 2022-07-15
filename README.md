
# روش اول
for number in range (1,100):
   if number % 3 == 0 and number % 5 == 0:
      print('Hop-Wiz')
   elif number % 3 == 0:
      print('Hop')
   elif number % 5 == 0:
      print('Wiz')
   else:
      print(str(number))

-----------------------------------

# روش دوم - بهتر

for number in range (1,100):
    decision = 'Hop-Wiz' if not number % 15 else 'Hop' if not number % 3 else 'Wiz' if not number % 5 else str(number)
    print(decision)

------------------------------------
# روش _سوم _

for number in range (1,100):
    decision = 'Hop-Wiz' if not number % 15 else 'Hop' if not number % 3 else 'Wiz' if not number % 5 else str(number)
    print(decision)
