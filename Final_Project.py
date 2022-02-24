# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 12:37:38 2021

@author: 
"""


import matplotlib.pyplot as plt
import numpy as np



# defining the country-finder function
def whichCont(nameStr):
    # making the arrays of country names
    europeArr = ["Belgium",
             "Czech Rep.",
             "France",
             "Germany",
             "Italy",
             "Netherlands",
             "Poland",
             "Portugal",
             "Romania",
             "Spain",
             "Sweden",
             "United Kingdom",
             "Norway",
             "Ukraine"
              ]
    mEastArr =   ["Turkey",
              "Algeria",
              "Egypt",
              "Iran",
              "Kuwait",
              "Saudi Arabia",
              "United Arab Emirates"
              ]
    asiaArr =    ["Kazakhstan",
              "Russia",
              "Uzbekistan",
              "China",
              "India",
              "Indonesia",
              "Japan",
              "Malaysia",
              "South Korea",
              "Taiwan",
              "Thailand",
              "Australia",
              "New Zealand"
              ]
    nAmerArr =   ["Canada",
              "United States",
              "Mexico"
              ]
    sAmerArr =   ["Argentina",
              "Brazil",
              "Chile",
              "Colombia",
              "Venezuela"
               ]
    africaArr =   ["Nigeria",
               "South Africa"
               ]
    
    if nameStr in europeArr:
        return 0
    elif nameStr in mEastArr:
        return 1
    elif nameStr in asiaArr:
        return 2
    elif nameStr in nAmerArr:
        return 3
    elif nameStr in sAmerArr:
        return 4
    elif nameStr in africaArr:
        return 5
    else:
        print("The country " + str(nameStr) + " is not in any of the country arrays.")




# defining the country-finder function
def whichContStr(nameStr):
    # making the arrays of country names
    europeArr = ["Belgium",
             "Czech Rep.",
             "France",
             "Germany",
             "Italy",
             "Netherlands",
             "Poland",
             "Portugal",
             "Romania",
             "Spain",
             "Sweden",
             "United Kingdom",
             "Norway",
             "Ukraine"
              ]
    mEastArr =   ["Turkey",
              "Algeria",
              "Egypt",
              "Iran",
              "Kuwait",
              "Saudi Arabia",
              "United Arab Emirates"
              ]
    asiaArr =    ["Kazakhstan",
              "Russia",
              "Uzbekistan",
              "China",
              "India",
              "Indonesia",
              "Japan",
              "Malaysia",
              "South Korea",
              "Taiwan",
              "Thailand",
              "Australia",
              "New Zealand"
              ]
    nAmerArr =   ["Canada",
              "United States",
              "Mexico"
              ]
    sAmerArr =   ["Argentina",
              "Brazil",
              "Chile",
              "Colombia",
              "Venezuela"
               ]
    africaArr =   ["Nigeria",
               "South Africa"
               ]
    
    if nameStr in europeArr:
        return "Europe"
    elif nameStr in mEastArr:
        return "Middle East"
    elif nameStr in asiaArr:
        return "Asia"
    elif nameStr in nAmerArr:
        return "North America"
    elif nameStr in sAmerArr:
        return "South America"
    elif nameStr in africaArr:
        return "Africa"
    else:
        print("The country " + str(nameStr) + " is not in any of the country arrays.")





# the first plot

# loading EnergyConsumers.txt into Consumers
with open("EnergyConsumers.txt", "r") as csmrFile:
    Consumers = csmrFile.readlines()
    
    
    # making Consumers 2-dimensional
    for i in range(len(Consumers)):
        # splitting by tabs
        Consumers[i] = Consumers[i].split("\t")
    
    
    # removing the first 3 lines for simplicity's sake
    Consumers = Consumers[3:]
    
    
    # creating an array of country names
    cntryArr = []
    for i in range(len(Consumers)):
        cntryArr.append( Consumers[i][0] )
    
    
    # converting to float values and removing the country name elements
    # creating the array to be used by the histogram
    histArr = []
    for i in range(len(Consumers)):
        # removing the country name element
        Consumers[i] = Consumers[i][1:]
        
        # converting to float values and appending to histArr
        for j in range(len(Consumers[i])):
            Consumers[i][j] = float( Consumers[i][j] )
        
        histArr.append(Consumers[i])
    

        
# plotting the histograms for each country
binArr = np.linspace(0, 3250, 15)

fig1 = plt.figure(1)
plt.hist(histArr, bins = binArr, edgecolor = "green")
plt.title("Energy Consumption of Countries (1990 - 2016)")
plt.xlabel("Energy consumption of a year (MTOE)")
plt.ylabel("Number of years")

# saving the figure
plt.savefig("figure_1.png")











# the second plot

# reading in EnergyRawDataFinal.txt
with open("EnergyRawDataFinal.txt", "r") as file:
          EnergyType = file.readlines()
          
          
          
          # removing the first line
          EnergyType = EnergyType[1:]
          
          # numInstances is the number data groupings
          numInstances = int( len(EnergyType) / 2 )
          
          sumElecArr = [0 for i in range(26)]
          sumNatGasArr = [0 for i in range(26)]
          
          for i in range(len(EnergyType)):
              
              currYear = int( EnergyType[i].split(",")[3] )
              currIdx = currYear - 1990
              
              # if the line is for electricity
              if EnergyType[i].split(",")[2] == "Electricity":
                  # adding to the appropriate electricity element
                  sumElecArr[currIdx]   += float( EnergyType[i].split(",")[1] )
                  
                  
                  # if the line is for natural gas
              elif EnergyType[i].split(",")[2] == "Natural Gas":
                  # adding to the appropriate electricity element
                  sumNatGasArr[currIdx] +=  float( EnergyType[i].split(",")[1] )



# plotting the two bar graphs

fig2 = plt.figure(2)

xArr = np.arange(len(sumElecArr))
barWidth = 0.5

fig2 = plt.figure(2)
lAxPlot = fig2.add_subplot(1, 1, 1)

# getting those labels
plt.xticks(xArr, [str(i) for i in range(1990, 2016)], rotation = "vertical")

lAxPlot.bar(xArr - barWidth / 2, sumElecArr, barWidth, color = "orange" , label = "Electricity")
lAxPlot.set_ylabel("Electricity")
lAxPlot.set_xlabel("Year")


rAxPlot = lAxPlot.twinx()

rAxPlot.bar(xArr + barWidth / 2, sumNatGasArr, barWidth, color = "green", label = "Natural gas")
rAxPlot.set_ylabel("Natural Gas (bil. cubic meters)")


lAxPlot.legend(loc = "upper left")
rAxPlot.legend(loc = "lower left")



plt.title("Sum of Elec. and Sum of Natural Gas Consump. of Select Countries (1990 - 2015)")




# saving the figure
plt.savefig("figure_2.png", bbox_inches='tight')







# the third plot
# editing Consumers to display industrial usage
Ind = Consumers[:]
# ALSO: preemptively making the residential consumer histogram array for the fifth plot
rchArr = Consumers[:]

# iterating through the outer array
for i in range( len(Ind) ):
    
    # iterating through the inner array
    for j in range( len(Ind[i]) ):
        # checking the year
        currYear = 1990 + j
        
        if currYear < 2000:
            Ind[i][j] *= 0.15
            rchArr[i][j] *= 0.85
            
        else:
            Ind[i][j] *= 0.35
            rchArr[i][j] *= 0.65


# storing stuff into their appropriate arrays

til_1999Arr = []
after1999Arr = []

for i in range( len( Ind ) ):
    for j in range( len (Ind[i] ) ):
        
        if j <= 9:
            til_1999Arr.append( Ind[i][j] )
            
        else:
            after1999Arr.append( Ind[i][j] )

# plotting the third plot

binArr = np.linspace(0, 800, 15)

fig3 = plt.figure(3)

plt.hist(after1999Arr, bins = binArr, color = "blue", histtype = "step", label = "2000 - 2016" )
plt.hist(til_1999Arr, bins = binArr, color = "red", histtype = "step",  label = "1990 - 1999" )

plt.legend(loc = "best")
plt.ylabel("Number of years")
plt.xlabel("Energy consumption of a year (MTOE)")

plt.title("Industrial Usage of Energy (1990 - 2016)")

# saving the plot
plt.savefig("figure_3.png")








# the fourth plot

# finding the index of china in Consumers
cIdx = cntryArr.index("China")
chinaArr = Consumers[cIdx]


# plotting the histogram

binArr = np.linspace(0, 750, 10)
fig4 = plt.figure(4)
plt.hist(chinaArr, bins = binArr, edgecolor = "black", color = "orange")
plt.title("Consumption of Energy in China (1990 - 2016)")
plt.xlabel("Energy consumption of a year (MTOE)")
plt.ylabel("Number of years")


# saving it as a figure
plt.savefig("figure_4.png")







# the fifth plot


# making Continent, an array of residential consumer data according to continent
Continent = [ [], [], [], [], [], [] ]
for i in range(len(Consumers)):
    
    Continent[ whichCont( cntryArr[i] ) ].append(rchArr[i])


# the residential consumer data is stored in rchArr

# plotting all the rchArr data, including Australia and New Zealand

binArr = np.linspace(0, 750, 100)

fig5 = plt.figure(5)

plt.hist( Continent[0], bins = binArr, histtype = "step", edgecolor = "blue", label = "Europe" )
plt.hist( Continent[1], bins = binArr, histtype = "step", edgecolor = "black", label = "Middle East" )
plt.hist( Continent[2], bins = binArr, histtype = "step", edgecolor = "red", label = "Asia"  )
plt.hist( Continent[3], bins = binArr, histtype = "step", edgecolor = "orange", label = "North America"  )
plt.hist( Continent[4], bins = binArr, histtype = "step", edgecolor = "purple", label = "South America"  )
plt.hist( Continent[5], bins = binArr, histtype = "step", edgecolor = "green" , label = "Africa" )
plt.title("Residential Consump. of Energy According to Region (1990 - 2016)")
plt.xlabel("Consumption of energy in year (MTOE)")
plt.ylabel("Number of years")
plt.legend(loc = "best")

plt.savefig("figure_5.png")








# the sixth plot

# loading CarbonEmissions.txt into CarbonEmissions
with open("CarbonEmissions.txt", "r") as file:
    CarbonEmissions = file.readlines()
    
    # removing the first line
    CarbonEmissions = CarbonEmissions[1:]
    
    
    # creating a simple array of only carbon emission values
    carbonBarArr = []
    for i in range(len(CarbonEmissions)):
        carbonBarArr.append( float( CarbonEmissions[i].split("\t")[2] ) )
    
    
    # creating an array of only the names of the countries in CarbonEmissions
    ceNameArr = []
    for i in range(len( CarbonEmissions )):
        ceNameArr.append( CarbonEmissions[i].split("\t")[1] )
    
    
    # creating a simple array of Consumer data of year 2015 of the countries found in Carbon Emissions
    consumBarArr = []
    for i in range( len( ceNameArr ) ):
        consumerIdx = cntryArr.index( ceNameArr[i] )
        
        consumBarArr.append( Consumers[consumerIdx][25] )

# plotting

xArr = np.arange(len(ceNameArr)) 
barWidth = 0.5

fig6 = plt.figure(6)
lAxPlot = fig6.add_subplot(1, 1, 1)

# getting those labels
plt.xticks(xArr, ceNameArr, rotation = "vertical")

lAxPlot.bar(xArr - barWidth / 2, carbonBarArr, barWidth, color = "orange" , label = "Carbon Emissions")
lAxPlot.set_ylabel("Carbon Emissions (mil. metric tons)")
lAxPlot.set_xlabel("Country")

rAxPlot = lAxPlot.twinx()

rAxPlot.bar(xArr + barWidth / 2, consumBarArr, barWidth,  label = "Energy Consumption")
rAxPlot.set_ylabel("Energy Consumption (MTOE)")

plt.title("Emiss. & Energy Consump. of Select Countries (2015)")
rAxPlot.legend(loc = "upper left")
lAxPlot.legend(loc = "best")

# saving the plot
plt.savefig("figure_6.png", bbox_inches='tight')






# finding the top three countries consuming the mot energy from Consumers


sumConsumArr = [sum(i) for i in Consumers]

maxConsumer1Idx = sumConsumArr.index( max(sumConsumArr) )
maxConsumer1 = cntryArr[ maxConsumer1Idx ]

# setting the ultimate maximum to 0 so we can search with max() again
sumConsumArr[maxConsumer1Idx] = 0
maxConsumer2Idx = sumConsumArr.index( max(sumConsumArr) )
maxConsumer2 = cntryArr[ maxConsumer2Idx ]

# setting the second maximum to 0 so we can search with max() again
sumConsumArr[maxConsumer2Idx] = 0
maxConsumer3Idx = sumConsumArr.index( max(sumConsumArr) )
maxConsumer3 = cntryArr[ maxConsumer3Idx ]

# getting the continents
cont1 = whichContStr( maxConsumer1 )
cont2 = whichContStr( maxConsumer2 )
cont3 = whichContStr( maxConsumer3 )


# output

print(str(maxConsumer1) + " is the number 1 energy consumer and is in " + str(cont1) + ".")
print(str(maxConsumer2) + " is the number 2 energy consumer and is in " + str(cont2) + ".")
print(str(maxConsumer3) + " is the number 3 energy consumer and is in " + str(cont3) + ".")
