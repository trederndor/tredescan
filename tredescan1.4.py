from __future__ import print_function
from datetime import datetime
from tabulate import tabulate
from queue import Queue
from colorama import Fore
from colorama import Style
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
import colorama


colorama.init()
privateIp = socket.gethostbyname(socket.gethostname())
hostname = socket.gethostname()
publicIp = requests.get('https://checkip.amazonaws.com').text.strip()

print(Fore.GREEN +"""


 
████████╗██████╗ ███████╗██████╗ ███████╗███████╗ ██████╗ █████╗ ███╗   ██╗
╚══██╔══╝██╔══██╗██╔════╝██╔══██╗██╔════╝██╔════╝██╔════╝██╔══██╗████╗  ██║
   ██║   ██████╔╝█████╗  ██║  ██║█████╗  ███████╗██║     ███████║██╔██╗ ██║
   ██║   ██╔══██╗██╔══╝  ██║  ██║██╔══╝  ╚════██║██║     ██╔══██║██║╚██╗██║
   ██║   ██║  ██║███████╗██████╔╝███████╗███████║╚██████╗██║  ██║██║ ╚████║
   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═════╝ ╚══════╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝
                                                                           
                                                                                         


"""+ Style.RESET_ALL)
print(Fore.YELLOW +"""\nPlease enter the type of scan you want to run

            [1] Port Scanner
            [2] OS Detection
            [3] Sys info
            [4] Hardware info
            [5] Ip localizer
            [6] Make QR Code
            [98] Print this help screen
            [99] exit

            \n"""+ Style.RESET_ALL)
ans=True
while ans:

    print(Fore.GREEN +"""What would you like to do?
    """+ Style.RESET_ALL)
    ans=input()

    if ans=="1":
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

    #elif ans=="2":
        #print("")
        #print("Il mio indirizzo IP privato:", privateIp)
        #print("")

    #elif ans=="3":
        #print("")
        #print("Il mio indirizzo IP pubblico:", publicIp)
        #print("")

    #elif ans=="4":
        #print("")
        #print("Your Computer Name is:" + hostname)
        #print("")

    elif ans=="2":
        print("")
        print("sys.platform                 ", sys.platform)
        print("platform.system()            ", platform.system())
        print("sysconfig.get_platform()     ", sysconfig.get_platform())
        print("platform.machine()           ", platform.machine())
        print("platform.architecture()      ", platform.architecture())
        print("")

    elif ans=="3":
        print("")
        print("Your Computer Name is:" + hostname)
        print("My subnet IP:", privateIp)
        print("My public IP:", publicIp)
        print("")

    elif ans=="4":
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
        print(f"System: {uname.system} {uname.release}")
        print(f"Node Name: {uname.node}")
        print(f"Machine: {uname.machine}")
        print(f"Processor: {uname.processor}")

        # Boot Time
        print("=" * 40, "Boot Time", "=" * 40)
        boot_time_timestamp = psutil.boot_time()
        bt = datetime.fromtimestamp(boot_time_timestamp)
        print(f"Boot Time: {bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}")

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

        # Network information
        print("=" * 40, "Network Information", "=" * 40)
        # get all network interfaces (virtual and physical)
        if_addrs = psutil.net_if_addrs()
        for interface_name, interface_addresses in if_addrs.items():
            for address in interface_addresses:
                print(f"=== Interface: {interface_name} ===")
                if str(address.family) == 'AddressFamily.AF_INET':
                    print(f"  IP Address: {address.address}")
                    print(f"  Netmask: {address.netmask}")
                    print(f"  Broadcast IP: {address.broadcast}")
                elif str(address.family) == 'AddressFamily.AF_PACKET':
                    print(f"  MAC Address: {address.address}")
                    print(f"  Netmask: {address.netmask}")
                    print(f"  Broadcast MAC: {address.broadcast}")
        # get IO statistics since boot
        net_io = psutil.net_io_counters()
        print(f"Total Bytes Sent: {get_size(net_io.bytes_sent)}")
        print(f"Total Bytes Received: {get_size(net_io.bytes_recv)}")

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

    elif ans=="5":
        print("")


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
        print("")
    elif ans == "6":
        import pyqrcode

        url = input("insert the link:     ")
        url = pyqrcode.create(url)
        #print(url.terminal(quiet_zone=1)) #per viasualizzare il codice qr
        url.svg('QR_Code.svg', scale=10, background="white", module_color="#7D007D", )

    elif ans=="98":
        print(Fore.MAGENTA +"""\nPlease enter the type of scan you want to run

            [1] Port Scanner
            [2] OS Detection
            [3] Sys info
            [4] Hardware info
            [5] Ip localizer
            [6] Make QR Code
            [98] Print this help screen
            [99] exit

            \n"""+ Style.RESET_ALL)
    elif ans=="99":
        print("closing session...")
        time.sleep(1)
        break
    elif ans !=(""):
        print(" Not Valid Choice Try again")