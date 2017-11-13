import urllib # Python URL functions
import urllib2 # Python URL functions

authkey = "" # Your authentication key.

mobiles = "" # Multiple mobiles numbers separated by comma.

message = "Test message" # Your message to send.

sender = "112233" # Sender ID,While using route4 sender id should be 6 characters long.

route = "4" # Define route

# Prepare you post parameters
values = {
          'authkey' : authkey,
          'mobiles' : mobiles,
          'message' : message,
          'sender' : sender,
          'route' : route
          }


url = "http://api.msg91.com/api/sendhttp.php" # API URL

postdata = urllib.urlencode(values) # URL encoding the data here.

req = urllib2.Request(url, postdata)

response = urllib2.urlopen(req)

output = response.read() # Get Response

print output # Print Response