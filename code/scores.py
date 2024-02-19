#imported libraries
import collections
import numpy as np
import string
import math

#imported files
import auxiliaires as aux
import stats

def score_ngram(text, key, n, ngrams_stats):
  score = 0
  ngram = ""
  for i in range(len(text) - n + 1):
    ngram = text[i:i + n]
    if ngram in ngrams_stats:
      score += np.log(ngrams_stats[ngram])
  return round(score, 2)
  

def score_pearson(text, cle):
 
  alphabet = string.ascii_uppercase
  
  dict_txt = aux.get_ngram_frequencies(text, 1)
  if '\n' in dict_txt:
    del dict_txt['\n']
  dict_fr = stats.monograms_stats

  tot_langue = sum(dict_fr.values())
  freq_fr = [dict_fr[alphabet[i]]/tot_langue for i in range(26)] #frequences des lettres dans la langue francaise
  freq_txt = [dict_txt[cle[i]]/len(text) for i in range(26)] #frequences de leur chiffrement correspondant dans le texte

  freq_fr = np.array(freq_fr)
  freq_txt = np.array(freq_txt)
  
  moy_fr = np.mean(freq_fr)
  moy_txt = np.mean(freq_txt)

  ecart_fr = freq_fr - moy_fr 
  ecart_txt = freq_txt - moy_txt

  return abs( np.sum(ecart_fr * ecart_txt) / np.sqrt(np.sum(ecart_fr**2) * np.sum(ecart_txt**2)) )
  
def score_1gram(text, key):
  return score_ngram(text, key, 1, stats.monograms_stats)


def score_2gram(text, key):
  return score_ngram(text, key, 2, stats.bigrams_stats)


def score_3gram(text, key):
  return score_ngram(text, key, 3, stats.trigrams_stats)

def score_4gram(text, key):
  return score_ngram(text, key,  4, stats.quatregrams_stats)

