import requests
import time
from host import Host

def SendData(method,url,hd=None,dt=None,cnt=10,cert=False,delay=None):
	i=0
	exp=[]
	print method+" "+url
	while i < cnt:
		t=time.clock()
		if method=='GET':
			r=requests.get(url,headers=hd,data=dt, verify=cert)
		elif method=='POST':
			r=requests.post(url,headers=hd,data=dt, verify=cert)
		elif method=='HEAD':
			r=requests.head(url,headers=hd,data=dt, verify=cert)
		elif method=='OPTIONS':
			r=requests.options(url,headers=hd,data=dt, verify=cert)
		elif method=='DELETE':
			r=requests.delete(url,headers=hd,data=dt, verify=cert)
		elif method=='PUT':
			r=requests.put(url,headers=hd,data=dt, verify=cert)
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
		if line == "\n":
			if (bd==False):
				bd=True
			else:
				g=SendData(method,url,header,body,cnt,cert,delay)
				k=Host(method,url,header,body,cnt,g,prec)
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
	
	g=SendData(method,url,header,body,cnt,cert,delay)
	k=Host(method,url,header,body,cnt,g,prec)
	arr.append(k)
	return arr