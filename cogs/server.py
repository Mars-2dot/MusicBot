from flask import Flask
import os
import platform

app = Flask(__name__)


def ping_host(host):
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    response = os.system(f"ping {param} 1 {host}")
    return response == 0


@app.route('/check-services', methods=['GET'])
def check_services():
    youtube_ok = ping_host('www.youtube.com')
    discord_ok = ping_host('www.discord.com')

    if youtube_ok and discord_ok:
        return "ok"
    else:
        return "failure", 503


def run_server():
    app.run(port=5001, debug=False, use_reloader=False, host='0.0.0.0')
