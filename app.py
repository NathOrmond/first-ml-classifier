from fastai.vision.all import *
import gradio as gr

def is_cat(x): return x[0].isupper()
im = PILImage.create("images/dog.jpg")
im.thumbnail((192,192))

learn = load_learner("model.pkl")
learn.preddict(im)


iface = gr.Interface(fn=greet, inputs="text", outputs="text")
iface.launch()