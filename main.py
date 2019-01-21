import os
from flask import Flask
app = Flask(__name__)

@app.route('/blockv4/<ip>')
def blockv4(ip):
    cmd = 'iptables -A OUTPUT -d %s -j REJECT' %ip
    try:
        os.system(cmd)
        return cmd
    except Exception as e:
        return str(e)


@app.route('/blockv6/<ip>')
def blockv6(ip):
    cmd = 'ip6tables -A OUTPUT -d %s -j REJECT' %ip
    try:
        os.system(cmd)
        return cmd
    except Exception as e:
        return str(e)
