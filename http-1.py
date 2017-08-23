import urllib.request
import json
import urllib.parse

def searchMovie():
    title = "dangal"
    url = "http://www.omdbapi.com/?t=%s" % urllib.parse.quote(title)
    try:
        conn = urllib.request.urlopen(url)
    except:
        print("Failure in connecting to IMDB")
        return

    print("Headers: ")
    for k, v in conn.getheaders():
        print(k, v)

    print(" ")

    jdata = conn.read()
    try:
        str_data = jdata.decode('utf8')
        print("str_data: ", str_data)
        print(" ")
        js_data2 = json.dumps(str_data, sort_keys=True, indent=2)
        print("js_data2: ", js_data2)
        print(" ")

        js_data  = json.loads(str_data)
        print("Title: ", js_data['Title'])
        print("Year: ", js_data['Year'])
        print("Plot: ", js_data['Plot'])
        print("Actors: ", js_data['Actors'])
    except:
        print("Sorry, no data found for movie")
        return
    

searchMovie()

    
