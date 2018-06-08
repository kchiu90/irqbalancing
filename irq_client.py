git #!/usr/bin/env python

# Task: IRQ Service Client
# We would like a python client to interact with this service.
# It should be able to:
# - Give a complete overview of the current distribution of interrupts.
# - Give a summary of how many interrupts have been serviced by each CPU.
# - Be able to use the service to set the affinity of various interrupts.
# Author: James Chiu (kuo.chiu@verizondigitalmedia.com)
# Last Modified: June 7, 2018

import argparse
import requests


# Get arguments, this script takes 6 different arguments for different purposes.
# python irq_client.py [ --url | --port | --view | --second | --irq | --cpu ]
def get_argument():
    parser = argparse.ArgumentParser(description="Client to query the IRQ information service")
    parser.add_argument('-u', '--url', default='http://localhost',
                        help='URL of the IRQ information service')
    parser.add_argument('-p', '--port', type=int, default=5000,
                        help='port of the IRQ information service')
    parser.add_argument('--view', choices=['distribution', 'cpu-summary'],
                        help='view current distribution or summary by CPU')
    parser.add_argument('--second', type=int, default=5,
                        help='time window in second')
    parser.add_argument('--irq',
                        help='IRQ ID to set affinity')
    parser.add_argument('--cpu', default=1,
                        help='CPU for smp_affinity value')
    args = parser.parse_args()
    return {'url': args.url, 'port': args.port,
            'view': args.view, 'second': args.second, 'irq': args.irq, 'cpu': args.cpu}


# main function parses argument and perform tasks accordingly.
def main():
    args = get_argument()
    base_url = args.get('url')
    port = args.get('port')
    view = args.get('view')

    # Code below use the result --view argument process accordingly.
    # --view = distribution
    if view == 'distribution':
        url = "{}:{}/get_current_distribution".format(base_url, port)
        try:
            content = requests.get(url).text
            print content
        except requests.RequestException as error:
            print "Unable to get data from {} due to {}".format(url, str(error))
    # --view = cpu-summary
    elif view == 'cpu-summary':
        second = args.get('second')
        url = "{}:{}/get_interrupt_by_cpu?second={}".format(base_url, port, second)
        try:
            content = requests.get(url).json()
            message = "Interrupt handled by CPU in last {} seconds\n".format(second)
            for key in content.keys():
                message += "{}: {}\n".format(key, content[key])
            print message
        except requests.RequestException as error:
            print "Unable to get data from {} due to {}".format(url, str(error))

    # Code below use the --irq and --cpu arguments to set smp_affinity
    irq = args.get('irq')
    cpu = args.get('cpu')
    if irq:
        url = "{}:{}/set_affinity/{}?cpu={}".format(base_url, port, irq, cpu)
        try:
            status_code = requests.put(url).status_code
            if status_code >= 300:
                print "Unable to set affinity for IRQ {}. Received status code: {}".format(irq, status_code)
            else:
                print "Successfully set affinity for IRQ {}".format(irq)
        except requests.RequestException as error:
            print "Unable to set affinity for IRQ {} due to {}".format(irq, str(error))


if __name__ == '__main__':
    main()
