import requests
import time
from host import Host

def SendData(host,delay,cnt,cert):
	i=0
	exp=[]
	print host.method+" "+host.urlt
	while i < cnt:
		t=time.clock()
		if host.method=='GET':
			r=requests.get(host.urlt,headers=host.header,data=host.body, verify=cert)
		elif host.method=='POST':
			r=requests.post(host.urlt,headers=host.header,data=host.body, verify=cert)
		elif host.method=='HEAD':
			r=requests.head(host.urlt,headers=host.header,data=host.body, verify=cert)
		elif host.method=='OPTIONS':
			r=requests.options(host.urlt,headers=host.header,data=host.body, verify=cert)
		elif host.method=='DELETE':
			r=requests.delete(host.urlt,headers=host.header,data=host.body, verify=cert)
		elif host.method=='PUT':
			r=requests.put(host.urlt,headers=host.header,data=host.body, verify=cert)
		t1=time.clock()
		exp.append(t1-t)
		print "\tRequest #:"+str(i+1)+"\tReply status code:"+str(r.status_code)+"\tTime:"+str(t1-t)
		i+=1
		if delay!=None:
			time.sleep(delay)
	return exp


def ReadFile(name,cnt,cert,delay,prec):
	f=open(name,"r")
	arr=[]
	bd=False

	for line in f:
		opt=line.split()
		if line == "\n" or len(opt) == 0:
			if (bd==False):
				bd=True
			else:
				k=Host(method,url,header,body,cnt,prec)
				arr.append(k)
				bd=False
		elif opt[0]=="GET" or opt[0]=="POST" or opt[0]=="HEAD" or opt[0]=="OPTIONS" or opt[0]=="PUT" or opt[0]=="DELETE":
			method=opt[0]
			url=opt[1]
			header={}
			body=""
		else:
			if bd==False:
				i=1
				str=""
				while i < len(opt):
					if i == len(opt)-1:
						str=str+opt[i]
					else:
						str=str+opt[i]+" "
					i+=1
				header[opt[0].replace(":","")]=str
			else:
				body+=line

	k=Host(method,url,header,body,cnt,prec)
	arr.append(k)
	'''
	for i in arr:
		g=SendData(i,delay,cnt,cert)
		i.time=g
	'''
	return arr
