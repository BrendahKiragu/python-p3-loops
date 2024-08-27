#!/usr/bin/env python3

def happy_new_year():
   count_down = 10
   while count_down > 0:
       print(count_down)
       count_down -= 1
   print('Happy New Year!')     
# happy_new_year()      


def square_integers(int_list):
    squared_integers = [ints ** 2 for ints in int_list]
    return squared_integers

# print(square_integers([2, 3, 4, 5, 6]))


def fizzbuzz():
   for num in range(1, 101):
       if (num % 3 == 0 and num % 5 == 0):
           print('FizzBuzz')
       elif num % 3 == 0:
           print('Fizz')
       elif num % 5 == 0:
           print('Buzz')
       else:
           print(num)
fizzbuzz()                   
