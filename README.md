# IRQ Balancing

## Task: IRQ Balancing Algorithm

* File name and location: irq_balance.py
```
jchiu@y700:~/code/irqbalancing$ ls -lsh | grep irq_balance.py 
4.0K -rw-rw-r-- 1 jchiu jchiu 1.7K Jun  7 22:37 irq_balance.py
```

* Install PrettyTable
```
jchiu@y700:~/code/irqbalancing$ pip install prettytable
Collecting prettytable
  Downloading https://files.pythonhosted.org/packages/ef/30/4b0746848746ed5941f052479e7c23d2b56d174b82f4fd34a25e389831f5/prettytable-0.7.2.tar.bz2
Building wheels for collected packages: prettytable
  Running setup.py bdist_wheel for prettytable ... done
  Stored in directory: /home/jchiu/.cache/pip/wheels/80/34/1c/3967380d9676d162cb59513bd9dc862d0584e045a162095606
Successfully built prettytable
Installing collected packages: prettytable
Successfully installed prettytable-0.7.2
```

* Make sure sample_interrupt is stored under same directory.
```
parser.add_argument('-l', '--location', default='sample_interrupt',
                     help="location of the sample interrupt file")
```

* To run the script: python irq_balance.py (--threshold 10 is optional)
```
jchiu@y700:~/code/irqbalancing$ python irq_balance.py --threshold 10
+------+--------+--------+-----------------+
| IRQ# | CPU0 % | CPU1 % | Set affinity to |
+------+--------+--------+-----------------+
| 132: |  0.29  | 99.71  |       CPU0      |
| 133: | 69.45  | 30.55  |       CPU1      |
| 134: | 99.49  |  0.51  |       CPU1      |
| 135: |  55.7  |  44.3  |       CPU1      |
| 136: | 69.89  | 30.11  |       CPU1      |
| 137: |  25.1  |  74.9  |       CPU0      |
| 138: | 63.14  | 36.86  |       CPU1      |
| 139: | 28.37  | 71.63  |       CPU0      |
| 140: | 45.49  | 54.51  |     Balanced    |
| 141: | 30.27  | 69.73  |       CPU0      |
| 142: |  1.93  | 98.07  |       CPU0      |
| 143: | 64.63  | 35.37  |       CPU1      |
| 144: |  69.4  |  30.6  |       CPU1      |
| 145: | 32.69  | 67.31  |       CPU0      |
| 146: | 67.58  | 32.42  |       CPU1      |
| 147: | 22.78  | 77.22  |       CPU0      |
| 148: |  56.1  |  43.9  |       CPU1      |
| 149: | 36.32  | 63.68  |       CPU0      |
| 150: |  83.9  |  16.1  |       CPU1      |
| 151: | 25.39  | 74.61  |       CPU0      |
| 152: | 73.42  | 26.58  |       CPU1      |
| 153: | 28.84  | 71.16  |       CPU0      |
| 154: | 43.91  | 56.09  |       CPU0      |
| 155: | 26.01  | 73.99  |       CPU0      |
| 156: | 70.37  | 29.63  |       CPU1      |
| 157: |  22.8  |  77.2  |       CPU0      |
| 158: | 46.14  | 53.86  |     Balanced    |
| 159: | 24.61  | 75.39  |       CPU0      |
| 160: | 39.85  | 60.15  |       CPU0      |
| 161: | 25.08  | 74.92  |       CPU0      |
| 162: | 41.15  | 58.85  |       CPU0      |
| 163: | 24.06  | 75.94  |       CPU0      |
| 164: | 26.61  | 73.39  |       CPU0      |
| 165: | 31.58  | 68.42  |       CPU0      |
| 166: | 24.55  | 75.45  |       CPU0      |
| 167: | 22.29  | 77.71  |       CPU0      |
| 168: |  27.9  |  72.1  |       CPU0      |
| 169: | 23.97  | 76.03  |       CPU0      |
| 170: | 27.41  | 72.59  |       CPU0      |
| 171: | 26.08  | 73.92  |       CPU0      |
| 172: | 20.96  | 79.04  |       CPU0      |
| 173: |  23.8  |  76.2  |       CPU0      |
| 174: | 24.24  | 75.76  |       CPU0      |
| 175: | 25.34  | 74.66  |       CPU0      |
| 176: | 22.74  | 77.26  |       CPU0      |
| 177: |  22.0  |  78.0  |       CPU0      |
| 178: | 20.51  | 79.49  |       CPU0      |
| 179: | 23.17  | 76.83  |       CPU0      |
| 180: | 23.71  | 76.29  |       CPU0      |
| 181: | 21.11  | 78.89  |       CPU0      |
| 182: |  24.9  |  75.1  |       CPU0      |
| 183: | 24.44  | 75.56  |       CPU0      |
| 184: | 22.14  | 77.86  |       CPU0      |
| 185: | 26.04  | 73.96  |       CPU0      |
| 186: | 22.98  | 77.02  |       CPU0      |
| 187: | 27.31  | 72.69  |       CPU0      |
| 188: | 22.84  | 77.16  |       CPU0      |
| 189: | 25.29  | 74.71  |       CPU0      |
| 190: | 25.49  | 74.51  |       CPU0      |
| 191: | 20.33  | 79.67  |       CPU0      |
| 192: | 23.94  | 76.06  |       CPU0      |
| 193: | 22.49  | 77.51  |       CPU0      |
| 194: | 22.92  | 77.08  |       CPU0      |
| 195: | 25.71  | 74.29  |       CPU0      |
| 196: | 22.82  | 77.18  |       CPU0      |
+------+--------+--------+-----------------+
```

