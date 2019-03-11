#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import shutil
import sys
RECV_path = '/home/1900000001SERVERID/sftp-root/RECV/'
RECV_DONE_path = '/home/1900000001SERVERID/sftp-root/RECV_DONE/'
if os.path.isdir(RECV_path):
    pollablelist = os.listdir(RECV_path)
    print(pollablelist)
else:
    sys.exit()
for i in pollablelist:
    new_path = shutil.move(RECV_path + i,RECV_DONE_path)