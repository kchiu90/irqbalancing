#!/usr/bin/env python

"""
Task: IRQ Balancing Algorithm
Write a short python script to do an approximation of the best way to evenly balance these IRQs between two CPUs.
Your script should output:
- A list of IRQs to have their affinity set to CPU0 or CPU1.
- A metric showing how closely balanced the IRQs are.

Author: James Kuo Chiu (kuo.chiu@verizondigitalmedia.com)
Last Modified: June 7, 2018
"""

import csv
import argparse
from prettytable import PrettyTable


# This script takes 2 arguments: -l for file location and -t for desired threshold (default=5).
def get_arguments():
    parser = argparse.ArgumentParser(description='Check irq balance')
    parser.add_argument('-l', '--location', default='sample_interrupt',
                        help="location of the sample interrupt file")
    parser.add_argument('-t', '--threshold', type=int, default=5,
                        help='Define the definition threshold for good distribution')
    args = parser.parse_args()
    return {'location': args.location, 'threshold': args.threshold}


# Reads in file in line, parse it accordingly.
def import_text(filename, separator):
    for line in csv.reader(open(filename), delimiter=separator, 
                           skipinitialspace=True):
        if line:
            yield line


# This section checks whether the distribution is in balance based on the threshold.
def is_balance(irq, cpu0, cpu1, threshold=5):
    total = int(cpu0) + int(cpu1)
    # Here we only calculate till 2 digits after decimal point.
    cpu0_per = float("{:.2f}".format(float(cpu0) / float(total) * 100))
    cpu1_per = float("{:.2f}".format(float(cpu1) / float(total) * 100))

    # Below are comparison and determine what output should be for the table.
    if abs(cpu0_per - cpu1_per) <= threshold:
        return [irq, cpu0_per, cpu1_per, "Balanced"]
    elif cpu0_per - cpu1_per > 0:
        return [irq, cpu0_per, cpu1_per, "CPU1"]
    elif cpu1_per - cpu0_per > 0:
        return [irq, cpu0_per, cpu1_per, "CPU0"]


def main():
    args = get_arguments()
    table = PrettyTable()
    table.field_names = ["IRQ#", "CPU0 %", "CPU1 %", "Set affinity to"]
    interrupt_file = args.get('location')
    threshold = args.get('threshold')
    separator = ' '
    # Store data into a list.
    data = list()
    for line in import_text(interrupt_file, separator):
        data.append(line)
    for i in range(1, len(data)):
        table.add_row(is_balance(data[i][0], data[i][1], data[i][2], threshold))
    print table


if __name__ == '__main__':
    main()