------------

## Task: IRQ Client/Server in Python

### Server side: irq_server.py
```
To Execute: python irq_server.py 
Location: /code/irqbalancing/server
```
#### Options available:
##### get_current_distribution
```
Arguments:
* format = [ json | raw ]
```

```
Example:
http://localhost:5000/get_current_distribution?format=json
http://localhost:5000/get_current_distribution?format=raw
```
##### Get_interrupt_by_cpu
```
Arguments: 
* cpu (default: all)
* second (default: 5)
```
```
Example:
http://localhost:5000/get_interrupt_by_cpu
http://localhost:5000/get_interrupt_by_cpu?cpu=1&second=3
```
##### set_affinity/irq#
```
Arguments:
* irq
* cpu
```
```
Example:
http://localhost:5000/set_affinity/129?cpu=f
```

------------

### Client side: irq_client.py
```
To Execute: python irq_client.py [ --url | --port | --view | --second | --irq | --cpu ]
Location: /code/irqbalancing
```
Default value for arguments listed above:
```
--url = http://localhost
--port = 5000
--second = 5
--cpu = 1
```
#### Options available:
##### --view distribution
```
jchiu@y700:~/code/irqbalancing$ python irq_client.py --view distribution
            CPU0       CPU1       CPU2       CPU3       
   0:         21          0          0          0  IR-IO-APIC    2-edge      timer
   8:          1          0          0          0  IR-IO-APIC    8-edge      rtc0
   9:          0          0          0          0  IR-IO-APIC    9-fasteoi   acpi
  17:        283        104        189         46  IR-IO-APIC   17-fasteoi   snd_hda_intel:card1
 120:          0          0          0          0  DMAR-MSI    0-edge      dmar0
 121:          0          0          0          0  IR-PCI-MSI 16384-edge      PCIe PME
 122:          0          0          0          0  IR-PCI-MSI 458752-edge      aerdrv, PCIe PME
 123:          0          0          0          0  IR-PCI-MSI 468992-edge      aerdrv, PCIe PME
 124:        148         81     343319         91  IR-PCI-MSI 327680-edge      xhci_hcd
 125:       6973       1745       1812      42554  IR-PCI-MSI 376832-edge      ahci[0000:00:17.0]
 126:          0          0          0          0  IR-PCI-MSI 1048576-edge      enp2s0
 127:        601        154     824177       9216  IR-PCI-MSI 524288-edge      nvkm
 128:         30          1          0          3  IR-PCI-MSI 360448-edge      mei_me
 129:        291      39876       2828      20651  IR-PCI-MSI 1572864-edge      iwlwifi
 130:        615        146         11         32  IR-PCI-MSI 514048-edge      snd_hda_intel:card0
 NMI:         50         50         51         52   Non-maskable interrupts
 LOC:   35505103   33437824   32126113   38625686   Local timer interrupts
 SPU:          0          0          0          0   Spurious interrupts
 PMI:         50         50         51         52   Performance monitoring interrupts
 IWI:          0          0          0          0   IRQ work interrupts
 RTR:          0          0          0          0   APIC ICR read retries
 RES:     103642      97831      99954      74961   Rescheduling interrupts
 CAL:      73046      76704      70844      71996   Function call interrupts
 TLB:      69211      75614      69508      70965   TLB shootdowns
 TRM:          0          0          0          0   Thermal event interrupts
 THR:          0          0          0          0   Threshold APIC interrupts
 DFR:          0          0          0          0   Deferred Error APIC interrupts
 MCE:          0          0          0          0   Machine check exceptions
 MCP:         17         17         17         17   Machine check polls
 ERR:          0
 MIS:          0
 PIN:          0          0          0          0   Posted-interrupt notification event
 NPI:          0          0          0          0   Nested posted-interrupt event
 PIW:          0          0          0          0   Posted-interrupt wakeup event
```

