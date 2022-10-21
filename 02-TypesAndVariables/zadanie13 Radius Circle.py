##
# Calculation of the area and circumference of a circle#

import math as M  
# determine radius 
Radius = float (input ("Please enter the radius of the given circle: "))  

# determine pi
# import math as M 
# M.pi

# calculate area
area_of_the_circle = M.pi* Radius * Radius  

# alternative Pi
# π = 3.14  
# calculate area
# area_of_the_circle = π * Radius * Radius  

# Calculation of the circumference of a circle#
# circum = 2πr
circumference_of_the_circle = M.pi * M.pi * Radius 

print (" The area of the given circle is: ", area_of_the_circle) 
print (" The circumference of the given circle is: ", circumference_of_the_circle)  











