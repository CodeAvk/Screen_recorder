from tkinter import *
import pyscreenrec


root=Tk()
root.geometry("400x600")
root.title("@Avk_ScreenRecorder")
root.config(bg="#fff")
root.resizable(False,False)

def start_rec():
    file=Filename.get()
    rec.start_recording(str(file+".mp4"),5)

def resume_rec():
    rec.resume_recording()


def stop_rec():
    rec.stop_recording()

def pause_rec():
    rec.pause_recording()

# icon
image_icon=PhotoImage(file="scr_icon.png")
root.iconphoto(False,image_icon)

#background Image
image1=PhotoImage(file="scr_yelllow.png")
Label(root,image=image1,bg="#fff").place(x=-2,y=35)

image2=PhotoImage(file="scr_blue.png")
Label(root,image=image2,bg="#fff").place(x=223,y=200 )

# heading
lbl=Label(root,text="Screen Recorder",bg="#fff",font="arial  15 bold")
lbl.pack(pady=12)


image3=PhotoImage(file="scr_recording.png")
Label(root,image=image3,bd=0).pack(pady=30 )

#entry
Filename=StringVar()
entry=Entry(root,textvariable=Filename,width=18,font="DS-Digital  15 bold")
entry.place(x=73,y=350)
Filename.set("recording###")

# Buttons
start=Button(root,text="Start",font="arial 20",bd=0,command=start_rec)
start.place(x=136,y=232)

image4=PhotoImage(file="scr_pause.png")
pause=Button(root,image=image4,bd=0,bg="#fff",command=pause_rec)
pause.place(x=50,y=450 )

image5=PhotoImage(file="scr_resume.png")
resume=Button(root,image=image5,bd=0,bg="#fff",command=resume_rec)
resume.place(x=150,y=450 )

image6=PhotoImage(file="scr_stop.png")
stop=Button(root,image=image6,bd=0,bg="#fff",command=stop_rec)
stop.place(x=250,y=450 )

rec=pyscreenrec.ScreenRecorder()


root.mainloop()

