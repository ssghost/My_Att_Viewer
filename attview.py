import tensorflow as tf
import pandas as pd
from keras.models import load_model
import matplotlib.pyplot as plt

class Visualizer:
    def __init__(self):
        self.model = None
        self.attention = None
        self.map = None

    def read(self, modelpath):
        self.model = load_model(modelpath)
        self.attention = self.model.get_layer('attention_vec').output

    def color_cv(self, s):
        r = 255-int(s.val*255)
        color = '#%02x%02x%02x' % (255,r,r)
        return color

    def create_map(self, seq, figsize):
        class CVpair(object):
            def __init__(self, char, val):
                self.char = char
                self.val = val
            def __str__(self):
                return self.char 
        att_out = self.attention[0][-len(seq.in_tokens):]
        cvpairs = [CVpair(c,v) for c,v in zip(seq.dec, att_out)]
        cdf = pd.DataFrame(cvpairs).transpose()
        self.map = cdf.style.applymap(self.color_cv)
        fig = self.map.plot(size = figsize).get_figure()
        fig.savefig('attmap.pdf')
