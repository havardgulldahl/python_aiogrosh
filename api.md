Our test server is running at the endpoint https://groshapp.com/edge and John Does credentials are:
Username: ***
Password: ***
Use basic authentication on the request headers to get access to the APIs, e.g. if using jQuery

$.ajax({
type: "GET",
url: "https://groshapp.com/edge/users/me/households",
async: false,
headers: {
"Authorization": "Basic " + btoa(USERNAME + ":" +PASSWORD)
},

You may try out the APIs in a web browser before you write your program, e.g.
https://groshapp.com/edge/users/me/households This will tell you authentication is missing, add ?www to
the end of the URL to make the browser prompt you for this.

To get items from list:
https://groshapp.com/edge/households/{id}/current