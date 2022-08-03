from flask import Flask, redirect, render_template, url_for, request
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
                return url + " Site blocked"

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template("index.html")



@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form.get('loginUser')
        url = request.form.get('loginPassword')
        message = "<p>"+block_sites(url)+"</p>"
        return message
    return render_template("login.html")


 
 
if __name__ == '__main__':
    app.run(debug=True) 