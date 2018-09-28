from turtle import *
vinkel=int(input("Skriv inn en vinkel"))
while True:
    forward(200 * vinkel / 360)
    left(vinkel)