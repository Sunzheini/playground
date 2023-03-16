"""
200 – OK. The request was successful. The answer itself depends on the method 
used (GET, POST, etc.) and the API specification.
204 – No Content. The server successfully processed the request and did not 
return any content.
301 – Moved Permanently. The server responds that the requested page (endpoint) 
has been moved to another address and redirects to this address.
400 – Bad Request. The server cannot process the request because the client-side 
errors (incorrect request format).
401 – Unauthorized. Occurs when authentication was failed, due to incorrect 
credentials or even their absence.
403 – Forbidden. Access to the specified resource is denied.
404 – Not Found. The requested resource was not found on the server.
500 – Internal Server Error. Occurs when an unknown error has occurred on the server.

"""
import requests

url = "https://google-translate1.p.rapidapi.com/language/translate/v2/detect"

payload = "q=English%20is%20hard%2C%20but%20detectably%20so"
headers = {
	"content-type": "application/x-www-form-urlencoded",
	"Accept-Encoding": "application/gzip",
	"X-RapidAPI-Key": "9eee0d615fmsh414ace264454d8ap14a435jsn486edea4b81e",
	"X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
}

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
