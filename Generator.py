import pyqrcode
import png
import pyqrcode 

input_String = input()

url = pyqrcode.create(input_String)

url.show()