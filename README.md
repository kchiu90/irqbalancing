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

## Task: IRQ Client/Server in Python

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
