#!/usr/bin/env python
import os
import re
import sys
import os.path
import paramiko
from tail_file import timing_task
import json
from global_variable import ssh_newest_files


def ssh_connect(hostname, port, username, password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(hostname, port, username, password)
        return ssh
    except:
        pass
    
def get_ssh_newest_file():
    # newest_logs = []
    ssh = ssh_connect('120.27.220.53', 8222, 'hsplan', 'wUrSLSoE%Jaih*sx%M')
    # log_file = "biz-service-info.log"
    # command_cat = "cat /var/log/ppss_biz_service/" + log_file + "|grep ERROR"
    command_ls = "ls -rt /var/log/ppss_biz_service|tail -2"
    stdin, stdout, stderr = ssh.exec_command(command_ls)
    output = stdout.readlines()
    for i in range(len(output)):
        line = output[i].strip()
        # print(ssh_newest_files)
        if line not in ssh_newest_files:
            ssh_newest_files.append(line)
            # print(line)
    # print(ssh_newest_files)
    ssh.close()

def cat_ssh_newest_file():
    directory = "/var/log/ppss_biz_service/"
    ssh = ssh_connect('120.27.220.53', 8222, 'hsplan', 'wUrSLSoE%Jaih*sx%M')
    ssh_newest_files = get_ssh_newest_file()
    log_file = ssh_newest_files.pop()

    command_cat = "cat "+directory+log_file+"|grep ERROR"
    sdin,stdout,stderr = ssh.exec_command(command_cat)
    lines = stdout.readlines()
    for i in range(len(lines)):
        line = lines[i].strip()
        print(line)
    
def tail_ssh_newest_file():
    directory = "/var/log/ppss_biz_service/"
    ssh = ssh_connect('120.27.220.53', 8222, 'hsplan', 'wUrSLSoE%Jaih*sx%M')
    ssh_newest_files = get_ssh_newest_file()
    log_file = ssh_newest_files.pop()
    command_tail = "tail -F "+directory+log_file
    stdin,stdout,stderr = ssh.exec_command(command_tail)
    while True:
        output = stdout.readline().strip()
        print(output)
    # for i in range(len(output)):
    #     line = output[i].strip()
    #     print(line)
    
# def ssh_log_analyze():
    


if __name__ == '__main__':
    
    timing_task(get_ssh_newest_file,second=5)
    # ssh_newest_files = get_ssh_newest_file()
    # print(ssh_newest_files)
    # tail_ssh_newest_file()
    
    # cat_ssh_newest_file()
    
    