##### --view cpu-summary 
```Arguments:
* second (default 5 sec, can manually specify desired time)
```
```
jchiu@y700:~/code/irqbalancing$ python irq_client.py --view cpu-summary
Interrupt handled by CPU in last 5 seconds
CPU2: 19513
CPU3: 5350
CPU0: 10486
CPU1: 11228

jchiu@y700:~/code/irqbalancing$ python irq_client.py --view cpu-summary --second 3
Interrupt handled by CPU in last 3 seconds
CPU2: 1864
CPU3: 12786
CPU0: 4050
CPU1: 8728
```

##### irq (When irq_server is running as root)
```
Arguments:
* irq
* cpu
```
```
jchiu@y700:~/code/irqbalancing$ cat /proc/irq/129/smp_affinity
2
jchiu@y700:~/code/irqbalancing$ python irq_client.py --irq 129 --cpu f
Successfully set affinity for IRQ 129
jchiu@y700:~/code/irqbalancing$ cat /proc/irq/129/smp_affinity
f
```

------------

### How to do init.d
* Make the init.d script executable
```
jchiu@y700:~/code/irqbalancing$ chmod +x irqserver.sh 
jchiu@y700:~/code/irqbalancing$ ls -lsh
total 28K
4.0K -rw-rw-r-- 1 jchiu jchiu 3.5K Jun  7 15:19 irq_client.py
4.0K -rwxrwxr-x 1 jchiu jchiu 1.4K Jun  7 20:39 irqserver.sh
4.0K drwxrwxr-x 6 jchiu jchiu 4.0K Jun  7 09:08 irq_venv
4.0K -rw-rw-r-- 1 jchiu jchiu 2.6K Jun  7 11:20 README.rst
4.0K drwxrwxr-x 3 jchiu jchiu 4.0K Jun  7 18:38 server
4.0K -rw-rw-r-- 1 jchiu jchiu  253 Jun  7 09:04 setup.cfg
4.0K -rw-rw-r-- 1 jchiu jchiu 1.1K Jun  7 20:31 setup.py
```

* Copy to irqserver (sh file) to /etc/init.d
```
jchiu@y700:~/code/irqbalancing$ sudo cp irqserver.sh /etc/init.d/

jchiu@y700:/etc/init.d$ ls -lsh | grep irqserver 
4.0K -rwxr-xr-x 1 root root 1.5K Jun  7 21:21 irqserver
```

