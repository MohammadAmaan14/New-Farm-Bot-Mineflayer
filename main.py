import subprocess
import datetime

# Function to run the Node.js script and capture both stdout and stderr
def run_nodejs():
    try:
        process = subprocess.Popen(['node', 'index.js'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True, bufsize=1, text=True)
        with open('console_log.txt', 'a') as log_file:
            for line in process.stdout:
                log_file.write(f'{datetime.datetime.now()} [STDOUT] {line}')
                log_file.flush()
                print(f'{datetime.datetime.now()} [STDOUT] {line}', end='')
                
            for line in process.stderr:
                log_file.write(f'{datetime.datetime.now()} [STDERR] {line}')
                log_file.flush()
                print(f'{datetime.datetime.now()} [STDERR] {line}', end='')
    except Exception as e:
        print(f'{datetime.datetime.now()} [ERROR] An error occurred: {str(e)}')

# Rest of the code...

# Run the Node.js script and capture messages
run_nodejs()

# Rest of the code...
