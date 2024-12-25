from tkinter.filedialog import askdirectory
from pytube import *
from tkinter import *
from tkinter.messagebox import *
from threading import *

file_size = 0
file_downloaded = 0

#downloading progress function
def progress(steam=None,chunk=None,file_handle=None,remaining=None):
    global file_downloaded
    file_downloaded = (file_size - remaining)
    per = (file_downloaded / file_size) * 100
    d_btn.config(text=f"{per} % downloaded")


def startDownload():
 
    global file_size
    try:
        url = url_entry.get()
        print(url)

        #changing button text

       
        #creating youtube object with url..
        
        path_to_save_video = askdirectory()
        print(path_to_save_video)
        if path_to_save_video is None:
            return
        
        d_btn.config(text='please wait...')
        d_btn.config(state=DISABLED)
        # strm = obj.streams.all()
        # for s in strm:
        #     print(s)
        obj = YouTube(url,on_progress_callback=progress)
        strm = obj.streams.first()
        file_size = strm.filesize
        print(file_size)
        strm.download(path_to_save_video)
        print("Done..")
        #changing on done
        d_btn.config(text="Start Download")
        d_btn.config(state=NORMAL)
        
        showinfo("file is downloaded","Downloaded successfully")
        # url_entry.delete(0,END) 
    except Exception as e:
        print(e)
        print("something wrong !!")
    
#thread function
 
def startDownloadThread():
    thread = Thread(target=startDownload)
    thread.start()

#starting GUI building
main = Tk()
main.title("youtube downloader")
 
icon_path = "C:\\Users\\satya\\OneDrive\\Documents\\Just_Do_it\\python\\icon.ico"
main.iconbitmap(icon_path)

main.geometry("500x600")

#heading icon
file = PhotoImage(file='C:\\Users\\satya\\OneDrive\\Documents\\Just_Do_it\\python\\icon.png')
headingIcon = Label(main, image=file)
headingIcon.pack(side=TOP)


#url text field

url_entry =  Entry(main,font=("monospace",18),justify=CENTER) 

url_entry.pack(side=TOP,fill=X, padx=10)

# download button

d_btn = Button(main, text="Download", font=("monospace",18),relief='ridge',command=startDownloadThread)
d_btn.pack(side=TOP,padx=10)


main.mainloop()