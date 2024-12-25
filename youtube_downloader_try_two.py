from pytube import * 
from tkinter.filedialog import *
from tkinter import *
from tkinter.messagebox import *
from threading import *

# https://youtu.be/UjEngEpiJKo?si=6e6FxujQvI5Azzwk

file_size = None
init_remain = 0

def progress(stream=None,chunk=None,file_handle=None,remaining=init_remain):
    file_downloaded = (file_size - remaining)
    per = (file_downloaded/file_size) * 100
    dBtn.config(text="{:00.0f} % downloaded ".format(per))


def startDownload():
    global file_size

    try:
        url = urlField.get()
        print(url)
        #changing button text
        dBtn.configure(text="please wait...")
        dBtn.config(state=DISABLED)


        path_to_save_video = askdirectory()
        if path_to_save_video is None:
            return      
          
        ob = YouTube(url,on_progress_callback=progress)

        strm = ob.streams.get_highest_resolution()
        file_size = strm.filesize
        vTitle.config(text=strm.title)
        vTitle.pack(side=TOP)
        print(file_size)

        strm.download(path_to_save_video)
        print("done...")
        dBtn.config(text="start download")

        dBtn.config(state=NORMAL)
        showinfo("Download finished","Downloaded successfully")
        urlField.delete(0,END)
        vTitle.pack_forget()

    except Exception as e:
        print(e)
        print("something wrong...")


def startDownloadThread():
    thread = Thread(target=startDownload)
    thread.start()

# GUI building

main = Tk()

#Setting the title 
main.title("YOUTUBE DOWNLOADER")

main.iconbitmap('C:\\Users\\satya\\OneDrive\\Documents\\Just_Do_it\\python\\icon.ico')
main.geometry("500x600")

#heading icon

file = PhotoImage(file='C:\\Users\\satya\\OneDrive\\Documents\\Just_Do_it\\python\\icon.png')
headingIcon = Label(main,image=file)
headingIcon.pack(side=TOP)

#url entry

urlField = Entry(main,font=("monospace",18),justify=CENTER)
urlField.pack(side=TOP,fill=X,padx=10)

#Download Button

dBtn = Button(main,text="start downlaod",font=("monospace",18),relief="ridge",command=startDownloadThread)
dBtn.pack(side=TOP,pady=10)

# video title
vTitle = Label(main,text="video title")



main.mainloop()