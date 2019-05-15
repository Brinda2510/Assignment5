import matplotlib.pyplot as plt
import numpy as np
from collections import Counter
import cv2
import pandas as pd

num = ["TRUE" if i%2==0 else "FALSE" for i in range (1301)]
print(num)

import functools
q=range(1,10)
print (functools.reduce(lambda x,y:x*y,q)) 

def f(x):
    def g(y):
        return y + x 
    return g
nf1 = f(1)
nf2 = f(3)
print(nf2(1))

def longest_word(filename):
    with open(filename, 'r') as infile:
              words = infile.read().split()
    max_len = len(max(words, key=len))
    return [word for word in words if len(word) == max_len]
print(longest_word('test.txt'))


class Triangle:
     def __init__(self,a,b,c):
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)
    def area(self):
        s=(self.a + self.b + self.c)/2
        return((s*(s-self.a)*(s-self.b)*(s-self.c))**0.5)
a=input("Enter the value of a = ")
b=input("Enter the value of b = ")
c=input("Enter the value of c = ")
t = Triangle(a, b, c)
print("area : {}".format(t.area()))

import random
lowercase= 'abcdefghijklmnopqrstuvwxyz'
uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '0123456789' 
punctuation = '!"#$%&\'()*+,-./:;<=>?@[]^_{|}~'
allowed = lowercase + uppercase + digits + punctuation
visually_similar = 'Il1O05S2Z'
def new_password(length:int, readable=True) -> str:
    if length < 4:
        print("password length={} is too short,".format(length),
            "minimum length=4")
        return ''
    choice = random.SystemRandom().choice
    while True:
        password_chars = [
            choice(lowercase),
            choice(uppercase),
            choice(digits),
            choice(punctuation)
            ] + random.sample(allowed, length-4)
        if (not readable or 
                all(c not in visually_similar for c in password_chars)):
            random.SystemRandom().shuffle(password_chars)
            return ''.join(password_chars)
def password_generator(length, qty=1, readable=True):
    for i in range(qty):
        print(new_password(length, readable))


def list_ends(a_list):
    return [a_list[0], a_list[len(a_list)-1]]
a_list[1,1,2,3,4]


def sec(n):
    main=list(1,2,3,4)
    even=list()
    odd=list()
    index=0
    for number in main:
        if index%2!=0:
            even.append(number)
        else:
            odd.append(number)
        index +=1
    final_even = " enter number".join(even)
    final_odd = "enter number".join(odd)
    print(final_even)
    print(final_odd)
sec('1,2,2,3,4,5,6,7')


sec = ['abc','def','ghi','ert','yui']
def divide(l,n):
    for i in range(0, len(l), n):
        yield l[i:i + n]
n = 3
x = list(divide(sec, n))
while n>0:
    n+=1
    if n==3:
        break
print(x)
