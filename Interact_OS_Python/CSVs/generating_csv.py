import csv

hosts = [['webserver.local', '192.2.0.0.1'], ['webserver.cloud', '345.10.2.0.1']]

with open('hosts.txt', 'w') as host_f:
    writer = csv.writer(host_f)
    #   the writer variable is now an instance of the csv writer class
    writer.writerows(hosts)
