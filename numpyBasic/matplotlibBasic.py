import matplotlib.pyplot as plt
import numpy as np

def tryPlot():
    #create from 0 to 2pi 50 elements
    x = np.linspace(0,2*np.pi,50)
    #plot elements of array in argument as y
    plt.plot(np.sin(x))
    plt.show()

    #plot multiple data set as pair of array xyxyxy...
    plt.plot(x,np.sin(x),x,np.sin(2*x))
    plt.show()

    a = np.random.rand(200)
    b = np.random.rand(200)
    size = np.random.rand(200) * 30
    color = np.random.rand(200)
    #size can be array of individual size of each dot or just one value
    #color is array of color of individual dots
    plt.scatter(a,b,size,color)
    plt.colorbar()
    plt.show()
    #if u just use plot without show it will plot everything on same figure
    #and then show everything when u call show

def tryFigure():
    #You can also use figure() to create new figure and plot on it
    #put in first figure
    x = np.linspace(0, 2 * np.pi, 50)
    a = np.random.rand(200)
    b = np.random.rand(200)
    plt.figure()
    plt.scatter(a,b)
    #put these into second figure
    plt.figure()
    plt.plot(x)
    plt.scatter(a,b)
    #show all 2 figures
    plt.show()
    #plt.hold(False) will make it clear figure everytime you call plot

def trySubplot():
    #multiple plot on same figure
    #subplot(row,columns,active plot) (one bas index)
    x = np.array([1,2,3,2,1])
    y = [1,3,2,3,1]
    plt.subplot(2,1,1)
    plt.plot(x)
    #if the position of plot over lap the new plot will be shown
    plt.subplot(4,2,6)
    plt.plot(y)
    plt.show()

def tryLegendAndLabels():
    #using legend and labels
    #following 2 are identical

    #this is easier to keep track
    x = np.linspace(0, 2 * np.pi, 50)
    plt.plot(np.sin(x), label ='sin')
    plt.plot(np.cos(x), label ='cos')
    #display grid at background
    plt.grid()
    plt.legend()

    plt.figure()
    plt.plot(np.sin(x))
    plt.plot(np.cos(x))
    leg = ['sin','cos']
    plt.legend(leg)
    #adding x,y label and title
    plt.xlabel('randians')
    plt.ylabel('amplitude', fontsize = 'large')
    plt.title('sinx and cosx')

    #clears figure but leave figure there
    #plt.clf()

    #close currently active figure
    #close()

    #close all figures, usually run at the top of the script to clear all other existing plot
    #close('all')

    plt.show()

tryLegendAndLabels()