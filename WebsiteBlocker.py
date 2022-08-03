from datetime import datetime              # We don't need to import as it is builtin
end_time = datetime(2022,8,5)             # time when our websites will be unblocked
url = "www.wikepedia.com"
hosts_path = "C:/Windows/System32/drivers/etc/hosts"       # This is the file where we put the ip address and the url in order to block it
redirect = "127.0.0.1"

def block_sites(url):
    if datetime.now() < end_time: 
        with open(hosts_path, 'r+') as hostfile:
            hosts_content = hostfile.read()    # here the information is put into one string
            if url not in hosts_content:
                hostfile.write(redirect + " " + url + "\n")
                print(url + " Site blocked")
                
                    


# if __name__ == "__main__":
#     block_sites()       





            

