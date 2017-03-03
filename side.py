import requests
import time
from prettytable import PrettyTable
import sys, getopt
from cmdopt import *
from network import *
from collections import namedtuple


def PrintStat(array):
	print "\n\n"
	t = PrettyTable(['Method', 'URL','# Request','MIN','MAX','AVG','RSD'])
	for i in array:
		i.statistics()
		t.add_row(i.value())

	print t

def escapeIndex(str,escape):
	star=-1
	st=0
	while st < len(str):
		st=str.find(escape, st+1,len(str))
		if st!=-1:
			if star == -1:
				star=st
			else:
				pt=[star+1, st]
				return pt
		else:
			st==-1
			break
	return None

def Fuzz(host,fz,escape,ret):
	pt=escapeIndex(host.urlt,escape)
	if pt is not None:
		for item in fz:
			newone=host.urlt[:pt[0]-1]+item+host.urlt[pt[1]+1:]
			nv=Host(host.method,newone,host.header,host.body,host.cnt,host.prec)
			#Recursion
			Fuzz(nv,fz,escape,ret)
			#print "URL:"+nv.urlt
	#HEADER DOPO
	else:
		pt=escapeIndex(host.body,escape)
		if pt is not None:
			for item in fz:
				#Devo modificare il body
				newone=host.body[:pt[0]-1]+item+host.body[pt[1]+1:]
				nv=Host(host.method,host.urlt,host.header,newone,host.cnt,host.prec)
				#Recursion
				Fuzz(nv,fz,escape,ret)
		else:
			ret.append(host)



def main(argv):
	par=ParseOpt(argv)
	print "Timing analysis v1.0.0 - A tool for timing side-channel analysis.\n\n"
	hs=[]
	fz=[]
	kll=None

	if par['fuzz']==True:
		if par['dict'] is None:
			print "Error. Define a dictionary file using '--dict option'."
			sys.exit()
		f=open(par['dict'])
		for line in f:
			fz.append(line.strip())

	if par['url'] != None:
		hd=None
		if par['hd'] != None:
			hd={}
			for i in par['hd']:
				d=i.split(':')
				hd[d[0].strip()]=d[1].strip()
		k=Host(par['md'],par['url'],hd,par['dt'],par['cnt'],par['pre'])
		hs.append(k)
	if par['fi'] != None:
		kll=ReadFile(par['fi'],par['cnt'],par['cert'],par['dl'],par['pre'])

	if kll != None:
		hs=hs+kll

	if par['fuzz'] == True:
		tot=[]
		for host in hs:
			nn=[]
			Fuzz(host,fz,par['escape'],nn)
			tot+=nn
	else:
		tot=hs
	for i in tot:
#		Sending Data
		t=SendData(i,par['dl'],par['cnt'],par['cert'])
		i.time=t

	PrintStat(tot)

if __name__ == "__main__":
	main(sys.argv)
