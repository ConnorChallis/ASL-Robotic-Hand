from __future__ import division
import time
import sign_positions
import logging
import math
import Adafruit_PCA9685


pwm = Adafruit_PCA9685.PCA9685()
#
# # Configure min and max servo pulse lengths for fingers
# #higher number = closed grip
# pos_close_thumb = 550
# pos_open_thumb = 300
# pos_close_pointer = 210
# pos_open_pointer = 450
# pos_close_middle = 600
# pos_open_middle = 295
# pos_close_ring = 580 #needs to be physically loosened
# pos_open_ring = 305 #needs to be physically loosened
# pos_close_pinky = 570
# pos_open_pinky = 310
#
# pos_right_wrist = 600
# pos_left_wrist = 150
#
# #Define the pins for different fingers
# pin_thumb = 4
# pin_pointer = 1
# pin_middle = 2
# pin_ring = 3
# pin_pinky = 5
# pin_wrist = 0
#
# # pause time inbetween signs in routine
routine_pause = 4.0
#
# #List of currently available signs and routines
signs = ['rock_on','f_you','fist','hang_loose','relax','love','1','2','3','4','5','6','7','8','9','quit']
shows = ['cycle_all','numbers','random']
#
# #Helper function to make setting a servo pulse width simpler.
# def set_servo_pulse(channel, pulse):
#     pulse_length = 1000000    # 1,000,000 us per second
#     pulse_length //= 60       # 60 Hz
#     print('{0}us per period'.format(pulse_length))
#     pulse_length //= 4096     # 12 bits of resolution
#     print('{0}us per bit'.format(pulse_length))
#     pulse *= 1000
#     pulse //= pulse_length
#     pwm.set_pwm(channel, 0, pulse)
#
# pwm.set_pwm_freq(60)

toggle = True
active = True
help = False
while active == True:
    command = raw_input("\nInput desired hand movement here: (type 'help' for help or 'settings') \n")
    if command == 'quit':
        active = False
    if command == 'settings':
        print ("To toggle printing current state, type 'enable' or 'disable'")
        toggle = raw_input()
        if toggle == 'enable':
            toggle = True
        else:
            toggle = False
        print ("\nValue of printing current state: " + str(toggle))
    elif command == 'help':
        help = True
        while help == True:
            print ("\nWelcome to help menu:\ntype 'signs' for available signs\ntype 'shows' for available routines")
            help_type = raw_input()
            if help_type == 'signs':
                print ('\nList of available signs:')
                print('____________________________')
                for sign in signs:
                    print (sign)
                    help = False
            elif help_type == 'shows':
                print ('\nList of available shows:')
                print('____________________________')
                for show in shows:
                    print (show)
                    help = False
            else:
                print (str(help_type) + ' was not a recognised command!')
                help = False
    elif command == 'rock_on':
        if toggle == True:
            print ("Rock on!")
        sign_positions.rock_on()

    elif command == 'relax':
        if toggle == True:
            print ("Relax")
        sign_positions.relax()

    elif command == 'f_you':
        if toggle == True:
            print ("Middle finger justice!")
        sign_positions.f_you()

    elif command == 'fist':
        if toggle == True:
            print ("Making Fist")
        sign_positions.fist()

    elif command == 'hang_loose':
        if toggle == True:
            print ("Hang loose")
        sign_positions.hang_loose()

    elif command == 'love':
        if toggle == True:
            print ("signing I Love You")
        sign_positions.love()

    elif command == 'sign_1':
        if toggle == True:
            print ("Sign language number 1")
        sign_positions.sign_1()


    elif command == 'sign_2':
        if toggle == True:
            print ("Sign language number 2")
        sign_positions.sign_2()

    elif command == 'sign_3':
        if toggle == True:
            print ("Sign language number 3")
        sign_positions.sign_3()

    elif command == 'sign_4':
        if toggle == True:
            print ("Sign language number 4")
        sign_positions.sign_4()

    elif command == 'sign_5':
        if toggle == True:
            print ("Sign language number 5")
        sign_positions.sign_5()

    elif command == 'sign_6':
        if toggle == True:
            print ("Sign language number 6")
            sign_positions.sign_6()

    elif command == 'sign_7':
        if toggle == True:
            print ("Sign language number 7")
        sign_positions.sign_7()

    elif command == 'sign_8':
        if toggle == True:
            print ("Sign language number 8")
        sign_positions.sign_8()

    elif command == 'sign_9':
        if toggle == True:
            print ("Sign language number 9")
        sign_positions.sign_9()

    elif command == 'numbers':
        show = True
        while show == True:
            print ("Running numbers routine")

            if toggle == True:
                print ("Sign language number 1")
            sign_positions.sign_1()
            time.sleep(routine_pause)
            if toggle == True:
                print ("Sign language number 2")
            sign_positions.sign_2()
            time.sleep(routine_pause)
            if toggle == True:
                print ("Sign language number 3")
            sign_positions.sign_3()
            time.sleep(routine_pause)
            if toggle == True:
                print ("Sign language number 4")
            sign_positions.sign_4()
            time.sleep(routine_pause)
            if toggle == True:
                print ("Sign language number 5")
            sign_positions.sign_5()
            time.sleep(routine_pause)
            if toggle == True:
                print ("Sign language number 6")
            sign_positions.sign_6()
            time.sleep(routine_pause)
            if toggle == True:
                print ("Sign language number 7")
            sign_positions.sign_7()
            time.sleep(routine_pause)
            if toggle == True:
                print ("Sign language number 8")
            sign_positions.sign_8()
            time.sleep(routine_pause)
            if toggle == True:
                print ("Sign language number 9")
            sign_positions.sign_9()
            time.sleep(routine_pause)

    elif command == 'cycle_all':
        show = True
        while show == True:
            if toggle == True:
                print ("Sign language number 1")
            sign_positions.sign_1()
            time.sleep(routine_pause)
            if toggle == True:
                print ("Sign language number 2")
            sign_positions.sign_2()
            time.sleep(routine_pause)
            if toggle == True:
                print ("Sign language number 3")
            sign_positions.sign_3()
            time.sleep(routine_pause)
            if toggle == True:
                print ("Sign language number 4")
            sign_positions.sign_4()
            time.sleep(routine_pause)
            if toggle == True:
                print ("Sign language number 5")
            sign_positions.sign_5()
            time.sleep(routine_pause)
            if toggle == True:
                print ("Sign language number 6")
            sign_positions.sign_6()
            time.sleep(routine_pause)
            if toggle == True:
                print ("Sign language number 7")
            sign_positions.sign_7()
            time.sleep(routine_pause)
            if toggle == True:
                print ("Sign language number 8")
            sign_positions.sign_8()
            time.sleep(routine_pause)
            if toggle == True:
                print ("Sign language number 9")
            sign_positions.sign_9()
            time.sleep(routine_pause)
            if toggle == True:
                print ("Rock on!!")
            sign_positions.rock_on()
            time.sleep(routine_pause)
            if toggle == True:
                print ("Fist")
            sign_positions.fist()
            time.sleep(routine_pause)
            if toggle == True:
                print ("Hang Loose man!")
            sign_positions.hang_loose()
            time.sleep(routine_pause)
            if toggle == True:
                print ("Sign language for I Love You")
            sign_positions.love()
            time.sleep(routine_pause)

    else:
        print (str(command) + " not a known command. Type 'help' for help")
print ("End of program, Thanks for signing!")
