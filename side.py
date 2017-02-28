import requests
import time
from prettytable import PrettyTable
import sys, getopt
from cmdopt import *
from network import *


def PrintStat(array):
	print "\n\n"
	t = PrettyTable(['Method', 'URL','# Request','MIN','MAX','AVG','RSD'])
	for i in array:
		i.statistics()
		t.add_row(i.value())

	print t

	
def main(argv):
	par=ParseOpt(argv)
	print "Timing analysis v1.0.0 - A tool for timing side-channel analysis.\n\n"
	hs=[]
	kll=None
	if par['url'] != None:
		hd=None
		if par['hd'] != None:
			hd={}
			for i in par['hd']:
				d=i.split(':')
				hd[d[0].strip()]=d[1].strip()
			t=SendData(par['md'],par['url'],hd,par['dt'],par['cnt'],par['cert'],par['dl'])
		else:
			t=SendData(par['md'],par['url'],None,par['dt'],par['cnt'],par['cert'],par['dl'])
		k=Host(par['md'],par['url'],hd,par['dt'],par['cnt'],t,par['pre'])
		hs.append(k)
	if par['fi'] != None:
		kll=ReadFile(par['fi'],par['cnt'],par['cert'],par['dl'],par['pre'])
	if kll != None:
		hs=hs+kll
	PrintStat(hs)
		
if __name__ == "__main__":
	main(sys.argv)
	