import serial
from time import sleep

port = "/dev/serial0"  # Raspberry Pi 3

def parseGPS(data):
   # print("raw:", data)
    data = data.decode() 
    if "GPGGA" in data:
        s = data.split(",")
        if s[7] == '0':
            print("no satellite data available")
            return        
        time = s[1][0:2] + ":" + s[1][2:4] + ":" + s[1][4:6]
        lat = decode(s[2])
        dirLat = s[3]
        lon = decode(s[4])
        dirLon = s[5]
        alt = s[9] + " m"
        sat = s[7] 
       # print("Time(UTC): %s-- Latitude: %s(%s)-- Longitude:%s(%s) -- Altitute:%s--(%s satellites)" %(time, lat, dirLat, lon, dirLon, alt, sat) )
        
        return (decode_normal(s[4]), decode_normal(s[2]))
    else:
       #print(data)
       pass

def decode(coord):
    # DDDMM.MMMMM -> DD deg MM.MMMMM min
    v = coord.split(".")
    head = v[0]
    tail =  v[1]
    deg = head[0:-2]
    min = head[-2:]
    return deg + " deg " + min + "." + tail + " min"
    
def decode_normal(coord):
    # DDDMM.MMMMM -> DD deg MM.MMMMM min
    dot_location = coord.find(".")
    dot_removed = coord.replace(".", "")
    
    word_listed = list(dot_removed)
    word_listed.insert(dot_location-2, ".")
    
    new_word = "".join(word_listed)
    
    return float(new_word)

ser = serial.Serial(port, baudrate = 9600, timeout = 0.5)


def get_gps_data():

    while True:


        try:
            
            with serial.Serial(port, baudrate = 9600, timeout = 0.5) as ser:
                data = ser.readline()
                gps_data = parseGPS(data)
                
                if gps_data:
                    print("REAL DATA : ", gps_data)
                    return gps_data
            
        except Exception as e:
            
            print(e)
            
        #sleep(1)
    
        
#get_gps_data()