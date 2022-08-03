from flask import Flask, redirect, url_for, request
app = Flask(__name__)

from datetime import datetime            
end_time = datetime(2022,8,5)             # time when our websites will be unblocked
#url = "www.wikepedia.com"
hosts_path = "C:/Windows/System32/drivers/etc/hosts"       # This is the file where we put the ip address and the url in order to block it
redirect = "127.0.0.1"

def block_sites(url):
    url = url[8:]
    if datetime.now() < end_time: 
        with open(hosts_path, 'r+') as hostfile:
            hosts_content = hostfile.read()    # here the information is put into one string
            if url not in hosts_content:
                hostfile.write(redirect + " " + url + "\n")
                print(url + " Site blocked") 

@app.route('/login')
def success(url):
    block_sites(url)
    return 'Website blocked'
 
 
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['loginUser']
        return redirect(url_for('success', name=user))
    else:
        user = request.args.get('loginUser')
        return redirect(url_for('success', name=user))


 
 
if __name__ == '__main__':
    app.run(debug=True) 

@app.route()