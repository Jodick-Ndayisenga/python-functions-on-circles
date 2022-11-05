from math import sqrt

print('Welcome to circle computation.')
firstname= input('What is your name please?: ')

r = ['radius','r']
d = ['diameter','d']
c = ['circumference','c']
a = ['area','a']

data = input('Do you want to enter the radius, diameter, circumference or area? ')

def radius(x):
    print('Dear', firstname, ', based on the date you privided, the radius of the circle is: ', x)
    diameter = x *2
    print('The diameter of the circle is', diameter)

    circumference = round(22/7 * diameter)
    print('The circumference of the circle is', circumference)

    area = round(22/7 * x**2)
    print('The area of the circle is', area)

if data in r:
    rad = int(input('Enter the radius:'))
    radius(rad)

def diameter(v):
    print('Dear', firstname, ', based on the date you privided, the diameter of the circle is: ', v)
    radius = v/2
    print('The radius of the circle is', radius)

    circumference = round(22/7 *v)
    print('The circumference of the circle is', circumference)

    area = round(22/7 * radius**2)
    print('Area of the circle is', area)

if data in d:
    diam = int(input('Enter the diameter: '))
    diameter(diam)

def circumference(p):
    print('Dear', firstname, ', based on the date you privided, the circumference of the circle is: ', p)
    radius = round(p/ (2*22/7 ))
    print('The radius of the circle is', radius)

    diameter = radius*2
    print('The diameter of the circle is', diameter)

    area = round(22/7 * radius ** 2)
    print('The area of the circle is', area)

if data in c:
    circ = int(input('Enter the circumference of the circle: '))
    circumference(circ)

def area(y):
    print('Dear', firstname, ', based on the date you privided, the area of the circle is: ', y)
    radius = round(sqrt(y/22/7)) 
    print('The radius of the circle is', radius)

    diameter = radius *2
    print('The diameter of the circle is', diameter)

    circumference = round(22/7 *diameter)
    print('The circumference of the circle is:', circumference)

if data in a:
    ar= int(input('Enter the area of the circle: '))
    area(ar)