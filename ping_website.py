#importing the necessary libraries
import subprocess

def ping(host):
    #using the built-in ping command on Windows
    ping = subprocess.Popen(
    ["ping", "-n", "1", host],
    stdout = subprocess.PIPE,
    stderr = subprocess.PIPE
)
    #checking if "reply" exists in the response
    out, error = ping.communicate()
    if "Reply" in str(out):
        return "Successful"
    else:
        return "Unsuccessful"
print(ping("www.google.com"))
