from urllib.request import urlopen


class Document:

    def __init__(self):
        response = urlopen('https://aca.am/en/')
        self.x = response.read().decode().splitlines()[3].replace(" ", "")

    def decode(self):
        return ''.join(chr(int(self.x[i*8:i*8+8], 2)) for i in range(len(self.x)//8))

a = Document()
print(a.decode())