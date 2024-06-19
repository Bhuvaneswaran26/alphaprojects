print("Welcome to the depth calculator by using stone")
print("Procedure : Take a stone and timer while throwing the stone into the well start the timer . when you are getting the sound stop the clock")
print("---Note the timing and enter into the depth calculator---")
sum=0
for i in range(1,4):
    print("Enter the time in seconds reading--",i)
    time=float(input())
    sum+=time
time=sum/3
c=345*time
accuratetimep=(-345+((345**2)-4*4.905*c)**0.5)/(2*4.905)
accuratetimen=(-345-((345**2)-4*4.905*c)**0.5)/(2*4.905)
if accuratetimep>accuratetimen:
    t=accuratetimep
    
else:
    t=accuratetimen
    t=+t
if t<0:
    t=-t
depth=4.905*t*3.282
depth=round(depth,2)
print("Depth of the well is {} feets".format(depth))
