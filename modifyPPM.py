#Python ver 2.7.10
#___________________________________________________________________________________________________________________________________________________________________________________
# Vamsy Jasti
# CS 524-02
# Oct 14 2016
#____________________________________________________________________________________________________________________________________________________________________________________
# Python program to manipulate an image in PPM format
# This programs takes a ppm image as an input and applies the filters the user desires and creates an output file with the desired filters, NOTE: the input file remains unchanged
#____________________________________________________________________________________________________________________________________________________________________________________


# This function defines the Extreme contrast filter
def extremecontrast():
# We iterate row by row and columns by columns (3 columns at a time) in each row
    for rowg in range(row):
        for colg in range(0, totalcolumns, 3):
#We check if the Red/Green/Blue value is greater than half the maximum colour. If it is we change the value as 0 else we change the value as maximum colour. We check the values of R, G & B at once.
            if int(finalar[rowg][colg])<int(mediancol):
                finalar[rowg][colg]=str(0)
            elif int(finalar[rowg][colg]) >int(mediancol):
                finalar[rowg][colg]=str(maxcol)

            if int(finalar[rowg][colg+1]) < int(mediancol):
                finalar[rowg][colg+1] = str(0)
            elif int(finalar[rowg][colg+1]) > int(mediancol):
                finalar[rowg][colg+1] = str(maxcol)

            if int(finalar[rowg][colg+2]) < int(mediancol):
                finalar[rowg][colg+2] = str(0)
            elif int(finalar[rowg][colg+2]) > int(mediancol):
                finalar[rowg][colg+2] = str(maxcol)
    return finalar


def horizontalflip():
#We iterate row by row and initialize count and temp as 0 at each iteration
    for rowg in range(0,row):
        count=0
        temp=0
#we iterate column by column till half number of columns because the other half would have already been flipped by the time we complete half
#We then swap each of R, G & B with the correspinding R, G, B values on the other half. If we have 6 columns we swap (1,6), (2,5), (3,4)
        for colg in range(0, halfcolumns,3):
            temp=finalar[rowg][colg]
            colalternate=int((totalcolumns-count)-3)
            finalar[rowg][colg]=finalar[rowg][colalternate]
            finalar[rowg][colalternate]=temp

            temp = finalar[rowg][colg+1]
            colalternate = int((totalcolumns - count) - 2)
            finalar[rowg][colg+1] = finalar[rowg][colalternate]
            finalar[rowg][colalternate] = temp

            temp = finalar[rowg][colg+2]
            colalternate = int((totalcolumns - count) - 1)
            finalar[rowg][colg+2] = finalar[rowg][colalternate]
            finalar[rowg][colalternate] = temp
            count=count+3
    return finalar


def colourinversion(maxcol):
# We iterate row by row and in each row we iterate column by column, If the value is 0 we make it 255 and if it is 255 we make it 0 else we make it Maximum colour-value
    for rowg in range(row):
        for colg in range(0, totalcolumns):
            if int(finalar[rowg][colg]) == 0:
                finalar[rowg][colg] = str(255)
            elif int(finalar[rowg][colg]) == 255:
                finalar[rowg][colg] = str(0)
            elif int(finalar[rowg][colg]) != 0 and int(finalar[rowg][colg]) != 255:
                finalar[rowg][colg] = str(int(maxcol) - int(finalar[rowg][colg]))
    return finalar


def greyscale():
# We iterate row by row and in each row we iterate column by column and we increment each time by 3, We add the R,G,B values, get their averages and replace the the values of R, G, B with the avg
    for rowg in range(row):
        for colg in range(0,totalcolumns,3):
            totall=int(finalar[rowg][colg])+int(finalar[rowg][colg+1])+int(finalar[rowg][colg+2])
            avg = int(totall/3)
            finalar[rowg][colg]=str(avg)
            finalar[rowg][colg+1]=str(avg)
            finalar[rowg][colg+2]=str(avg)
        avg=0
        totall=0
    return finalar

def flattenred():
# We iterate row by row and in each row we iterate column by column and we increment each time by 3, and make the change the value of red pixel to 0
    for rowg in range(row):
        for colg in range(0, totalcolumns, 3):
            finalar[rowg][colg] = str(0)
    return finalar


