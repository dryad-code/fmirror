#!/usr/bin/python
#Note: python files read doesn't reflect updates
import os, sys, time, socket
header = '~*~___---fmirror---___~*~'
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if sys.argv[1] == '-l':
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	s.bind(('', 5068))
	s.listen(5)
	c, caddr = s.accept()
	fp = open(sys.argv[2], 'w')
	while True:
		fc = c.recv(2147483647)	#Yowza, am I right?
		f_split = fc.split('\n')
		if f_split[-1] != header:
			continue
		fl = fc.split(header)[-2]
		fp.truncate()
		fp.write(fl)
		fp.seek(0,0)
		time.sleep(2)
else:
	fp = open(sys.argv[2], 'r')
	s.connect((socket.gethostbyname(sys.argv[1]), 5068))
	while True:
		try:
			fp = open(sys.argv[2], 'r')
			s.send(fp.read() + header)
			fp.seek(0,0)
			print fp.read()
			fp.seek(0,0)
		except IOError:
			continue
		fp.seek(0,0)
