from flask import Flask, request, render_template
from datetime import datetime
import user_agents
import csv
import os
import pytz  # al inicio del archivo

app = Flask(__name__)

@app.route('/')
def index():
    ip_address = request.remote_addr
    user_agent = user_agents.parse(request.headers.get('User-Agent'))
    browser = f"{user_agent.browser.family} {user_agent.browser.version_string}"
    operating_system = f"{user_agent.os.family} {user_agent.os.version_string}"
    device = user_agent.device.family or "Desconocido"

    tz_mx = pytz.timezone('America/Mexico_City')
    access_time = datetime.now(tz_mx).strftime('%Y-%m-%d %H:%M:%S')


    # Registrar datos en un archivo CSV
    csv_file = 'registro_visitas.csv'
    file_exists = os.path.isfile(csv_file)

    with open(csv_file, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(['Hora de acceso', 'IP', 'Navegador', 'Sistema Operativo', 'Dispositivo'])
        writer.writerow([access_time, ip_address, browser, operating_system, device])

    return render_template('info.html',
                           ip=ip_address,
                           browser=browser,
                           os=operating_system,
                           device=device,
                           access_time=access_time)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


