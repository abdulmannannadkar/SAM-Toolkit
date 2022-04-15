# Project's main screen
#!/usr/bin/env python
from time import sleep
import signal
import os

def progress(percent=0, width=30):
    # The number of hashes to show is based on the percent passed in. The
    # number of blanks is whatever space is left after.
    hashes = width * percent // 100
    blanks = width - hashes

    print('\r[', hashes*'#', blanks*' ', ']', f' {percent:.0f}%', sep='',
        end='', flush=True)

print("Wellcome! We are making the tool ready for you...")
print('This will take a moment')

for i in range(101):
    progress(i)
    sleep(0.03) # sleep(0.1) default

# Newline so command prompt isn't on the same line
print()

banner1 = """

#                                                                                     
#                                                                                     
#     SSSSSSSSSSSSSSS                AAA               MMMMMMMM               MMMMMMMM
#   SS:::::::::::::::S              A:::A              M:::::::M             M:::::::M
#  S:::::SSSSSS::::::S             A:::::A             M::::::::M           M::::::::M
#  S:::::S     SSSSSSS            A:::::::A            M:::::::::M         M:::::::::M
#  S:::::S                       A:::::::::A           M::::::::::M       M::::::::::M
#  S:::::S                      A:::::A:::::A          M:::::::::::M     M:::::::::::M
#   S::::SSSS                  A:::::A A:::::A         M:::::::M::::M   M::::M:::::::M
#    SS::::::SSSSS            A:::::A   A:::::A        M::::::M M::::M M::::M M::::::M
#      SSS::::::::SS         A:::::A     A:::::A       M::::::M  M::::M::::M  M::::::M
#         SSSSSS::::S       A:::::AAAAAAAAA:::::A      M::::::M   M:::::::M   M::::::M
#              S:::::S     A:::::::::::::::::::::A     M::::::M    M:::::M    M::::::M
#              S:::::S    A:::::AAAAAAAAAAAAA:::::A    M::::::M     MMMMM     M::::::M
#  SSSSSSS     S:::::S   A:::::A             A:::::A   M::::::M               M::::::M
#  S::::::SSSSSS:::::S  A:::::A               A:::::A  M::::::M               M::::::M
#  S:::::::::::::::SS  A:::::A                 A:::::A M::::::M               M::::::M
#   SSSSSSSSSSSSSSS   AAAAAAA                   AAAAAAAMMMMMMMM               MMMMMMMM
#                                                                                     
                                                                                .... A Security And Monitoring Toolkit
                                                                                     Developed by @Abdul_Mannan_Nadkar
"""

banner = """

   ███████╗ █████╗ ███╗   ███╗ TM
   ██╔════╝██╔══██╗████╗ ████║
   ███████╗███████║██╔████╔██║
   ╚════██║██╔══██║██║╚██╔╝██║
   ███████║██║  ██║██║ ╚═╝ ██║
   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝
                              .... A Security And Monitoring Toolkit
                                   Developed by @Abdul_Mannan_Nadkar

"""
welcome = """
--------------------------WELCOME!-----------------------
Before moving further let's get connected with each other.
---------------------------------------------------------
"""

services = """
> Which section do you like to move on?
> 1} Security
> 2} Monitoring
"""
security_banner = """

"""

monitoring_banner = """
~ Here are some services which you can use : 
> 1 } System Process Monitor
> 2 } Server Process Monitor
> 3 } Keylogger
> 4 } Go back 

"""

print(banner1)
#print(banner)
print(welcome)

def monitor_tools(script_name):
    paths = {
        'process_monitor':"Tools(Monitoring)/Process-monitoring/proc_monitor.py",
        'server_monitor':"Tools(Monitoring)/Server-Monitoring-Script/monitor.py",
        'keylogger':"Tools(Monitoring)/keylogger/SAM-keylogger/keylogger.py"
    }
    script_name = script_name
    os.system('start python {}'.format(str(paths[script_name])))



def user_data():
    user_data.name = str(input("What's ur name? : "))
    os.system('cls')


def service_selection():
    while 1==1:
        print(banner)
        print('Welcome {}!'.format(str(user_data.name)))
        print(services)
        inp = str(input(" --> "))
        if inp == 'monitor' or inp == 'monitoring' or inp == '2':
            os.system('cls')
            while 1==1:
                print(banner)
                print(monitoring_banner)
                inp_data = str(input("> Which tool do you wanna use : "))
                if "system" in inp_data or '1' in inp_data:
                    monitor_tools('process_monitor')
                    os.system('cls')
                elif "server" in inp_data or '2' in inp_data:
                    monitor_tools('server_monitor')
                    os.system('cls')
                elif "keylogger" in inp_data or '3' in inp_data:
                    monitor_tools('keylogger')
                    os.system('cls')
                elif "back" in inp_data or '4' in inp_data:
                    os.system('cls')
                    service_selection()
                else:
                    print("Couldn't understand ")
                    inp1 = input("Do you wanna quit? (Y/N) : ")
                    if inp1 == "no" or inp1 == "n":
                        service_selection()
                    else:
                        exit()
        elif inp == 'security' or inp == '1':
            print("do some tasks")
        else:
            print("Couldn't understand ")
            inp1 = input("Do you wanna quit? (Y/N) : ")
            if inp1 == "no" or inp1 == "n":
                service_selection()
            else:
                exit()



user_data()
service_selection()