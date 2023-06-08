from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import json
# urllib.request to make a request to api
import urllib.request


def index(request):

	if request.method == 'POST':
		city = request.POST['city']
		''' api key might be expired use your own api_key
			place api_key in place of appid ="your_api_key_here " '''

		# source contain JSON data from API
		start_url = 'http://api.openweathermap.org/data/2.5/weather?q ='+ city +'&appid =f23cee21fd0fe489cf8789bf86ed3c3a'
		url = start_url.replace(" ", "")
		source = urllib.request.urlopen(url).read()



		# converting JSON data to a dictionary
		list_of_data = json.loads(source)

		# data for variable list_of_data
		data = {"city":city,
			"country_code": str(list_of_data['sys']['country']),
			"coordinate": str(list_of_data['coord']['lon']) + ' '
						+ str(list_of_data['coord']['lat']),
		    "temp": str(list_of_data['main']['temp']) + 'k',
			"pressure": str(list_of_data['main']['pressure']),
			"humidity": str(list_of_data['main']['humidity']),
		}
		print(data)
	else:
		data ={}
	return render(request, "main/index.html", data)

