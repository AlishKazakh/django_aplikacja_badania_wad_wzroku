import sys
from PyQt5.QtWidgets import QApplication, QCalendarWidget


def calculate_dpi():
    app = QApplication(sys.argv)

    screen = app.screens()[0]
    screen.devicePixelRatio()
    dpi = screen.physicalDotsPerInch()
    return dpi


def calculate_pixel_ratio():
    app = QApplication(sys.argv)
    screen = app.screens()[0]
    ratio = screen.devicePixelRatio()

    return ratio
