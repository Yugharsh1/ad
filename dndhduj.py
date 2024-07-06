
from tkinter import *
from simplecrypt import encrypt, decrypt
from tkinter import filedialog
from tkinter import messagebox
import os

root = Tk()
root.title("Encrypting Personal Data")
root.geometry("400x250")
root.config(bg = "orange")

file_name_entry = ""
encryption_text_data = ""
decryption_text_data = ""

def saveData():
    global file_name_entry
    global encryption_text_data
    file_name = file_name_entry.get()
    file = open(file_name + ".txt", "w")
    data = encryption_text_data.get("1.0", END)
    ciphercode = encrypt('AIM', data)
    hex_string = ciphercode.hex()
    print(hex_string)
    file.write(hex_string)
    file_name_entry.delete(0, END)
    encryption_text_data.delete(1.0, END)
    messagebox.showinfo("Update", "Success")
    
def viewData():
    global decryption_text_data
    text_file = filedialog.askopenfilename(title = "Open Text File", filetypes = (("Text Files", "*.txt"), ))
    name = os.path.basename(text_file)
    print(name)
    text_file = open(name, 'r')
    paragraph = text_file.read()
    byte_str = bytes.fromhex(paragraph)
    original = decrypt('AIM', byte_str)
    final_data = original.decode("utf-8")
    decryption_text_data.insert(END, final_data)
    text_file.close()

def startDecryption():
    global file_name_entry
    global decryption_text_data
    root.destroy()
 
    decryption_window = Tk()
    decryption_window.title("Decryption")
    decryption_window.config(bg = '#B2C9AB')
    decryption_window.geometry("600x500")
    
    decryption_text_data = Text(decryption_window, height = 20, width = 72)
    decryption_text_data.place(relx = 0.5, rely = 0.4, anchor = CENTER)
    
    btn_open_file = Button(decryption_window, text = "Choose File...", font = 'arial 13', command = viewData, bg = "red", relief = FLAT)
    btn_open_file.place(relx = 0.5, rely = 0.8, anchor = CENTER)
    
    decryption_window.mainloop()
    
def startEncryption():
    global file_name_entry
    global encryption_text_data
    root.destroy()
 
    encryption_window = Tk()
    encryption_window.title("Encryption")
    encryption_window.config(bg = '#B2C9AB')
    encryption_window.geometry("600x500")
    
    file_name_label = Label(encryption_window, text = "File Name:" , font = 'arial 13', bg = "orange")
    file_name_label.place(relx = 0.2, rely = 0.2, anchor = CENTER)
    
    file_name_entry = Entry(encryption_window, font = 'arial 15')
    file_name_entry.place(relx = 0.5, rely = 0.2, anchor = CENTER)
    
    btn_create = Button(encryption_window, text = "Create", font = 'arial 13', command = saveData, bg = "red", relief = FLAT)
    btn_create.place(relx = 0.8, rely = 0.2, anchor = CENTER)
    
    encryption_text_data = Text(encryption_window, height = 20, width = 72)
    encryption_text_data.place(relx = 0.5, rely = 0.6, anchor = CENTER)
    
    encryption_window.mainloop()
    
heading_label = Label(root, text = "Encryption & Decryption", font = 'arial 18 italic', bg = '#ADC698')
heading_label.place(relx = 0.5, rely = 0.2, anchor = CENTER)

btn_start_encryption = Button(root, text = "Start Encryption", font = 'arial 13', command = startEncryption, bg = "white", relief = FLAT)
btn_start_encryption.place(relx = 0.3, rely = 0.7, anchor = CENTER)

btn_start_decryption = Button(root, text = "Start Decryption", font = 'arial 13', command = startDecryption, bg = "white", relief = FLAT)
btn_start_decryption.place(relx = 0.7, rely = 0.7, anchor = CENTER)

root.mainloop()