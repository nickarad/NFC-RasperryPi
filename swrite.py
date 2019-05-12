import RPi.GPIO as GPIO
import SimpleMFRC522

#-------setting up led-------

#----------------------------


reader = SimpleMFRC522.SimpleMFRC522()

try:
        #Last Name
        text='Last Name:'
        text+= raw_input('Last Name: ')
        text+='\n'
        #First Name
        text+='First Name:'
        text+=raw_input('First Name: ')
        text+='\n'
        #AMKA
        text+='AMKA:'
        text+=raw_input('AMKA: ')
        text+='\n'
        #Blood Type
        text+='Blood Type:'
        text+=raw_input('Blood Type: ')
        text+='\n'



        print("Now place your tag to write")
        reader.write(text)
        print("Written")

finally:
        GPIO.cleanup()


