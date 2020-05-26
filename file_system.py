import os
import shutil
import timeit
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

# Developed by David
start = timeit.default_timer()


class Login_class(object):
    def __init__(self, mainframe):
        self.mainframe = mainframe
        self.timelb = tk.Label(self.mainframe, bg='light gray', width=15)
        self.timelb.pack()

        self.root = tk.LabelFrame(mainframe, width=650, height=200, text='File', font=('Times', 16, 'bold'), bd=6,
                                  bg='sky blue')
        self.root.pack(pady=40)

        self.path_lb = tk.Label(self.root, text='Select Path', width=20, font=('Helvetical', 18, ''), bg='sky blue')
        self.path_lb.place(x=50, y=20)

        def fun():
            self.txt.delete('1.0', 'end')
            path1 = filedialog.askdirectory(parent=self.root, initialdir='c:/', title='Path Selection.')
            try:
                os.chdir(path1)
                self.txt.insert('insert', 'Directory successfully changed.\n')
            except OSError as e:
                self.txt.insert('insert', f"Can't change current directory.\n {e}\n")

            self.txt.insert('insert', f'Present path   {os.getcwd()} \n\n')
            for j in os.listdir():
                self.txt.insert('insert', f'{j}\n')
            # print(path1)

        def arrange_file():
            ask = messagebox.askyesno('Path', f'Current path is {os.getcwd()}. \nDo you want to continue with this.')
            start1 = timeit.default_timer()
            if ask:
                # print(os.getcwd())
                # print(os.listdir())
                for file in os.listdir():
                    # ************************************************************ MUSIC
                    if '.mp3' in file or '.aif' in file or '.cda' in file or '.mid' in file or '.midi' in file or '.mpa' in file or '.ogg' in file or '.wav' in file or '.wma' in file or '.wpl' in file:
                        if not os.path.exists('Music'):
                            os.mkdir('Music')
                        try:
                            curr_path = os.path.join(os.getcwd(), file)
                            dest_path = os.path.join(os.getcwd(), 'Music')
                            shutil.move(curr_path, dest_path)
                        except:
                            messagebox.showerror('Error!', 'Error in Music please inform to developer.')

                    elif '.jpg' in file or '.png' in file or '.ai' in file or '.bmp' in file or '.gif' in file or '.ico' in file or '.jpeg' in file or '.ps' in file or '.psd' in file or '.svg' in file or '.tif' in file or '.tiff' in file:
                        if not os.path.exists('Pictures'):
                            os.mkdir('Pictures')
                        try:
                            curr_path = os.path.join(os.getcwd(), file)
                            dest_path = os.path.join(os.getcwd(), 'Pictures')
                            shutil.move(curr_path, dest_path)
                        except:
                            messagebox.showerror('Error!', 'Error in Pictures please inform to developer.')

                    elif '.zip' in file or '.7z' in file or '.arj' in file or '.deb' in file or '.pkg' in file or '.rar' in file or '.rpm' in file or '.tar.gz' in file or '.z' in file:
                        if not os.path.exists('Compressed files'):
                            os.mkdir('Compressed files')
                        try:
                            curr_path = os.path.join(os.getcwd(), file)
                            dest_path = os.path.join(os.getcwd(), 'Compressed files')
                            shutil.move(curr_path, dest_path)
                        except:
                            messagebox.showerror('Error!', 'Error in Compressed files please inform to developer.')

                    elif '.dmg' in file or '.iso' in file or '.toast' in file or '.vcd' in file:
                        if not os.path.exists('Dic and Media'):
                            os.mkdir('Dic and Media')
                        try:
                            curr_path = os.path.join(os.getcwd(), file)
                            dest_path = os.path.join(os.getcwd(), 'Dic and Media')
                            shutil.move(curr_path, dest_path)
                        except:
                            messagebox.showerror('Error!', 'Error in Dic and Media please inform to developer.')

                    elif '.csv' in file or '.dat' in file or '.db' in file or '.dbf' in file or '.log' in file or '.mdb' in file or '.sav' in file or '.sql' in file or '.tar' in file or '.xml' in file:
                        if not os.path.exists('Database'):
                            os.mkdir('Database')
                        try:
                            curr_path = os.path.join(os.getcwd(), file)
                            dest_path = os.path.join(os.getcwd(), 'Database')
                            shutil.move(curr_path, dest_path)
                        except:
                            messagebox.showerror('Error!', 'Error in Database please inform to developer.')

                    elif '.email' in file or '.eml' in file or '.emlx' in file or '.msg' in file or '.oft' in file or '.ost' in file or '.pst' in file or '.vcf' in file:
                        if not os.path.exists('E-mail'):
                            os.mkdir('E-mail')
                        try:
                            curr_path = os.path.join(os.getcwd(), file)
                            dest_path = os.path.join(os.getcwd(), 'E-mail')
                            shutil.move(curr_path, dest_path)
                        except:
                            messagebox.showerror('Error!', 'Error in E-mail please inform to developer.')

                    elif '.exe' in file or '.apk' in file or '.bat' in file or '.bin' in file or '.cgi' in file or '.com' in file or '.gadget' in file or '.jar' in file or '.msi' in file or '.wsf' in file:
                        if not os.path.exists('Executable files'):
                            os.mkdir('Executable files')
                        try:
                            curr_path = os.path.join(os.getcwd(), file)
                            dest_path = os.path.join(os.getcwd(), 'Executable files')
                            shutil.move(curr_path, dest_path)
                        except:
                            messagebox.showerror('Error!', 'Error in Executable files please inform to developer.')

                    elif '.fnt' in file or '.fon' in file or '.otf' in file or '.tt' in file:
                        if not os.path.exists('Fonts'):
                            os.mkdir('Fonts')
                        try:
                            curr_path = os.path.join(os.getcwd(), file)
                            dest_path = os.path.join(os.getcwd(), 'Fonts')
                            shutil.move(curr_path, dest_path)
                        except:
                            messagebox.showerror('Error!', 'Error in Fonts please inform to developer.')

                    elif '.c' in file or '.py' in file or '.java' in file or '.asp' in file or '.aspx' in file or '.cer' in file or '.cfm' in file or '.cgi' in file or '.pl' in file or '.css' in file or '.html' in file or '.htm' in file or '.js' in file or '.jsp' in file or '.part' in file or '.php' in file or '.rss' in file or '.xhtml' in file or '.class' in file or '.cs' in file or '.cpp' in file or '.h' in file or '.sh' in file or '.vd' in file or '.go' in file or '.pyc' in file:
                        if not os.path.exists('Programming'):
                            os.mkdir('Programming')
                        try:
                            curr_path = os.path.join(os.getcwd(), file)
                            dest_path = os.path.join(os.getcwd(), 'Programming')
                            shutil.move(curr_path, dest_path)
                        except:
                            messagebox.showerror('Error!', 'Error in Programming please inform to developer.')

                    elif '.mp4' in file or '.3g2' in file or '.3gp' in file or '.avi' in file or '.flv' in file or '.h264' in file or '.m4v' in file or '.mkv' in file or '.mov' in file or '.mp4' in file or '.mpg' in file or '.mpeg' in file or '.rm' in file or '.swf' in file or '.vob' in file or '.wmv' in file:
                        if not os.path.exists('Videos'):
                            os.mkdir('Videos')
                        try:
                            curr_path = os.path.join(os.getcwd(), file)
                            dest_path = os.path.join(os.getcwd(), 'Videos')
                            shutil.move(curr_path, dest_path)
                        except:
                            messagebox.showerror('Error!', 'Error in Videos please inform to developer.')

                    elif '.txt' in file or '.doc' in file or '.docx' in file or '.pdf' in file or '.rtf' in file or '.tex' in file or '.wpd' in file or '.ods' in file or '.xls' in file or '.xlsm' in file or '.xlsx' in file or '.key' in file or '.odp' in file or '.pptx' in file or '.ppt' in file:
                        if not os.path.exists('Docs'):
                            os.mkdir('Docs')
                        try:
                            curr_path = os.path.join(os.getcwd(), file)
                            dest_path = os.path.join(os.getcwd(), 'Docs')
                            shutil.move(curr_path, dest_path)
                        except:
                            messagebox.showerror('Error!', 'Error in Docs please inform to developer.')

                stop1 = timeit.default_timer()
                self.timelb.config(text=f'Time : {round(stop1 - start1, 5)} sec')
            else:
                fun()
            self.txt.delete('1.0', 'end')
            self.txt.insert('insert', f'Present path   {os.getcwd()} \n\n')
            for k in os.listdir():
                self.txt.insert('insert', f'{k}\n')

        self.browse = tk.Button(self.root, text='Browse', command=fun, width=15, font=('Helvetical', 16, ''),
                                bg='light green', relief='raise')
        self.browse.place(x=300, y=10)

        self.arrange = tk.Button(self.root, command=arrange_file, text='Arrange', width=15, font=('Times', 16, ''),
                                 bg='orange')
        self.arrange.place(x=220, y=100)

        self.txt = tk.Text(self.mainframe, width=70, height=12, bg='snow', font=16)
        self.txt.pack(pady=20)

        self.txt.insert('insert', f'Present path {os.getcwd()} \n')
        for i in os.listdir():
            self.txt.insert('insert', f'{i}\n')

        stop = timeit.default_timer()
        self.timelb.config(text=f'Time : {round(stop - start, 5)} sec')


def Account_main():
    master = tk.Tk()
    Login_class(master)
    master.title("File Arrangement System")
    master.geometry("800x580+270+65")
    # master.config(bg='#F0F8FF')
    master.config(bg='#EFDECD')
    master.mainloop()


if __name__ == '__main__':
    Account_main()
