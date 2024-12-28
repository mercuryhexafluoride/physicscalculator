import math
satVel = 0#float(input("insert satellite vel"))
satMass = float(input("what is the mass of your satellite"))
satPot = 0
satKin = 0
gravConst = 0.000000000066743
cenMass = float(input("Mass of central object in tons"))
orbRad = float(input("Orbit distance in km from core(add planet size)"))
satVel = (((gravConst*cenMass)/orbRad)**0.5)#use this for synchronising units = https://rechneronline.de/g-acceleration/orbital-speed.php
print("your satellites' speed should be",satVel)#equation used = v = sqr(Gm/r)
satKin = (gravConst*satMass*cenMass)/(2*orbRad)
satPot = -(gravConst*satMass*cenMass)/(orbRad)
satEnerg = satPot+satKin#equation used = e+u = -(GMm/2r), not yet scaled to units or tested
print(satEnerg)
