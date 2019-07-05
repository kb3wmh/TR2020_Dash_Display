import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from diagwindow import Ui_MainWindow
import time
import random
import _thread as thread

def rpmController(ui):
    i = 0
    delta = 20

    while True:
        ui.rpm_lcdnumber.display(i)
        i = i + delta

        if i <= 0:
            delta = 20

        elif i >= 12800:
            delta = -20

        time.sleep(.1)

def engine_temp_controller(ui):
    while True:
        i = random.randint(195, 205)
        ui.engine_temp_lcdnumber.display(i)
        time.sleep(5)
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(window)

    window.show()

    try:
        thread.start_new_thread( rpmController, (ui,))
        thread.start_new_thread( engine_temp_controller, (ui,))
        
    except:
        print ("Error creating threads...")
        sys.exit(1)
            
    sys.exit(app.exec_())
    




        
    
