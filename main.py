'''
import requests



def get_gps():
    latitude = 59.3991064
    longitude = 17.92282
    return latitude, longitude


def generate_static_map(api_key, latitude, longitude, marker_color="red"):
    marker = f"color:{marker_color}%7C{latitude},{longitude}"
    url = f"https://maps.googleapis.com/maps/api/staticmap?center={latitude},{longitude}&zoom=15&size=720x400&markers={marker}&key={api_key}"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses
    except requests.exceptions.RequestException as e:
        print(f"Error making the request: {e}")
        return

    with open("static_map_with_marker.png", "wb") as f:
        f.write(response.content)
        print("Static map with marker saved as static_map_with_marker.png")


api_key = "AIzaSyBtuPn-649uIBsd80KfCpVr3pBLERtO3gw"
latitude, longitude = get_gps()
generate_static_map(api_key, latitude, longitude)
'''
import tkinter as tk
import webbrowser

def get_gps():
    latitude = 59.4067225
    longitude = 17.9426422
    return latitude, longitude

def generate_html(lat, lng):
    html_content = f"""
    <html>
    <body>
    <div id="map" style="width: 1600px; height: 720px;"></div>
    <script>
      function initMap() {{
        var location = {{lat: {lat}, lng: {lng}}};
        var map = new google.maps.Map(document.getElementById('map'), {{
          zoom: 16,
          center: location
        }});
        var marker = new google.maps.Marker({{
          position: location,
          map: map,
          icon: 'http://maps.google.com/mapfiles/ms/icons/red-dot.png'
        }});
      }}
      // 调用 show_map 函数
      function show_map() {{
        initMap();
      }}
    </script>
    <script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyBtuPn-649uIBsd80KfCpVr3pBLERtO3gw&callback=show_map" async defer></script>
    </body>
    </html>
    """
    with open("map.html", "w") as f:
        f.write(html_content)

def show_map():
    webbrowser.open("map.html")

root = tk.Tk()
root.title("Map")

button_show_map = tk.Button(root, text="Show", command=show_map)
button_show_map.pack()

generate_html(*get_gps())

root.mainloop()





