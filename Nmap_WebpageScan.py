import sys
import nmap
from PyQt5 import QtWidgets, QtWebEngineWidgets


# Scan function.
def scan_website():
    url = web.view.url().toString()
    nmap_portscan = nmap.PortScanner()
    nmap_portscan.scan(url)
    print(nmap_portscan())


# Main window and a web view.
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QMainWindow()
web_view = QtWebEngineWidgets.QWebEngineView()

# Create Scan button.
scan_button = QtWidgets.QPushButton('Scan')
scan_button.clicked.connect(scan_website)

# Let's make a layout ya'll
layout = QtWidgets.QVBowLayout()
layout.addWidget(web_view)
layout.addWidget(scan_button)

window.setLayout(layout)
window.show()


sys.exit(app.exec_())

# Fuck me in the arse, cuz this code is not working one bit!
