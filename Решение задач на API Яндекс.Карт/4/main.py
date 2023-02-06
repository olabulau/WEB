import sys

from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, \
    QLineEdit, QMainWindow, QPushButton
import requests
from requests.adapters import HTTPAdapter
from urllib3 import Retry


class MainWindow(QMainWindow):
    g_map: QLabel
    g_search: QLineEdit
    g_layer1: QPushButton
    g_layer2: QPushButton
    g_layer3: QPushButton
    press_delta = 5

    def __init__(self):
        super().__init__()
        uic.loadUi('main_window.ui', self)
        self.map_zoom = 5
        self.map_ll = [37.977751, 55.757718]
        self.map_l = 'map'
        self.map_key = ''
        self.map_point = ''

        # noinspection PyUnresolvedReferences
        self.g_search.returnPressed.connect(self.search)
        self.g_layer1.clicked.connect(self.set_layer1)
        self.g_layer2.clicked.connect(self.set_layer2)
        self.g_layer3.clicked.connect(self.set_layer3)

        self.refresh_map()

    def set_layer1(self):
        self.map_l = 'map'
        self.refresh_map()

    def set_layer2(self):
        self.map_l = 'sat'
        self.refresh_map()

    def set_layer3(self):
        self.map_l = 'sat,skl'
        self.refresh_map()

    def keyPressEvent(self, event):
        key = event.key()

        if key == Qt.Key_PageUp:
            if self.map_zoom < 17:
                self.map_zoom += 1
        elif key == Qt.Key_PageDown:
            if self.map_zoom > 0:
                self.map_zoom -= 1

        elif key == Qt.Key_Escape:
            self.g_map.setFocus()

        elif key == Qt.Key_Right:
            self.map_ll[0] += self.press_delta
            if self.map_ll[0] > 180:
                self.map_ll[0] = self.map_ll[0] - 360
        elif key == Qt.Key_Left:
            self.map_ll[0] -= self.press_delta
            if self.map_ll[0] < 0:
                self.map_ll[0] = self.map_ll[0] + 360
        elif key == Qt.Key_Up:
            if self.map_ll[1] + self.press_delta < 90:
                self.map_ll[1] += self.press_delta
        elif key == Qt.Key_Down:
            if self.map_ll[1] - self.press_delta > -90:
                self.map_ll[1] -= self.press_delta
        else:
            return

        self.refresh_map()

    def refresh_map(self):
        map_params = {
            "ll": f'{self.map_ll[0]},{self.map_ll[1]}',
            "l": self.map_l,
            'z': self.map_zoom,
        }
        if self.map_point:
            map_params['pt'] = self.map_point
        response = make_request('https://static-maps.yandex.ru/1.x/', params=map_params)
        if not response:
            print('error: could not get map')
            return
        with open('tmp.png', mode='wb') as tmp:
            tmp.write(response.content)

        pixmap = QPixmap()
        pixmap.load('tmp.png')

        self.g_map.setPixmap(pixmap)

    def search(self):
        x, y = geo_locate(self.g_search.text())
        if x == -1 or y == -1:
            return
        self.map_ll = [x, y]
        self.map_point = f'{x},{y},comma'
        self.refresh_map()


def geo_locate(name):
    params = {
        'apikey': '40d1649f-0493-4b70-98ba-98533de7710b',
        'geocode': name,
        'format': 'json'
    }
    response = make_request('http://geocode-maps.yandex.ru/1.x/', params=params)
    if not response:
        print(f'error: could not get geo_locate object {name}')
        return -1, -1
    geo_objects = response.json()['response']["GeoObjectCollection"]["featureMember"]
    if not geo_objects:
        print('error: could not get geo_objects')
        return -1, -1
    return list(map(float, geo_objects[0]["GeoObject"]["Point"]["pos"].split()))


def make_request(*args, **kwargs):
    session = requests.Session()
    retry = Retry(total=10, connect=5, backoff_factor=0.5)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    return session.get(*args, **kwargs)


def clip(v, _min, _max):
    if v < _min:
        return _min
    if v > _max:
        return _max
    return v


app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
sys.exit(app.exec())
