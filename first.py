from influxdb import InfluxDBClient
	
import random
series=['1','2','3']
for i in (series):
		print i	
		
		jsonBody = [
		{
        		 "measurement": "cpu1",
       	 	 'tags': {
        		     "host": "server02",
             
       	 	 },
       	  	'fields': {
       	  	 	'first':i,
			
			
       	  	},
     	}
	]	 		
series.append(jsonBody)
client = InfluxDBClient('localhost', 8086,'admin','admin', 'dutt')
client.write_points(jsonBody)
