import pyqrcode
import png
import pyqrcode 

input_String = input()
#This is the first Comment
url = pyqrcode.create(input_String)

url.show()