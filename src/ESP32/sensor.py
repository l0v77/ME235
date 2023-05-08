from machine import Pin, time_pulse_us
import machine
import time
import socket
import network
from time import sleep


# Replace these with your Wi-Fi credentials
WIFI_SSID = 'msi'
WIFI_PASSWORD = '88888888'

# UDP server IP and port
SERVER_IP = '10.142.87.193'
SERVER_PORT = 5432

# Connect to Wi-Fi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(WIFI_SSID, WIFI_PASSWORD)

while not wlan.isconnected():
    print("Connecting to Wi-Fi...")
    sleep(1)

print("Connected to Wi-Fi")

# Create UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Pin definitions
TRIG_PIN1 = 13
ECHO_PIN1 = 39
TRIG_PIN2 = 12
ECHO_PIN2 = 34

# Set trigger pins as outputs
trigger1 = Pin(TRIG_PIN1, Pin.OUT)
trigger2 = Pin(TRIG_PIN2, Pin.OUT)

# Set echo pins as inputs
echo1 = Pin(ECHO_PIN1, Pin.IN)
echo2 = Pin(ECHO_PIN2, Pin.IN)

while True:
    # Send first ultrasonic pulse
    trigger1.off()
    time.sleep_us(2)
    trigger1.on()
    time.sleep_us(10)
    trigger1.off()
    pulse_duration1 = time_pulse_us(echo1, 1)
    distance1 = (pulse_duration1 / 2) / 29.1  # Distance in centimeters

    # Send second ultrasonic pulse
    trigger2.off()
    time.sleep_us(2)
    trigger2.on()
    time.sleep_us(10)
    trigger2.off()
    pulse_duration2 = time_pulse_us(echo2, 1)
    distance2 = (pulse_duration2 / 2) / 29.1  # Distance in centimeters
          
    
    
    message = str(distance1) +" " + str(distance2)
#     message = str(distance2)
    sock.sendto(message.encode(), (SERVER_IP, SERVER_PORT))
    print("Sent:", message)
    time.sleep_ms(400) 
    
    

sock.close()