* Install service to be run at boot-time:
```
jchiu@y700:/etc/init.d$ update-rc.d irqserver defaults
```

* Reboot and check status:
```
jchiu@y700:/etc/init.d$ /etc/init.d/irqserver status
irqserver is Running with PID 894

OR

jchiu@y700:~$ ps aux | grep irq_server
root       894  0.0  0.2 225808 21268 ?        S    21:21   0:00 python /home/jchiu/code/irqbalancing/server/irq_server.py
jchiu     3202  0.0  0.0  21292   940 pts/17   S+   21:28   0:00 grep --color=auto irq_server
```

------------

### How to Build Wheel:

* Command :
```
jchiu@y700:~/code/irqbalancing$ python setup.py bdist_wheel
/usr/lib/python2.7/dist-packages/setuptools/dist.py:285: UserWarning: Normalizing 'v0.1' to '0.1'
  normalized_version,
running bdist_wheel
running build
running build_py
creating build
creating build/lib.linux-x86_64-2.7
creating build/lib.linux-x86_64-2.7/server
copying server/__init__.py -> build/lib.linux-x86_64-2.7/server
copying server/irq_server.py -> build/lib.linux-x86_64-2.7/server
installing to build/bdist.linux-x86_64/wheel
running install
running install_lib
creating build/bdist.linux-x86_64
creating build/bdist.linux-x86_64/wheel
creating build/bdist.linux-x86_64/wheel/server
copying build/lib.linux-x86_64-2.7/server/__init__.py -> build/bdist.linux-x86_64/wheel/server
copying build/lib.linux-x86_64-2.7/server/irq_server.py -> build/bdist.linux-x86_64/wheel/server
running install_egg_info
running egg_info
creating irqservice.egg-info
writing requirements to irqservice.egg-info/requires.txt
writing irqservice.egg-info/PKG-INFO
writing top-level names to irqservice.egg-info/top_level.txt
writing dependency_links to irqservice.egg-info/dependency_links.txt
writing entry points to irqservice.egg-info/entry_points.txt
writing manifest file 'irqservice.egg-info/SOURCES.txt'
reading manifest file 'irqservice.egg-info/SOURCES.txt'
writing manifest file 'irqservice.egg-info/SOURCES.txt'
Copying irqservice.egg-info to build/bdist.linux-x86_64/wheel/irqservice-0.1.egg-info
running install_scripts
creating build/bdist.linux-x86_64/wheel/irqservice-0.1.dist-info/WHEEL
```

* After the execution above, few folders and files were generated.
```
jchiu@y700:~/code/irqbalancing$ ls -lsh
total 40K
4.0K drwxrwxr-x 4 jchiu jchiu 4.0K Jun  7 22:08 build
4.0K drwxrwxr-x 2 jchiu jchiu 4.0K Jun  7 22:08 dist
4.0K -rw-rw-r-- 1 jchiu jchiu 3.5K Jun  7 22:01 irq_client.py
4.0K -rwxr-xr-x 1 root  root  1.5K Jun  7 21:55 irqserver
4.0K drwxrwxr-x 2 jchiu jchiu 4.0K Jun  7 22:08 irqservice.egg-info
4.0K -rw-rw-r-- 1 jchiu jchiu   58 Jun  7 22:06 README.md
4.0K -rw-rw-r-- 1 jchiu jchiu 2.6K Jun  7 11:20 README.rst
4.0K drwxrwxr-x 3 jchiu jchiu 4.0K Jun  7 18:38 server
4.0K -rw-rw-r-- 1 jchiu jchiu  253 Jun  7 09:04 setup.cfg
4.0K -rw-rw-r-- 1 jchiu jchiu 1.1K Jun  7 21:47 setup.py
```

* Under dist directory.
```jchiu@y700:~/code/irqbalancing$ ls -lsh dist/
total 8.0K
8.0K -rw-rw-r-- 1 jchiu jchiu 4.3K Jun  7 22:08 irqservice-0.1-py2.py3-none-any.whl
```
