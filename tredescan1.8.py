from __future__ import print_function
from datetime import datetime
from tabulate import tabulate
from queue import Queue
from colorama import Fore
from colorama import Style
from scapy.all import ARP, Ether, srp
from pytube import YouTube
import scapy.all as scapy
import sys
import sysconfig
import socket
import time
import threading
import platform
import psutil
import GPUtil
import requests
import json
import pyqrcode
import colorama
import os
import os
import platform
import re
import signal
import socket
import sys
import threading
import timeit
import xml.parsers.expat
import subprocess


#  except:
#       print('Failed to open URL. Unsupported variable type.')
#os.system("mode con cols=150 lines=50")    ridimenziona la finestra teoricamente
colorama.init()
privateIp = socket.gethostbyname(socket.gethostname())
hostname = socket.gethostname()

user_list = psutil.users()
for user in user_list:
    username = user.name
print("")


target = (privateIp)
t_IP = socket.gethostbyname(target)

print("")

print(Fore.GREEN + """

████████╗██████╗ ███████╗██████╗ ███████╗███████╗ ██████╗ █████╗ ███╗   ██╗
╚══██╔══╝██╔══██╗██╔════╝██╔══██╗██╔════╝██╔════╝██╔════╝██╔══██╗████╗  ██║
   ██║   ██████╔╝█████╗  ██║  ██║█████╗  ███████╗██║     ███████║██╔██╗ ██║
   ██║   ██╔══██╗██╔══╝  ██║  ██║██╔══╝  ╚════██║██║     ██╔══██║██║╚██╗██║
   ██║   ██║  ██║███████╗██████╔╝███████╗███████║╚██████╗██║  ██║██║ ╚████║
   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═════╝ ╚══════╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝


""" + Style.RESET_ALL)
print(Fore.YELLOW + """\nPlease enter the type of scan you want to run:
                                                    *******************************************************
            [1] Port Scanner                         Current system user are:     >>>""" , username, """ 
            [2] Network scanner (automatic)          Your Computer Name is:       >>>""" , hostname, """ 
            [2.2] Alternative scanner                My subnet IP:                >>>""" , privateIp, """
            [2.3] Manual scanner                     
            [3] Sys info                             *******************************************************
            [4] Hardware info                        
            [5] Ip localizer                        [97] Print the available cmd commands
            [6] Make QR Code                        [98] Print this help screen
            [7] Process viewer and killer           [99] exit
            [8] Youtube downloader
            [9] See saved WIFI password
            
            \n""" + Style.RESET_ALL)



print("")


