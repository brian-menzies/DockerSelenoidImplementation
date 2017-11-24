from Helpers.BaseTest import GetConfig
import subprocess

# Import the Access Key and the Secret Key from your Config.xml file
aws_access = GetConfig('AWS_ACCESS_KEY')
aws_secret = GetConfig('AWS_SECRET_KEY')

region_name = GetConfig('REGION_NAME')
output_format = GetConfig('DEFAULT_OUTPUT_FORMAT')


# Verify that the Main Selenoid Instance is Up and Running
print("Pressing Enter Key")
# Types in a Command into the Terminal and runs the command as stated.
# Does not interact with user input as far as I know
subprocess.call('pip install hotdog -U')
print("done in console")


# If it isn't, Attempt to Start the Machine and Wait to see if it begins running


#
