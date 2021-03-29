import os
import tkinter
import tkinter.filedialog
import tkinter.messagebox
import tkinter.ttk


class UserInterface:
    def __init__(self):
        self.gui = tkinter.Tk("Firmware Encoder")
        self.gui.geometry("345x85")
        self.string_firmware_fpath = tkinter.StringVar()
        self.label_firmware_fpath = tkinter.Label(self.gui, text="firmware :")
        self.label_firmware_fpath.grid(column=0, row=0, ipadx=5, ipady=10)
        self.textbox_firmware_fpath = tkinter.Entry(self.gui, textvariable=self.string_firmware_fpath, width=25,
                                                    state="readonly")
        self.textbox_firmware_fpath.grid(column=1, row=0, padx=5)
        self.button_open_filedialog = tkinter.Button(self.gui, text="Open", width=10, command=self.open_file)
        self.button_open_filedialog.grid(column=2, row=0)

        self.button_encode = tkinter.Button(self.gui, text="Encode", width=10, command=self.encode_file)
        self.button_encode.grid(column=0, columnspan=3, row=1, sticky=tkinter.W + tkinter.E, padx=5, pady=5)

        self.firmware_fpath = ""

    def __new__(cls):
        return super().__new__(cls)

    def run(self):
        self.gui.mainloop()

    def open_file(self):
        self.firmware_fpath = tkinter.filedialog.askopenfilename(initialdir="c:", title="select a firmware-file")
        self.string_firmware_fpath.set(self.firmware_fpath)

    def encode_file(self):
        if len(self.firmware_fpath) == 0:
            tkinter.messagebox.showerror("File Error", "The file is not found.")
            return
        fsize = os.path.getsize(self.firmware_fpath)
        if fsize == 0:
            tkinter.messagebox.showerror("File Error", "The target file size is zero")
            return
        encoded_fpath = self.firmware_fpath + ".encode"
        fw = open(encoded_fpath, 'wb')
        fr = open(self.firmware_fpath, 'rb')
        file_data = fr.read(fsize)
        encoded_data = bytearray()
        for i in range(0, fsize):
            byte = file_data[i] ^ 0x0f
            encoded_data.append(byte)

        byte_array = bytes(encoded_data)
        fw.write(byte_array)
        fr.close()
        fw.close()


UserInterface().run()
