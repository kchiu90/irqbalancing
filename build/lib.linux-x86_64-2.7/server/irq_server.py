#!/usr/bin/env python
"""
Task: IRQ Client/Server in Python.
IRQ Information Service like a service, that presents a restful API which allows:
- Get an overview of how interrupts are distributed among the different CPUs in our system.
-   This overview should be over a specified time window.
- Set the CPU affinity for each interrupt.
- Provide a basic init script to start this service at machine boot time.
- Package the service as a basic wheel using setuptools.
Author: James Chiu (kuo.chiu@verizondigitalmedia.com)
Last Modified: June 7, 2018
"""

import os
import time
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)


# Function to collect data in /proc/interrupts
def collect(output='raw'):
    # Using access() to check if user is authorized to open file before actually doing so. os.R_OK: readability.
    if not os.access('/proc/interrupts', os.R_OK):
        return False
    # Here I used 2 dictionaries to hold data
    result = dict()
    other_result = dict()

    # Open interrupts file
    fh = open('/proc/interrupts', 'r')
    if output == 'raw':
        return fh.read()

    # Get data
    cpuCount = None
    # Read in data line-by-line
    for line in fh:
        if not cpuCount:
            cpuCount = len(line.split())
        else:
            # strip() remove spaces, and split() 6 times to format (and store) all data for later.
            data = line.strip().split(None, cpuCount + 2)
            # Replace : with space, which is to remove the unneeded :
            data[0] = data[0].replace(':', '')
            if len(data) == 2:
                continue
            else:
                # Y-axis parsing data horizontally, index traverse through line data save value up to CPU3.
                for index, value in enumerate(data):
                    if index == 0 or index >= cpuCount + 1:
                        continue
                    cpu = 'CPU' + str(index - 1)
                    if other_result.get(cpu, None):
                        other_result[cpu].append({'name': data[0], 'value': int(value)})
                    else:
                        other_result[cpu] = list()
                        other_result[cpu].append({'name': data[0], 'value': int(value)})
                    metric_name_node = 'CPU' + str(index - 1) + '.' + data[0]
                    result[metric_name_node] = int(value)
    result['cpuCount'] = cpuCount
    # Close file
    fh.close()
    return result


# Homepage of this service, showing some sample commands.
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


# This module provides current interrupt distribution among CPUs.
# Can pass in output format as argument.
@app.route('/get_current_distribution', methods=['GET'])
def get_current_distribution():
    output = request.args.get('format', 'raw')
    result = collect(output)
    if output == 'raw':
        return result
    else:
        return jsonify(result)


# This module provides interrupts handled by CPU within given time.
# Default value shows ALL CPU, within 5 second time window.
@app.route('/get_interrupt_by_cpu', methods=['GET'])
def get_interrupt_by_cpu():
    cpu_id = request.args.get('cpu', 'all')
    time_window = float(request.args.get('second', 5))

    first = collect(output='json')
    time.sleep(time_window)
    second = collect(output='json')

    result = {key: second[key] - first.get(key, 0) for key in second.keys()}
    cpus = second.get('cpuCount', 0)
    data = dict()
    for cpu in range(cpus):
        cpuid = 'CPU' + str(cpu)
        total = 0
        for key in result.keys():
            if key.startswith(cpuid):
                total += result[key]
        data[cpuid] = total

    if cpu_id == 'all':
        return jsonify(data)
    if int(cpu_id) >= cpus:
        return "Not found", 404

    return jsonify({'CPU'+cpu_id: data['CPU'+cpu_id]})


# This module updates specific IRQ#'s smp_affinity based on the input.
# The default path is: /proc/irq/smp_affinity, user needs to specify IRQ# and affinity value (default=1).
# Server (irq_server.py) needs to run as root otherwise it will throw 403 permission denied error.
@app.route('/set_affinity/<string:irq>', methods=['PUT'])
def set_affinity(irq):
    cpu = request.args.get('cpu', 1)
    dir = "/proc/irq"
    filepath = os.path.join(dir, irq, 'smp_affinity')
    if not os.path.exists(filepath):
        return "Invalid irq", 404
    try:
        with open(filepath, 'w') as fh:
            fh.write(str(cpu))
    except IOError as err:
        return "%s" % str(err), 403
    return "Ok", 200


if __name__ == "__main__":
    app.run(host='0.0.0.0')
