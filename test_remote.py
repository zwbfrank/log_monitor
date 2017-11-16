#!/usr/bin/env python
# coding:utf-8
import os
import re
import signal
import subprocess
import time
import smtplib

from email.mime.text import MIMEText
from email.header import Header
from email.utils import parseaddr,formataddr
import pymysql
import paramiko

import sys

from threading import Timer,Thread
from multiprocessing import Process, Queue
from datetime import time, datetime, timedelta

def tail_ssh_newest_file():
    directory = "/var/log/ppss_biz_service/"
    ssh = ssh_connect('120.27.220.53', 8222, 'hsplan', 'wUrSLSoE%Jaih*sx%M')
    ssh_newest_file = get_ssh_newest_file()
    log_file = ssh_newest_file
    command_tail = "tail -F " + directory + log_file
    stdin, stdout, stderr = ssh.exec_command(command_tail)
    while True:
        output = stdout.readline().strip()
        if not output:
            continue
        print(output)
        