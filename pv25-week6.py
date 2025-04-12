import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QMainWindow
from sliderUI_ui import Ui_MainWindow

class MainUI(QMainWindow):
    def __init__(self):
        super(MainUI, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Font Size and Color Adjuster")

        # Set min max value
        self.ui.Slider1.setMinimum(20)
        self.ui.Slider1.setMaximum(60)
        self.ui.Slider2.setMinimum(0)
        self.ui.Slider2.setMaximum(255)
        self.ui.Slider3.setMinimum(0)
        self.ui.Slider3.setMaximum(255)

        self.ui.Slider1.setValue(20)
        self.ui.Slider2.setValue(255)
        self.ui.Slider3.setValue(0)
       
        self.ui.Slider1.setTickPosition(QSlider.TicksBelow)
        self.ui.Slider2.setTickPosition(QSlider.TicksBelow)
        self.ui.Slider3.setTickPosition(QSlider.TicksBelow)

        self.ui.Slider1.valueChanged.connect(self.rezise_font)
        self.ui.Slider2.valueChanged.connect(self.changeBGColor)
        self.ui.Slider3.valueChanged.connect(self.changeFontColor)

    def rezise_font(self):
        font_size = self.ui.Slider1.value()
        font = self.ui.label.font()
        font.setPointSize(font_size)
        self.ui.label.setFont(font)

    def changeBGColor(self):
        colorBG = self.ui.Slider2.value()
        currentStyle = self.ui.label.styleSheet()
        self.ui.label.setStyleSheet(f"{currentStyle} background-color: rgb({colorBG}, {colorBG}, {colorBG});")

    def changeFontColor(self):
        fontColor = self.ui.Slider3.value()
        currentStyle = self.ui.label.styleSheet()
        self.ui.label.setStyleSheet(f"{currentStyle} color: rgb({fontColor}, {fontColor}, {fontColor});")
       

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainUI()
    window.show()
    sys.exit(app.exec_())