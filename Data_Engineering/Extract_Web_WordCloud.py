
# Import request for web scrapping

from xml.dom.minidom import Element
import pandas as pd
import requests as rq
import numpy as np
import collections

# Matplotlub and associated plotting modules
import matplotlib.cm as cm
import matplotlib.colors as colors
import matplotlib as mpl
import matplotlib.pyplot as plt

# Import k-means for clustering stage
from PIL import Image
from matplotlib import rcParams

print('Libraries installed')

website_url = rq.get('https://lopezobrador.org.mx/2020/09/01/discurso-del-presidente-andres-manuel-lopez-obrador-en-su-segundo-informe-de-gobierno/')

# Import BeautifulSoup for html structure info from our request

from bs4 import BeautifulSoup
html = website_url.text

soup = BeautifulSoup(html, "lxml")

data = [element.text for element in soup.find_all('p')] # Retrieving text from 'p' founds
data = str(data) # Convert to string
data

# Word Cloud

from stop_words import get_stop_words # the words we want to ignore

stop_words_es = get_stop_words('es') # spanish stopwords

from wordcloud import WordCloud, STOPWORDS

stop_words = ['año', 'mil', 'millones', 'pesos', 'ciento', 'El', 'En'] + stop_words_es # Adding additional stop words

# Initiative the word cloud project

amlo_wc = WordCloud(
    background_color='white',
    max_words=2000,
    stopwords=stop_words
)

# Generate the word cloud

amlo_wc.generate(data)

# Display

plt.imshow(amlo_wc, interpolation='bilinear')
plt.axis('off')
plt.show()


#Retrieving the image for the mask
url_image = "https://raw.githubusercontent.com/PhinanceScientist/AMLO_Wordcloud/master/test.png" #Out mask image
#save mask to mx_mask
mx_mask = np.array(Image.open(r'C:\Users\Administrador\Documents\7_PLATZI\IMAGES\test.png'))

fig = plt.figure()
fig.set_figwidth(14)
fig.set_figheight(18)
plt.imshow(mx_mask, interpolation='bilinear')
plt.axis('off')
plt.show()

# instantiate a word cloud object
amlo_wc = WordCloud(background_color='white', max_words=2000, mask=mx_mask, stopwords=stop_words)

# generate the word cloud
amlo_wc.generate(data)

# display the word cloud
fig = plt.figure()
fig.set_figwidth(14)
fig.set_figheight(18)
plt.imshow(amlo_wc, interpolation='bilinear')
plt.axis('off')
plt.show()