def flattengreen():
# We iterate row by row and in each row we iterate column by column and we increment each time by 3, and make the change the value of green pixel to 0
    for rowg in range(row):
        for colg in range(0, totalcolumns, 3):
            finalar[rowg][colg+1] = str(0)
    return finalar


def flattenblue():
# We iterate row by row and in each row we iterate column by column and we increment each time by 3, and make the change the value of blue pixel to 0
    for rowg in range(row):
        for colg in range(0, totalcolumns, 3):
            finalar[rowg][colg+2] = str(0)
    return finalar



x = input("Please enter the name of Input file: ")
y = input("Please enter the name of Output file: ")
# We open the image with read permissions and prints error message if a file with the name given is not found
try:
    img= open(x,'r')
except IOError:
    print ("Could not open file! You have entered an invalid name!")
data=img.read()
#we get the data into a list splitd by splitting each term by a space
splitd=data.split()
#ver stores the version of the image(ex: P3)
ver=splitd[0]
#pixel stores the pixel value
pixel=int(splitd[1])
#totalcolumns stores the total no of columns in the file which is 3 times pixel
totalcolumns=pixel*3
halfcolumns=int(totalcolumns/2)
#row stores the no of rows in the file
row=int(splitd[2])
#maxcol stores the maximum colour value of the image
maxcol=int(splitd[3])
mediancol=int(maxcol/2)
#gets the list splitd from the position 4 and stores it in remaininglist
remaininglist=splitd[4:]
finalar=[]
#we now convert the 1d list to a 2d list for our convenience
#using the for loop we iterate row by row at once
for rowCount in range(int(row)):
#Rbegin stores the value of the index of the rows starting bit and rowend stores the value of the index of the rows ending bit
    Rbegin = rowCount * totalcolumns
    Rend = Rbegin + totalcolumns
#Using Rbegin & Rend we append each row row to a list finalar
    finalar.append( remaininglist[Rbegin : Rend] )
    #print (finalar)
update = input("Do you want to see the updated lists after every effect? y or n:")
if update == "y":
    print(finalar)
case1 = input("Do you want to perform greyscale conversion? y or n:")
if case1=="y":
    greyscale()
    if update=="y":
        print(finalar)
else:
    print("Not Selected")
case2 = input("Do you want to perform image colour inversion? y or n:")
if case2=="y":
    finalar = colourinversion(maxcol)
    if update == "y":
        print(finalar)
else:
    print("Not Selected")
case3 = input("Do you want to perform flatten red? y or n:")
if case3=="y":
    flattenred()
    if update == "y":
        print(finalar)
else:
    print("Not Selected")
case4 = input("Do you want to perform flatten green? y or n:")
if case4=="y":
    flattengreen()
    if update == "y":
        print(finalar)
else:
    print("Not Selected")
case5 = input("Do you want to perform flatten blue? y or n:")
if case5=="y":
    flattenblue()
    if update == "y":
        print(finalar)
else:
    print("Not Selected")
case6 = input("Do you want to perform horizontal flip? y or n:")
if case6=="y":
    horizontalflip()
    if update == "y":
        print(finalar)
else:
    print("Not Selected")
case7 = input("Do you want to perform extreme contrast? y or n:")
if case7=="y":
    print(finalar)
    extremecontrast()
    if update == "y":
        print(finalar)
else:
    print("Not Selected")

#we open a newfile with the name stored in y with write permissions
outputFile = open(y, 'w')
#we first add the version, pixel & row count, maximum colour value t the list
outputFile.write(ver+"\n" + str(pixel) + " " + str(row) +"\n"+ str(maxcol) + "\n")
#rowsLen & colsLen stores the number of rows and columns
rowsLen = len(finalar)
colsLen = len(finalar[0])
#we now iterate row by row and column by column by column in each row and writh the values to the outputfile
for row in range(rowsLen):
    for col in range(colsLen):
        outputFile.write(finalar[row][col] + " ")
        outputFile.write("\n")

print("the output file name is",y)

