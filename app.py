import subprocess
from flask import Flask, render_template, request

app = Flask(__name__)

def get_host_name():
    try:
        import socket
        host_name = socket.gethostname()
        return host_name
    except Exception as e:
        return f"Unable to get Hostname: {str(e)}"

def get_host_ip():
    try:
        import socket
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        return host_ip
    except Exception as e:
        return f"Unable to get IP: {str(e)}"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/display', methods=['POST'])
def display():
    choice = request.form.get('choice')
    if choice == '1':
        result = get_host_ip()
    elif choice == '2':
        result = get_host_name()
    elif choice == '3':
        try:
            # Specify full path to lmutil executable
            lmutil_command = r'D:\M\FlexLM_11_13_1_2\lmutil.exe'

            # Run lmutil command to generate lic.txt
            subprocess.run([lmutil_command, "lmstat", "-a", "-c", "27000@localhost"], shell=True)
            
            # Read the contents of lic.txt
            with open("lic.txt", "r") as file:
                result = file.read()
        except Exception as e:
            result = f"Error executing command: {str(e)}"
    else:
        result = "Invalid choice"
    return render_template('display.html', result=result)

if __name__ == "__main__":
    app.run(debug=True)
