import tkinter as tk
from tkinter import*
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile

#window
root = tk.Tk()
root.geometry('500x500')
root.title('Python Image Converter')
heading = Label(text = 'Image Converter', fg = 'black')
heading.grid()

#file name entry label
fileEntryLabel = tk.Label(root, text='File Name:')
fileEntryLabel.grid(column=0, row=1)

#file name entry
file_name = tk.Entry()
file_name.grid(column=1, row=1)




class ImageConvert():
    #open file and present convert button
    def open_image(self):
        browse_text.set('Loading...')
        file= askopenfile(parent=root, mode='rb', title='choosefile', filetype=[('Image file', '*')])
        if file:
            #convert button
            convert_text = tk.StringVar()
            convert_btn = tk.Button(root, textvariable=convert_text, font='Calibri', bg='#20bebe', fg='white', height=2, width=15, command=lambda:convert_file())
            convert_text.set('Convert')
            convert_btn.grid(column=1, row=5)
        def convert_file():
            def choose_type(a):
                file_type = a
                img = Image.open(file)
                img.save(f'{str(file_name.get())}.{file_type}', f'{file_type}')
            #png button
            convert_text = tk.StringVar()
            convert_btn = tk.Button(root, textvariable=convert_text, font='Calibri', bg='#20bebe', fg='white', height=2, width=15, command=lambda:choose_type('png'))
            convert_text.set('PNG')
            convert_btn.grid(column=1, row=6)
            #jpeg button
            convert_text = tk.StringVar()
            convert_btn = tk.Button(root, textvariable=convert_text, font='Calibri', bg='#20bebe', fg='white', height=2, width=15, command=lambda:choose_type('jpeg'))
            convert_text.set('JPEG')
            convert_btn.grid(column=1, row=7)
            


#browse button
execute = ImageConvert()
browse_text = tk.StringVar()
browse_btn = tk.Button(root, textvariable=browse_text, font='Calibri', bg='#20bebe', fg='white', height=2, width=15, command=lambda:execute.open_image())
browse_text.set('Browse')
browse_btn.grid(column=1, row=2)

#end loop
root.mainloop()