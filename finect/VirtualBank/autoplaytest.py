import os
import sys
# path = '/home/1900000001SERVERID/sftp-root/SEND/'
path = '/lost+found'
if os.path.isdir(path):
    pollablelist = os.listdir(path)
else:
    sys.exit()
files = os.listdir(path)
print(files)

