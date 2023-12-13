import sys

from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QMainWindow, QApplication



class MapWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        lat = "59.4069278"
        lng = "17.9455545"
        html_content = f"""
        <html>
        <body>
        <div id="map" style="width: 100%; height: 100%;"></div>
        <script>
          function initMap() {{
            var location = {{lat: {lat}, lng: {lng}}};
            var map = new google.maps.Map(document.getElementById('map'), {{
              zoom: 15,
              center: location
            }});
            var marker = new google.maps.Marker({{
              position: location,
              map: map,
              icon: 'http://maps.google.com/mapfiles/ms/icons/red-dot.png'
            }});
          }}
        </script>
        <script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyBtuPn-649uIBsd80KfCpVr3pBLERtO3gw
&callback=initMap" async defer></script>
        </body>
        </html>
        """

        self.webview = QWebEngineView()
        self.webview.setHtml(html_content)
        self.setCentralWidget(self.webview)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MapWindow()
    window.show()
    sys.exit(app.exec_())
