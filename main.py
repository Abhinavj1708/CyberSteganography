import AES, DES, ElGamal, Playfair, Hill, Twofish, LSBImage, LSBAudio
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import *
# i = int(input('AES or DES'))
'''if i:
    cipher, Tkey = AES.encrypt()
    AES.decrypt(cipher, Tkey)
else:
    cipher, rk, rkb = DES.encrypt()
    DES.decrypt(cipher, rk, rkb)'''
# cipher, rk, rkb = DES.encrypt()
# LSBImage.Stego(cipher)
# LSBImage.Stego(cipher)
# DES.decrypt(cipher, rk, rkb)

'''cipher, Tkey = AES.encrypt()
LSBImage.Encode(cipher)
LSBImage.Decode()
AES.decrypt(cipher, Tkey)'''

# cipher, Tkey = AES.encrypt()
# LSBAudio.encode(cipher)
# LSBAudio.decode()
# AES.decrypt(cipher, Tkey)

# cipher, Tkey = AES.encrypt()
# channels = PhaseAudio.encode(cipher)
# PhaseAudio.decode(channels)
# AES.decrypt(cipher, Tkey)

root = Tk()
cipher = ''
decipher = ''
Tkey = ''
rk = ''
rkb = ''
a = 0
q = 0
p = 0
key1 = []
key2 = []
correct = []
K = []
chk = []
C = []
key = ''
# create window using from in Tkinter
class Window(Frame):

    # Define settings upon initialization. Here you can specify
    def __init__(self, master=None):
        # parameters that you want to send through the Frame class.
        Frame.__init__(self, master)
        # reference to the master widget, which is the tk window
        self.master = master


        self.init_window()

    # Creation of init_window
    def init_window(self):
        # changing the title of our master widget
        self.master.title("Cryptography-Steganography")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)
        self.appEncrypt()
        self.appDecrypt()

    def appEncrypt(self):
        # encode Label
        self.encodeVar = StringVar()
        self.encodelabel = Label(root, textvariable=self.encodeVar)
        self.encodelabel.place(x=10, y=10)
        self.encodeVar.set("Encryption ")

        self.encodeVar2 = StringVar()
        self.encodelabel2 = Label(root, textvariable=self.encodeVar2)
        self.encodelabel2.place(x=10, y=50)
        self.encodeVar2.set("Cryptography")
        # select algo
        self.optionsVar = StringVar()
        self.optionsVar.set("AES")  # default value

        self.encodingOptionsMenu = OptionMenu(root, self.optionsVar, "AES", "DES", "ElGamal", "Playfair", "Hill", "Twofish")
        self.encodingOptionsMenu.place(x=10, y=80)

        self.entryText = Entry(root)
        self.entryText.place(x=10, y=110)
        self.entryText.insert(0, "Enter Plaintext ")
        
        self.entryText2 = Entry(root)
        self.entryText2.place(x=10, y=150)
        self.entryText2.insert(0, "Enter Key ")
        # encode Button
        self.encodeVar3 = StringVar()
        self.encodelabel3 = Label(root, textvariable=self.encodeVar3)
        self.encodelabel3.place(x=10, y=200)
        self.encodeVar3.set("Steganography")
        # select algo
        self.optionsVar2 = StringVar()
        self.optionsVar2.set("LSB Image")  # default value

        self.encodingOptionsMenu2 = OptionMenu(root, self.optionsVar2, "LSB Image", "LSB Audio")
        self.encodingOptionsMenu2.place(x=10, y=225)

        # creating a button instance
        self.selectFileButton = Button(self, text="Select File To Encode", command=self.selectFile)
        self.selectFileButton.place(x=10, y=270)

        # file location label
        self.var = StringVar()
        self.label = Label(root, textvariable=self.var, relief=RAISED)
        self.label.place(x=10, y=320)
        # placing the button on my window

        # entry box
        self.encodeButton = Button(self, text="Encode", command=self.encode)
        self.encodeButton.place(x=10, y=370)
        # encoded  location label
        self.enocdedLocation = StringVar()
        self.locationOfEncodeFile = Label(root, textvariable=self.enocdedLocation)
        self.locationOfEncodeFile.place(x=10, y=400)

    def appDecrypt(self):
        # decode Label
        self.decodeVar = StringVar()
        self.decodelabel = Label(root, textvariable=self.decodeVar)
        self.decodelabel.place(x=500, y=10)
        self.decodeVar.set("Decoding ")

        # select algo
        self.decodeOptionsVar = StringVar()
        self.decodeOptionsVar.set("Least Significant Bit")  # default value

        self.decodingOptionsMenu = OptionMenu(root, self.decodeOptionsVar, "LSB Image", "LSB Audio")
        self.decodingOptionsMenu.place(x=500, y=50)
        # creating a button instance
        self.selectFileDecodeButton = Button(self, text="Select  File To Decode ", command=self.selectFileDecode)
        self.selectFileDecodeButton.place(x=500, y=100)
        
        self.decodeOptionsVar2 = StringVar()
        self.decodeOptionsVar2.set("AES")  # default value

        self.decodingOptionsMenu2 = OptionMenu(root, self.decodeOptionsVar2, "AES", "DES", "ElGamal", "Playfair", "Hill", "Twofish")
        self.decodingOptionsMenu2.place(x=500, y=170)

        #
        # file location label
        self.decodeFileVar = StringVar()
        self.decodeFileLabel = Label(root, textvariable=self.decodeFileVar, relief=RAISED)
        self.decodeFileLabel.place(x=500, y=140)

        self.decodeButton = Button(self, text="Decode", command=self.decode)
        self.decodeButton.place(x=500, y=200)
        #
        # decoded text label
        self.decodedString = StringVar()
        self.decodedStringlabel = Label(root, textvariable=self.decodedString, font=(None, 40))
        self.decodedStringlabel.place(x=500, y=350)

    def client_exit(self):
        exit()

    def selectFile(self):
        # file selection
        root.filename = filedialog.askopenfilename(initialdir="C:/Users/VIT/Desktop/Crypto-Stego/", title="Select file",
                                                   filetypes=(("Image file", "*.png"), ("Audio file", "*.wav"), ("all files", "*.*")))
        self.fileSelected = root.filename
        self.var.set(root.filename)

    def selectFileDecode(self):
        root.filename = filedialog.askopenfilename(initialdir="C:/Users/VIT/Desktop/Crypto-Stego/", title="Select file",
                                                   filetypes=(("Image file", "*.png"), ("Audio file", "*.wav"), ("all files", "*.*")))
        self.fileSelcetedForDecode = root.filename
        self.decodeFileVar.set(root.filename)

    def encode(self):
        # select algo to encode
        if self.optionsVar.get() == "AES":
            global Tkey
            cipher, Tkey = AES.encrypt(self.entryText.get(), self.entryText2.get())
        elif self.optionsVar.get() == "DES":
            global rk
            global rkb
            cipher, rk, rkb = DES.encrypt(self.entryText.get(), self.entryText2.get())
        elif self.optionsVar.get() == "ElGamal":
            global a, q, p
            cipher, a, q, p = ElGamal.encode(self.entryText.get())
        elif self.optionsVar.get() == "Playfair":
            global key1, key2, correct
            cipher, key1, key2, correct = Playfair.cipher(self.entryText.get(), self.entryText2.get())
        elif self.optionsVar.get() == "Hill":
            global K, chk, C
            cipher, K, chk, C = Hill.encrypt(self.entryText.get())
        else:
            global key
            cipher, key = Twofish.encrypt(self.entryText.get(), self.entryText2.get())

        if self.optionsVar2.get() == "LSB Image":
            LSBImage.Encode(cipher, self.fileSelected)
        else:
            LSBAudio.encode(cipher, self.fileSelected)
        result = 'Encrypted successfully!'
        self.enocdedLocation.set(result)
        

    def decode(self):
        # select algo to decode
        if self.decodeOptionsVar.get() == "LSB Image":
            decipher = LSBImage.Decode(self.fileSelcetedForDecode)
        else:
            decipher = LSBAudio.decode(self.fileSelcetedForDecode)

        if self.decodeOptionsVar2.get() == "AES":
            global Tkey
            result = AES.decrypt(decipher, Tkey)
        elif self.decodeOptionsVar2.get() == "DES":
            global rk
            global rkb
            result = DES.decrypt(decipher, rk, rkb)
        elif self.decodeOptionsVar2.get() == "ElGamal":
            global a, q, p
            result = ElGamal.decode(decipher, a, q, p)
        elif self.decodeOptionsVar2.get() == "Playfair":
            global key1, key2, correct
            result = Playfair.decipher(decipher, key1, key2, correct)
        elif self.decodeOptionsVar2.get() == "Hill":
            global K, chk
            result = Hill.decrypt(decipher, C, K, chk)
        else:
            global key
            result = Twofish.decrypt(decipher, key)
            # print(result)
        self.decodedString.set(result)


# resolution
root.geometry("1000x600")

# creation of an instance of window
app = Window(root)

# mainloop
root.mainloop()
