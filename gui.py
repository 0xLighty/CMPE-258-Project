import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image
from keras.applications.xception import Xception
from pickle import load
from keras.models import Model, load_model
import numpy as np
from keras.preprocessing.sequence import pad_sequences


max_length = 26
tokenizer = load(open("data/tokenizer.p","rb"))
model = load_model('Models/model_29.h5')
xception_model = Xception(include_top=False,pooling='avg')

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


def extract_features(filename, model):
    # image = Image.open(filename)

    # image = image.resize((299,299))
    # image = np.array(image)
    image = Image.open(filename)
    image = image.resize((299, 299))
    image = np.expand_dims(image, axis=0)
    # image = preprocess_input(image)
    image = image / 127.5
    image = image - 1.0
    print(np.shape(image))
    feature = model.predict(image)

    # print(np.shape(feature))

    return feature

def word_for_id(integer, tokenizer):
    for word, index in tokenizer.word_index.items():
        if index == integer:
            return word
    return None

def generate_desc(model, tokenizer, photo, max_length):
    in_text = 'start'
    for i in range(max_length):
        sequence = tokenizer.texts_to_sequences([in_text])[0]
        sequence = pad_sequences([sequence], maxlen=max_length)

        pred = model.predict([photo, sequence], verbose=0)
        pred = np.argmax(pred)
        word = word_for_id(pred, tokenizer)
        if word == ".":
            break
        in_text += ' ' + word
        if word == 'end':
            break

    decoded_caption = in_text.replace("start ", "")
    decoded_caption = decoded_caption.replace(" end", "").strip()
    return decoded_caption



def classify(file_path):
    global label_packed
    # enc = encode(file_path)
    # image = enc.reshape(1, 2048)

    photo = extract_features(file_path, xception_model)
    photo = photo.reshape(1, 2048)
    predicted_caption = generate_desc(model, tokenizer, photo, max_length)

    # predicted_caption = 'Caption will go here' # generate_caption(image) <-n uncomment it
    label.configure(foreground='#000000', text='Generated Caption: ' + predicted_caption)
    label.pack(side=BOTTOM, expand=True)

def show_classify_button(file_path):
    classify_b=Button(top,text="Generate",command=lambda: classify(file_path),padx=10,pady=5)
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
        show_classify_button(file_path)
    except:
        pass

upload=Button(top,text="Upload an image",command=upload_image,padx=10,pady=5)
upload.configure(background='#364156', foreground='white',font=('arial',10,'bold'))
upload.pack(side=BOTTOM,pady=50)
sign_image.pack(side=BOTTOM,expand=True)
top.mainloop()
