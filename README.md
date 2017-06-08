# Time_Response_Analyzer
Timing Analysis v1.0.0 
Automatized toll for serialized timing side channel attacks on a remote webserver plus fuzzer

## Dependencies

This packet depends on requests for http connections and  prettytable for visually formatting ASCII tables.
Install them using 
```
pip install prettytable requests

```

## Usage
Start:
```
python side.py
```
Commands:

```
-h 			Print help.

-r <file_name> 		Read from file the targets.

-c <counter> 		Specify the number of requests (default:10).

-d <sec>		Wait <sec> between each request.

-u <url> 		Sending the request at this URL.

--data <raw_data> 	Using this data as body of teh request.

--header <raw_header>	Insert this header in the request.

--method <method>	Use selected method (default GET).Allowed methods:
			GET,POST,PUT,DELETE,OPTIONS,HEAD

--proxy <address:port>  Tunnel through proxy (NOT YET IMPLEMENTED)

--precision <decimal>	Number of decimals in statistics

--nc 			Disable certificate verfication.


-f 			Activate the fuzzer mode.

--dict <dictionary>     Dictionary file to fuzz.

--escape <char> 	Escape character (default '$')
```

## TODO and contributions

- [ ] Implement the Proxy connection : this should be done properly.
      You should add a testing server were the connection time is knwon,
      so that you know the average lag between you and the proxy, 
      and subtract it from the connection request time.

- [ ] Add more statistics : now we the only metrics included are:
      Min Max Avg Time  and Std deviation.
