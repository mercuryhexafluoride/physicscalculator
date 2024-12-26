import math
satVel = 0#float(input("insert satellite vel"))
gravConst = 0.000000000066743
cenMass = float(input("Mass of central object in kg"))
orbRad = float(input("Orbit distance in km"))
satVel = (((gravConst*cenMass)/orbRad)**0.5)/1000#use this for units = https://rechneronline.de/g-acceleration/orbital-speed.php
print(satVel)
