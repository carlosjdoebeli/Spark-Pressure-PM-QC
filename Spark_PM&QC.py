import serial
import serial.tools.list_ports
import time
import datetime
import sys
import matplotlib.pyplot as plt
# import matplotlib.animation as animation
# from matplotlib import style

# find COM port for arduino
ports = list(serial.tools.list_ports.grep("arduino"))

readings = []
dataList = []
x_data = []
y_data = []
minimum_pressure = 25
maximum_pressure = 35

if len(ports) == 1:
    print("Arduino found")
else:
    print("Arduino not found or too many of them")
    print("Check Arduino connection and whether drivers are installed")
    print("Check your connection!")
    time.sleep(10)
    sys.exit()

# connect to com port

arduinoPort = ports[0]
ser = serial.Serial(arduinoPort[0], timeout = 0.1, baudrate = 250000)


# print ("connected to arduino")
name = input("Please enter file name: ")

#time.sleep(2)
# get time and date for naming file
time_now = datetime.datetime.now()
time_str = str(time_now)
#mod: added "pressure data" to file name
time_str = str(name) + " " + time_str.replace(":","-") + ".txt"
exited = False


# create text file to write data, w = write
with open(time_str, 'w') as fname:
    #fname.write("#Connected Arduinos"+"\n")

    #header1 = "#TimeStamp, Time(microseconds), Pressure (counts)"

    # for port in ports:
        # fname.write("#" + port[0]+"\n")
        #cd mod: ",VOLTAGE_"+port[0]
        #later have a function that changes voltage
        #header1 += ",VOLTAGE_"+port[0]

    # fname.write("\n")
    #fname.write(header1+"\n")
	fname.write(time_str+"\n")

ser.close()

# print ("Data saved to textfile: " +time_str)
# instructions for using program
# print ("Press Ctrl-C to stop collection and close program ")
input = ("Press Enter to start collection")
print("\n")
print("_____________________________________________________________________________")
print("\n")
print("WHEN LIGHTS TURN GREEN, PRESS RUN BUTTON ON THE INSTRUMENT")
print("(This window will close when readings are complete)")

#Open the serial port again to trigger a reset on the arduino
ser = serial.Serial(arduinoPort[0], timeout = 0.1, baudrate = 250000)
# loop for displaying temperature and writing to text file

with open(time_str, 'a') as fname :
    while (exited==False):
        try:

            data = "" #str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            #data += ", "

            try:
                serialExceptionOccured = False
                areading = bytes.decode(ser.readline())
                if len(areading) > 1:
                    dataList.append(areading)

                if "Complete" in areading:
                    time.sleep(2)
                    exited = True;

                if len(areading) <= 1:
                    serialExceptionOccured = True

            except serial.SerialTimeoutException:
                serialExceptionOccured = True

            if not serialExceptionOccured:
                # data += ","
                data += areading
                fname.write (data)
                # print (data)

            # print (data)


        except (KeyboardInterrupt, SystemExit):
            if ser.closed==False:
                ser.close()
                exited=True
            else:
                exited=True

# we do our plotting here
a = 0
for line in dataList:
    a = a+1
    # print(line)
    if(a < 5):
        continue
    else:
        if "," not in line:
            continue
        else:
            x, y = line.split(',')
            x_data.append(float(x))
            y_data.append(float(y))
            plt.ylabel("Pressure (PSI)")
            plt.xlabel("Time (ms)")
            plt.title(dataList[1])
            plt.plot(x_data, y_data, 'k')

# The following lines determine a maximum and minimum pressure for pass/fail tests
plt.axhline(y=minimum_pressure, linewidth=0.5, linestyle = ':', color = 'r')
plt.axhline(y=maximum_pressure, linewidth = 0.5, linestyle = ':', color = 'r')
plt.savefig(str(name) + ".png")
plt.show()




print("done")


"""THE END!!!"""
