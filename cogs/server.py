import subprocess

from flask import Flask
import logging
import os
import platform

app = Flask(__name__)

def ping_host(host):
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = f"ping {param} 1 {host}"

    try:
        response = subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return response.returncode == 0
    except Exception as e:
        print(f"An error occurred: {e}")
        return False


@app.route('/check-services', methods=['GET'])
def check_services():
    youtube_ok = ping_host('www.youtube.com')
    discord_ok = ping_host('www.discord.com')

    if youtube_ok and discord_ok:
        return "ok"
    else:
        return "failure", 503


def run_server():
    log = logging.getLogger('werkzeug')
    log.setLevel(logging.ERROR)
    app.run(port=5001, debug=False, use_reloader=False, host='0.0.0.0')
