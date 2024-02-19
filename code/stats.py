#imported libraries
import string
import json

# initialisation des dictionaires de statistiques (ngrams : occurences) faites sur le texte "Les misérables" qu'on a nettoyé avant

with open('statistiques_monogrammes.json', 'r') as f:
  monograms_stats = json.load(f)

with open('statistiques_bigrammes.json', 'r') as f:
  bigrams_stats = json.load(f)

with open('statistiques_trigrammes.json', 'r') as f:
  trigrams_stats = json.load(f)

with open('statistiques_4grammes.json', 'r') as f:
  quatregrams_stats = json.load(f)

#global variable
caracteristiques = ("", 0, string.ascii_uppercase, string.ascii_uppercase, 100, 1, 200, 10, 1000, 0.0)