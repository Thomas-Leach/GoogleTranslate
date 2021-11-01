#@title
%%capture
!pip install googletrans==4.0.0-rc1


import googletrans
from googletrans import Translator
import random

translator = Translator() 
langsdict = googletrans.LANGUAGES


def randtrans(text,lang): 
  langsdict = googletrans.LANGUAGES
  langs = [*googletrans.LANGUAGES]
  nlang = langs[random.randint(0,len(langs)-1)]
  translation = translator.translate(text, dest=nlang, src=lang) 
  return getattr(translation,'text'), nlang

def main(): 
  prompt = input('Text: ') 
  lang = 'en'
  iters = int(input('Translations: '))
  
  text = prompt
  langlis = ['English',"→"]
  for i in range(iters): 
    trans = randtrans(text,lang)
    text = trans[0]
    lang = trans[1]
    langlis.append(langsdict[lang].capitalize())
    langlis.append("→")
      
  print()
  translation = translator.translate(text, dest='en', src=lang) 
  print(getattr(translation,'text'))
  print(' '.join(langlis), "English")
