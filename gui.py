import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image


def generate_caption():
    # preprocess the image same as we are doing for model
    # dimension and channels of image
    # feed the image to the model
    # return caption generated from the model
    return

def encode(image):
    # image = preprocess_img(image)
    # vec = vgg_model.predict(image)
    # vec = np.reshape(vec, (vec.shape[1]))
    return

top = tk.Tk()
top.geometry('800x600')
top.title('Image Captioning')
top.configure(background='#f0f0f0')

label = Label(top, background = '#CDCDCD', font = ('arial',15))

sign_image = Label(top)

def classify(file_path):
    global label_packed
    # enc = encode(file_path)
    # image = enc.reshape(1, 2048)
    predicted_caption = 'Caption will go here' # generate_caption(image) <-n uncomment it
    label.configure(foreground='#000000', text='Generated Caption: ' + predicted_caption)
    label.pack(side=BOTTOM, expand=True)

def show_classify_button(file_path):
    classify_b=Button(top,text="Generate",command=lambda: classify('file_path'),padx=10,pady=5)
    classify_b.configure(background='#364156', foreground='white',font=('arial',10,'bold'))
    classify_b.place(relx=0.79,rely=0.46)

def upload_image():
    try:
        file_path=filedialog.askopenfilename()
        uploaded=Image.open(file_path)
        uploaded.thumbnail(((top.winfo_width()/2.25),(top.winfo_height()/2.25)))
        im=ImageTk.PhotoImage(uploaded)
        sign_image.configure(image=im)
        sign_image.image=im
        label.configure(text='')
        show_classify_button('file_path')
    except:
        pass

upload=Button(top,text="Upload an image",command=upload_image,padx=10,pady=5)
upload.configure(background='#364156', foreground='white',font=('arial',10,'bold'))
upload.pack(side=BOTTOM,pady=50)
sign_image.pack(side=BOTTOM,expand=True)
top.mainloop()
