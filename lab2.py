"""Lab Assignment 2: converting from Fahrenheit to Celsius and vice versa
   Conversions: °C * 9/5 + 32 = °F  ||  (°F - 32) * 5/9 = °C"""
__author__ = 'Jenny Hamer'

def convert_to_Celsius(number):
    degreesC = (number - 32) * 5/9
    #print(number, " degrees Fahrenheit equals {0:.1f}°C".format(degreesC))
    return degreesC #returns a number
    

def convert_to_Fahrenheit(number):
    degreesF = number * 9/5 + 32
    #print(number, " degress Celsius equals {0:.1f}°F".format(degreesF))
    return degreesF #returns a number
    

"""
convert_to_Celsius(56) 
convert_to_Fahrenheit(11.5) 
output:
56  degrees Fahrenheit equals 13.3°C
11.5  degress Celsius equals 52.7°F
"""
