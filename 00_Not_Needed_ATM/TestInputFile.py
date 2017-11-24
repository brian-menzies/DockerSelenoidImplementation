import subprocess

subprocess.call("git add .")

input_message = input("Please enter your Commit Message: ")
subprocess.call("commit -m " + input_message)