from matplotlib import pyplot as plt
import numpy as np

X,Y = np.meshgrid(np.linspace(-2,7,1000),np.linspace(-4,14,1000))

fig = plt.figure()
ax = plt.axes(projection="3d")
ax.plot_surface(X,Y,3*X+2*Y,color="cyan",alpha=0.25)

X = np.linspace(0,1,100)
Y = np.linspace(0,0,100)

ax.plot3D(X,Y,3*X+2*Y,"black")

Y = np.linspace(10,10,100)
ax.plot3D(X,Y,3*X+2*Y,"black")

X = np.linspace(0,0,100)
Y = np.linspace(0,10,100)
ax.plot3D(X,Y,3*X+2*Y,"black")

X = np.linspace(5,5,100)
Y = np.linspace(4,6,100)
ax.plot3D(X,Y,3*X+2*Y,"black")

X = np.linspace(1,3,100)
Y = np.linspace(0,1,100)
ax.plot3D(X,Y,3*X+2*Y,"black")

Y = np.linspace(10,9,100)
ax.plot3D(X,Y,3*X+2*Y,"black")

X = np.linspace(3,4,100)
Y = np.linspace(1,2,100)
ax.plot3D(X,Y,3*X+2*Y,"black")

Y = np.linspace(9,8,100)
ax.plot3D(X,Y,3*X+2*Y,"black")

X = np.linspace(4,5,100)
Y = np.linspace(2,4,100)
ax.plot3D(X,Y,3*X+2*Y,"black")

Y = np.linspace(8,6,100)
ax.plot3D(X,Y,3*X+2*Y,"black")

X = np.array([0,1,1,3,4,5,5,4])
Y = np.array([0,0,1,1,2,4,6,8])
Z = 3*X + 2*Y
ax.scatter(X,Y,Z,color="red")

xdir = X[1:] - X[:len(X)-1]
ydir = Y[1:] - Y[:len(Y)-1]
zdir = Z[1:] - Z[:len(Y)-1]
ax.quiver(X[:len(X)-1],Y[:len(Y)-1],Z[:len(Z)-1],xdir,ydir,zdir,color="red")

plt.show()

