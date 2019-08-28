from tkinter import *
from tkinter import ttk, messagebox
import os


class Application(Frame):

    def __init__(self):
        super().__init__()
        self.gui()
        self.local_dir = '%APPDATA%\\kicad\\fp-lib-table '
        self.server_dir = '"\\\\192.168.0.2\\dane\\Biblioteki KICAD\\" '

    def download(self):
        MsgBox = messagebox.askquestion(
            'Pobieranie biblioteki',
            'Jesteś pewien, że chcesz pobrać nową bibliotekę z serwera?',
            icon='warning')
        if MsgBox == 'yes':
            try:
                cmd = 'copy ' + self.server_dir + self.local_dir + ' /Z /Y'
                os.system(cmd)
                print('Plik został pobrany na dysk.')
            except Exception:
                print('Nie pobrano. Sprawdź czy plik istnieje.')

    def upload(self):
        MsgBox = messagebox.askquestion(
            'Wysyłanie biblioteki',
            'Jesteś pewien, że chcesz wysłać nową bibliotekę na serwer?',
            icon='warning')
        if MsgBox == 'yes':
            try:
                cmd = 'copy ' + self.local_dir + self.server_dir + ' /Z /Y'
                os.system(cmd)
                print('Plik został wysłany na serwer.')
            except Exception:
                print('Nie udało się wysłać na serwer.')

    def gui(self):

        self.pack(fill=BOTH, expand=True)

        main_frame = Frame(self)
        main_frame.grid(column=0, row=0)
        main_frame.columnconfigure(0, pad=10)
        main_frame.columnconfigure(1, pad=10)
        main_frame.rowconfigure(0, pad=10)

        download_frame = Frame(main_frame)
        download_frame.grid(column=0, row=0, sticky='news')

        upload_frame = Frame(self)
        upload_frame.grid(column=1, row=0, sticky='news')

        self.downloadbtn = ttk.Button(
            download_frame,
            text='Pobierz bibliotekę',
            command=self.download)
        self.downloadbtn.pack(ipadx=10, ipady=10, fill=BOTH, pady=10, padx=10)

        self.uploadbtn = ttk.Button(
            upload_frame,
            text='Wyślij bibliotekę',
            command=self.upload)
        self.uploadbtn.pack(ipadx=10, ipady=10, fill=BOTH, pady=10, padx=10)


def main():
    app = Application()
    app.master.title('KiCad Library Updater')
    app.mainloop()


if __name__ == '__main__':
    main()
