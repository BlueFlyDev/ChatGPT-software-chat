import Utils
import mainui
import sys
from PyQt5.QtWidgets import QApplication

token = Utils.getYml("account")['key']
url = Utils.getYml("account")['url']

app = QApplication(sys.argv)
print("loading....")
ex = mainui.CustomUI()
ex.show()
print("Start!")
sys.exit(app.exec_())
