# pymonzo-auth
Authenticating using PyMonzo to create a token

# Setting up Monzo API Access
* Go to [https://developers.monzo.com](https://developers.monzo.com/) and sign in
* Click on 'Clients' in the bar at the top
* Create a 'New OAuth Client'
* Set 'Redirection URLs' to be `http://127.0.0.1:8080/monzo/auth`. The other settings can be whatever you want them to be.
* Add the client secret and client id to the `api_info.conf` file

# How to use
* Run `authenticate.py`.
* Open the link it generates in your web browser
* Authenticate through the website and go to your emails to get the link
* Click the link in your email and `authenticate.py` authenticate to the Monzo API and exit cleanly.

You should now have setup pymonzo with a token ready to continue your development! 

# api_info.conf
The api_info.conf file just stores the secret and id that are required to access the API. There is `api_info.conf.example` which you can use as a guide to create this file.

# Tested
Tested on Windows 10, and macOS sierra using Python 2.7. I have tested this against version `pymonzo 0.10.0`

# Useful Links
* pymonzo - [pawelad @ GitHub](https://github.com/pawelad/pymonzo)
* Simple HTTP server - [trungly @ GitHub](https://gist.github.com/trungly/5889154)
* Killing the server from within - [jhermann @ stackoverflow](https://stackoverflow.com/questions/19040055/how-do-i-shutdown-an-httpserver-from-inside-a-request-handler-in-python)
