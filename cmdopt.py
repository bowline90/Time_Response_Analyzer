import sys, getopt

def Usage(name):
	print "Timing analysis v1.0.0 - A tool for timing side-channel analysis."
	print "Usage: "+name
	print "\t-h \t\t\tPrint this help."
	print "\t-r <file_name>\t\tRead from file the targets."
	print "\t-c <counter>\t\tSpecify the number of request (default:10)."
	print "\t-d <sec>\t\tWait <sec> between a request and anothers."
	print "\t-u <url>\t\tSending the request at this url."
	print "\t--data <raw_data>\tUsing this data as body of the request."
	print "\t--header <raw_header>\tInsert this header in the request."
	print "\t--method <method>\tUse this method (default GET).\n\t\t\t\tThe method allowed are: GET, POST, PUT, DELETE, OPTIONS, HEAD."
	print "\t--proxy <address:port>\tSend the requests througth this proxy. (Not yet implemented)"
	print "\t--precision <decimal>\tNumber of decimal in statistics."
	print "\t--nc\t\t\tDisable certificate verification."
	print "\n"
	print "\t-f\t\t\tActivate the fuzzer mode."
	print "\t--dict <dictionary>\tDictionary file to fuzz (mandatory in fuzz mode)."
	print "\t--escape <char>\t\tEscape character (default '$')."
		

def ParseOpt(argv):
	settings={}
	settings['fi']=None
	settings['cnt']=10
	settings['dl']=None
	settings['url']=None
	
	settings['data']=None
	settings['hd']=None
	settings['dt']=None
	settings['md']="GET"
	settings['pxy']=None
	settings['pre']=5
	settings['cert']=True
	
	settings['fuzz']=False
	settings['dict']=None
	settings['escape']='$'
	
	
	try:
		opts, args = getopt.getopt(argv[1:],"hfr:c:d:u:",["data=","header=","method=","proxy=","precision=","dict=","escape=","nocert"])
	except getopt.GetoptError:
		Usage(argv[0])
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			Usage(argv[0])
			sys.exit()
		elif opt in ("-r"):
			inputfile = arg.strip()
			settings['fi']=inputfile
		elif opt in ("-c"):
			try:
				counter = int(arg)
			except:
				Usage(argv[0])
				sys.exit()
			settings['cnt']=counter
		elif opt in ("-d"):
			try:
				delay = int(arg)
			except:
				Usage(argvd[0])
				sys.exit()
			settings['dl']=delay
		elif opt in ("-u"):
			url = arg
			settings['url']=url
		elif opt in ("-f"):
			settings['fuzz']=True
		elif opt in ("--data"):
			data = arg
			settings['dt']=data
		elif opt in ("--header"):
			header = arg
			if settings['hd'] == None:
				settings['hd'] = []
			settings['hd'].append(header)
		elif opt in ("--method"):
			method = arg
			settings['md']=method
		elif opt in ("--proxy"):
			proxy = arg
			settings['pxy']=proxy
		elif opt in ("--precision"):
			try:
				prec = int(arg)
			except:
				Usage(argv[0])
				sys.exit()
			settings['pre']=prec
		elif opt in ("--nocert"):
			settings['cert']=False
		elif opt in ("--dict"):
			settings['dict']=arg
		elif opt in ("--escape"):
			settings['escape']=arg
	return settings