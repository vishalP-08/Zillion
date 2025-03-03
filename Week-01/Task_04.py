'''
Task_04 :
Write a program to create a random 4-digit OTP generator.
'''
import random

OtpGeneration = random.randint(1000, 9999) #Generate a randon 4 Digit Number as OTP.

print("Your OTP is : ", OtpGeneration)