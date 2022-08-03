import datetime
import time

closing_time=datetime.datetime(2022,8,19) 
# update the closing time according to the needs
# sites mentioned here only for testing purpose
blocking_sites=["www.banggood.in","www.alibaba.com"] 
host_path= "C:/Windows/System32/drivers/etc/hosts"
host_ip="127.0.0.1"

while datetime.datetime.now()<closing_time :
        print("Websites blocking executed")
        with open(host_path,'r+') as host_file:
            content= host_file.read()
            for website in blocking_sites:
                if website not in content:
                    host_file.write(host_ip+" "+website+"\n")
                
        time.sleep(60)

else:
        print("Websites Unblocked")
        with open(host_path,'r+') as host_file:
            content=host_file.readlines()
            host_file.seek(0)
            for lines in content:
                if not any( website in lines for website in blocking_sites):
                    host_file.write(lines)
            host_file.truncate() 
          
             
        
                
