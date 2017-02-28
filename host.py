class Host:
	def __init__(self,method,url,header,body,counter,time,prec):
		self.method=method
		self.first=True
		stt=url.find('?')
		if stt == -1:
			self.url=url
		else:
			self.url=url[:stt]
		self.header=header
		self.body=body
		self.cnt=counter
		self.time=time
		self.prec=prec
	
	def statistics(self):
		self.max=0
		self.min=9223372036854775807
		sum=0
		sqr=0
		for i in self.time:
			sum+=i
			sqr+=(i*i)
			if i > self.max:
				self.max=i
			if i < self.min:
				self.min=i
		
		self.avg=sum/self.cnt
		'''
		sum=0
		for i in self.time:
			sum+=pow((i-self.avg),2)
		self.sqm=sum
		'''
		self.sqm=sqr-pow(self.avg,2)*self.cnt
	def value(self):
		ret=[]
		ret.append(self.method)
		ret.append(self.url)
		ret.append(self.cnt)
		ret.append(round(self.min,self.prec))
		ret.append(round(self.max,self.prec))
		ret.append(round(self.avg,self.prec))
		ret.append(round(self.sqm,self.prec))
		return ret