import subprocess
import threading
import datetime

# Function to run the Node.js script and capture both stdout and stderr
def run_nodejs():
    with open('console_log.txt', 'a') as log_file:
        process = subprocess.Popen(['node', 'index.js'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        for line in process.stdout:
            log_line = f'{datetime.datetime.now()} [STDOUT] {line}'
            print(log_line, end='')
            log_file.write(log_line)
        for line in process.stderr:
            log_line = f'{datetime.datetime.now()} [STDERR] {line}'
            print(log_line, end='')
            log_file.write(log_line)

# Function to run the Python script for logging messages
def run_python():
    subprocess.run(['python', 'log_messages.py'])

# Create threads for running both scripts
nodejs_thread = threading.Thread(target=run_nodejs)
python_thread = threading.Thread(target=run_python)

# Start both threads
nodejs_thread.start()
python_thread.start()

# Wait for both threads to finish
nodejs_thread.join()
python_thread.join()

print("Both scripts have finished executing.")