ans = True
while ans:

    print(Fore.GREEN + """What would you like to do?
    """ + Style.RESET_ALL)

    ans = input()

    if ans == "ping":
        ip = input('ip to ping:  ')
        os.system('ping ' + ip)
    elif ans == "cmd":
        os.system('cmd')
    elif ans == "chkdsk":
        os.system('chkdsk')
    elif ans == "chkdsk":
        os.system('chkdsk')
    elif ans == "color 3":
        os.system('color 3')
    elif ans == "ipconfig":
        os.system('ipconfig')
    elif ans == "ipconfig /all":
        os.system('ipconfig /all')
    elif ans == "ipconfig /release":
        os.system('ipconfig /renew')
    elif ans == "shutdown /r":
        os.system('shutdown /r')
    elif ans == "exit":
        print("closing session...")
        time.sleep(1)
        break
    elif ans == "1":
        print("")
        socket.setdefaulttimeout(0.25)
        print_lock = threading.Lock()

        target = input('Enter the host to be scanned: ')
        t_IP = socket.gethostbyname(target)
        print('Starting scan on host: ', t_IP)


        def portscan(port):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            try:
                con = s.connect((t_IP, port))
                with print_lock:
                    print(port, 'is open')
                con.close()
            except:
                pass


        def threader():
            while True:
                worker = q.get()
                portscan(worker)
                q.task_done()


        q = Queue()
        startTime = time.time()

        for x in range(100):
            t = threading.Thread(target=threader)
            t.daemon = True
            t.start()

        for worker in range(1, 500):
            q.put(worker)

        q.join()
        print('Time taken:', time.time() - startTime)
        print("")

    # elif ans=="2":
    # print("")
    # print("Il mio indirizzo IP privato:", privateIp)
    # print("")

    # elif ans=="3":
    # print("")
    # print("Il mio indirizzo IP pubblico:", publicIp)
    # print("")

    # elif ans=="4":
    # print("")
    # print("Your Computer Name is:" + hostname)
    # print("")
    elif ans == "2":
        privateIpdiviso = privateIp.split('.')
        radicerete = (privateIpdiviso[0] + '.' + privateIpdiviso[1] + '.' + privateIpdiviso[2] + '.' + '1' + '/24')

        print("")
        print('your class: ' + radicerete)
        print("")

        request = scapy.ARP()

        request.pdst = radicerete
        broadcast = scapy.Ether()

        broadcast.dst = 'ff:ff:ff:ff:ff:ff'

        request_broadcast = broadcast / request
        clients = scapy.srp(request_broadcast, timeout=10, verbose=1)[0]

        for element in clients:
            input01 = (element[1].psrc).upper()

            # gets information
            output = socket.gethostbyaddr(str(input01))

            # processes the information to only get the hostname
            outputProceesed = str(output).split("'")[1::2]
            print(
                element[1].psrc + "	 " + element[1].hwsrc + "	 " + (f"Their Hostname is:  {outputProceesed[0]}\n"))


    elif ans == "2.2":
        # print("")
        # print("sys.platform                 ", sys.platform)
        # print("platform.system()            ", platform.system())
        # print("sysconfig.get_platform()     ", sysconfig.get_platform())
        # print("platform.machine()           ", platform.machine())
        # print("platform.architecture()      ", platform.architecture())
        # print("")

        target_ip = input('insert the class (ex 192.168.1.1/24) :')
        # IP Address for the destination
        # create ARP packet
        arp = ARP(pdst=target_ip)
        # create the Ether broadcast packet
        # ff:ff:ff:ff:ff:ff MAC address indicates broadcasting
        ether = Ether(dst="ff:ff:ff:ff:ff:ff")
        # stack them
        packet = ether / arp

        result = srp(packet, timeout=3, verbose=0)[0]

        # a list of clients, we will fill this in the upcoming loop
        clients = []

        for sent, received in result:
            # for each response, append ip and mac address to `clients` list

            clients.append({'ip': received.psrc, 'mac': received.hwsrc})

        # print clients
        print("Available devices in the network:")
        print("IP" + " " * 18 + "MAC")
        for client in clients:
            print("{:16}    {}".format(client['ip'], client['mac']))
        print("")
    elif ans == "2.3":
        request = scapy.ARP()

        request.pdst = input('insert the class (ex 192.168.1.1/24) :')
        broadcast = scapy.Ether()

        broadcast.dst = 'ff:ff:ff:ff:ff:ff'

        request_broadcast = broadcast / request
        clients = scapy.srp(request_broadcast, timeout=10, verbose=1)[0]

        for element in clients:
            input01 = (element[1].psrc).upper()

            # gets information
            output = socket.gethostbyaddr(str(input01))

            # processes the information to only get the hostname
            outputProceesed = str(output).split("'")[1::2]
            print(
                element[1].psrc + "	 " + element[1].hwsrc + "	 " + (f"Their Hostname is {outputProceesed[0]}\n"))



    elif ans == "3":

        try:
            for user in user_list:
                username = user.name
                publicIp = requests.get('https://checkip.amazonaws.com').text.strip()
                ip_address = publicIp
                stripped_line = publicIp.strip()
                params = ['country', 'city']
                resp = requests.get('http://ip-api.com/json/' + stripped_line, params={'fields': ','.join(params)})
                infoip = resp.json()
            print("")
            print("Current system user are: ", username)
            print("Your Computer Name is:   ", hostname)
            print("")
            print("My subnet IP:            ", privateIp)
            print("My public IP:            ", publicIp)
            print("")
            socket.setdefaulttimeout(0.25)
            print_lock = threading.Lock()

            target = (privateIp)
            t_IP = socket.gethostbyname(target)


            def portscan(port):
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    con = s.connect((t_IP, port))
                    with print_lock:
                        print(port, 'is open')
                    con.close()
                except:
                    pass


            def threader():
                while True:
                    worker = q.get()
                    portscan(worker)
                    q.task_done()


            q = Queue()
            startTime = time.time()

            for x in range(100):
                t = threading.Thread(target=threader)
                t.daemon = True
                t.start()

            for worker in range(1, 500):
                q.put(worker)

            q.join()
        except:

             print("No line available")

    elif ans == "4":
        print("")


        def get_size(bytes, suffix="B"):
            """
            Scale bytes to its proper format
            e.g:
                1253656 => '1.20MB'
                1253656678 => '1.17GB'
            """
            factor = 1024
            for unit in ["", "K", "M", "G", "T", "P"]:
                if bytes < factor:
                    return f"{bytes:.2f}{unit}{suffix}"
                bytes /= factor


        print("=" * 40, "System Information", "=" * 40)
        uname = platform.uname()
        print(f"System: {uname.system}")
        print(f"Node Name: {uname.node}")
        print(f"Machine: {uname.machine}")
        print(f"Processor: {uname.processor}")



        # let's print CPU information
        print("=" * 40, "CPU Info", "=" * 40)
        # number of cores
        print("Physical cores:", psutil.cpu_count(logical=False))
        print("Total cores:", psutil.cpu_count(logical=True))
        # CPU frequencies
        cpufreq = psutil.cpu_freq()
        print(f"Max Frequency: {cpufreq.max:.2f}Mhz")
        print(f"Current Frequency: {cpufreq.current:.2f}Mhz")
        # CPU usage
        print(f"Total CPU Usage: {psutil.cpu_percent()}%")

        # Memory Information
        print("=" * 40, "Memory Information", "=" * 40)
        # get the memory details
        svmem = psutil.virtual_memory()
        print(f"Total: {get_size(svmem.total)}")
        print(f"Available: {get_size(svmem.available)}")
        print(f"Used: {get_size(svmem.used)}")
        print(f"Percentage: {svmem.percent}%")

        # Disk Information
        print("=" * 40, "Disk Information", "=" * 40)
        print("Partitions and Usage:")
        # get all disk partitions
        partitions = psutil.disk_partitions()
        for partition in partitions:
            print(f"=== Device: {partition.device} ===")
            print(f"  Mountpoint: {partition.mountpoint}")
            print(f"  File system type: {partition.fstype}")
            try:
                partition_usage = psutil.disk_usage(partition.mountpoint)
            except PermissionError:
                # this can be catched due to the disk that
                # isn't ready
                continue
            print(f"  Total Size: {get_size(partition_usage.total)}")
            print(f"  Used: {get_size(partition_usage.used)}")
            print(f"  Free: {get_size(partition_usage.free)}")
            print(f"  Percentage: {partition_usage.percent}%")
        # get IO statistics since boot
        disk_io = psutil.disk_io_counters()


        # GPU information

        print("=" * 40, "GPU Details", "=" * 40)
        gpus = GPUtil.getGPUs()
        list_gpus = []
        for gpu in gpus:
            # get the GPU id
            gpu_id = gpu.id
            # name of GPU
            gpu_name = gpu.name
            # get % percentage of GPU usage of that GPU
            gpu_load = f"{gpu.load * 100}%"
            # get free memory in MB format
            gpu_free_memory = f"{gpu.memoryFree}MB"
            # get used memory
            gpu_used_memory = f"{gpu.memoryUsed}MB"
            # get total memory
            gpu_total_memory = f"{gpu.memoryTotal}MB"
            # get GPU temperature in Celsius
            gpu_temperature = f"{gpu.temperature} °C"
            gpu_uuid = gpu.uuid
            list_gpus.append((
                gpu_id, gpu_name, gpu_load, gpu_free_memory, gpu_used_memory,
                gpu_total_memory, gpu_temperature, gpu_uuid
            ))

        print(tabulate(list_gpus, headers=("id", "name", "load", "free memory", "used memory", "total memory",
                                           "temperature", "uuid")))
        print("")

    elif ans == "5":
        print("")
        try:
            # IP address to test
            ip_address = input("digit here the ip:")

            # URL to send the request to
            request_url = 'https://geolocation-db.com/jsonp/' + ip_address
            # Send request and decode the result
            response = requests.get(request_url)
            result = response.content.decode()
            # Clean the returned string so it just contains the dictionary data for the IP address
            result = result.split("(")[1].strip(")")
            # Convert this data into a dictionary
            result = json.loads(result)
            print(result)
        except:

            print("No line available")

        print("")
    elif ans == "6":
        import pyqrcode

        url = input("insert the link:     ")
        url = pyqrcode.create(url)
        # print(url.terminal(quiet_zone=1)) #per viasualizzare il codice qr
        url.svg('QR_Code.svg', scale=10, background="white", module_color="#7D007D", )
        print("")

    elif ans == "7":
        c = 0
        for process in psutil.process_iter():
            c = c + 1
            Name = process.name()  # Name of the process
            ID = process.pid  # ID of the process
            print("Process name =", Name, ",", "Process ID =", ID)
        print("\nTotal number of running process are ", c)


        def terminate(ProcessName):
            os.system('taskkill /IM "' + ProcessName + '" /F')


        ans = input('Enter the process to terminate:  ')
        if ans != "":
            terminate(ans)
        elif ans == "":
            print('no valid selection')

        print("")

    elif ans == "8":
        url = input('enter link here:  ')
        my_video = YouTube(url)

        print("*********************Video Title************************")
        # get Video Title
        print(my_video.title)

        print("********************Tumbnail Image***********************")
        # get Thumbnail Image
        print(my_video.thumbnail_url)

        print("********************Download video*************************")
        # get all the stream resolution for the
        for stream in my_video.streams:
            print(stream)

        # set stream resolution
        my_video = my_video.streams.get_highest_resolution()

        # or
        # my_video = my_video.streams.first()

        # Download video
        my_video.download()
        print("9")
        print('your download ended !!!   ')

    elif ans == "9":
        output = subprocess.check_output("netsh wlan show profiles")
        ssidsplit1 = str(output).split('. ')
        ssidsplit2 = str(ssidsplit1).split(': ')
        nofwlans = len(ssidsplit2)
        nofwlansreal = nofwlans - 1
        print('n of total profiles:  ', nofwlansreal)
        print('this will find saved password where possible')

        print('')

        for nofwlans in range(1, nofwlans):
            try:
                pop1 = ssidsplit2.pop()

                populito = pop1[:-36]
                populitodalback = str(populito).replace("\\", "")
                output2 = subprocess.check_output(f"""netsh wlan show profile "{populitodalback}" key=clear""")
                splitpass = str(output2).split(':')
                pop2 = splitpass.pop(5)
                pop2pulito = pop2[:-31]
                pop3 = splitpass.pop(24)
                pop4 = splitpass.pop(20)
                pop2pulito2 = pop3[:-77]
                pop2pulito3 = pop4[:-77]
                nome = populitodalback
                password = (pop2pulito2 + pop2pulito3)
                print(nome + '   ----  ' + password)
            except:
                print('')



        for nofwlans in range(1, nofwlans):
            try:
                pop1 = ssidsplit2.pop(nofwlans)

                populito = pop1[:-36]
                output2 = subprocess.check_output(f"""netsh wlan show profile "{populito}" key=clear""")
                splitpass = str(output2).split(':')
                pop2 = splitpass.pop(5)
                pop2pulito = pop2[:-31]
                pop3 = splitpass.pop(20)
                pop2pulito2 = pop3[:-77]
                print(pop2pulito + '   ----  ' + pop2pulito2)
            except:
                print('')

    elif ans == "97":
        print("""
              [+] ping
              [+] cmd
              [+] chkdsk
              [+] color 3
              [+] ipconfig
              [+] ipconfig /all
              [+] ipconfig /release
              [+] shutdown /r
              """)

    elif ans == "98":
        print(Fore.YELLOW + """\nPlease enter the type of scan you want to run:
                                                            *******************************************************
                    [1] Port Scanner                         Current system user are:     >>>""", username, """ 
                    [2] Network scanner (automatic)          Your Computer Name is:       >>>""", hostname, """ 
                    [2.2] Alternative scanner                My subnet IP:                >>>""", privateIp, """
                    [2.3] Manual scanner                     
                    [3] Sys info                             *******************************************************
                    [4] Hardware info                        
                    [5] Ip localizer                        [97] Print the available cmd commands
                    [6] Make QR Code                        [98] Print this help screen
                    [7] Process viewer and killer           [99] exit
                    [8] Youtube downloader
                    [9] See saved WIFI password

                    \n""" + Style.RESET_ALL)
    elif ans == "99":
        print("closing session...")
        time.sleep(1)
        break

    elif ans != (""):
        print(" Not Valid Choice Try again")