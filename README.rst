IRQ Balancing Modern servers typically have many cores.
Modern high performance network cards present many queues to the host, each with their own interrupt.
The linux program irqbalance doesn't always evenly balance all these queue IRQs between CPUs on a multicore system.
In order to make sure that a single core isn't completely overloaded by interrupt requests, it is sometimes necessary
to manually set affinity to balance the IRQs.

Here is some background:
https://en.m.wikipedia.org/wiki/Network_interface_controller#Performance_and_advanced_functionality
https://access.redhat.com/documentation/en-US/Red_Hat_Enterprise_Linux/6/html/Performance_Tuning_Guide/s-cpu-irq.html


Task: IRQ Balancing Algorithm
Below is a contrived /proc/interrupts that shows the rate of interrupts that are occuring in interrupts per day
(instead of the raw count that /proc/interrupts actually shows). Write a short python script to do an approximation of
the best way to evenly balance these IRQs between two CPUs.

Your script should output:
- A list of IRQs to have their affinity set to CPU0 or CPU1.
- A metric showing how closely balanced the IRQs are.

You can assume:
Although the mock /proc/interrupts shows IRQs being serviced by both CPUs,
will be pinning one interrupt to one CPU for simplicity.


Task: IRQ Client/Server in Python
IRQ Information Service We would like a service, written in python, that presents a restful API which allows us to:
- Get an overview of how interrupts are distributed among the different CPUs in our system.
  This overview should be over a specified time window, showing how many interrupts fired within
  the window and on which CPUs.
- Set the CPU affinity for each interrupt. This can be simplified by allowing only one CPU to be associated with
  any given interrupt (instead of supporting the entire mask).
- Provide a basic init script to start this service at machine boot time. Our target OS is Ubuntu 14.04 or 16.04.
- Bonus: Package the service as a basic wheel using setuptools.

You can assume:
- You can use flask to make writing the service more straight forward.
- This service will be run as root.
- No authentication or encryption is necessary.


IRQ Service Client
We would like a python client to interact with this service.

It should be able to:
- Give a complete overview of the current distribution of interrupts.
- Give a summary of how many interrupts have been serviced by each CPU.
- Be able to use the service to set the affinity of various interrupts.

You can assume:
- Client can be a standalone script, packaging isn't necessary.
