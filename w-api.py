import urllib, json
city_name = raw_input("What city would you like to know more about? " )

api_url = "http://api.openweathermap.org/data/2.5/weather?q=%s&units=imperial" % urllib.quote(city_name)
json_tree = json.loads( urllib.urlopen(api_url).read() )
print "It is %s degrees in %s." %(json_tree["main"]["temp"], city_name)
