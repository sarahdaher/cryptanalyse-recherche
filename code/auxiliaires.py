#imported libraries
import string
import random
import matplotlib.pyplot as plt
from collections import Counter

#ensemble des caracteres spéciaux : voyelles
ens_e = {"è", 'é', 'ê', 'ë', 'ē', 'ė', 'ę', "È", 'É', 'Ê', 'Ë', 'Ē', 'Ė', 'Ę'}
ens_i = {'ï', 'í', 'ī', 'į', 'ì', 'ì', 'Ï', 'Í', 'Ī', 'Į', 'Ì', 'Ì'}
ens_o = {'ö', 'ò', 'ó', 'ø', 'ō', 'õ', 'Ö', 'Ò', 'Ó', 'Ø', 'Ō', 'Õ' }
ens_a = {'à', 'á', 'â', 'ä', 'ã', 'ā', 'å', 'À', 'Á', 'Â', 'Ä', 'Ã', 'Ā', 'Å'}
ens_u = {'û', 'ù', 'ú', 'ū', 'ü', 'Û', 'Ù', 'Ú', 'Ū', 'Ü'}
ens_y = {'ÿ', 'Ÿ'}

#ensemble des caracteres spéciaux : consonnes
ens_c = {'ç', 'Ç'}

#retourne si le caractere est une lettre acceptee par nos algorithmes de dechiffrement
def est_lettre(lettre):
    return ord('a') <= ord(lettre) <=ord('z') or ord('A') <= ord(lettre) <=ord('Z')
    
def min_en_maj(lettre):
    if ord('a') <= ord(lettre) <=ord('z'):
        return lettre.upper()
    else:
        return lettre

#passage en majuscule, suppression de la ponctuation et remplacement des caractères spéciaux par leur lettre équivalente
def nettoyage(nom_fichier):
    res = ""
    with open(nom_fichier, 'r', encoding="utf8") as fichier:
        texte = fichier.read()
    for i in range(len(texte)):
            if texte[i] in ens_e:
                res += 'E'
            elif texte[i] in ens_i:
                res += 'I'
            elif texte[i] in ens_o:
                res += 'O'
            elif texte[i] in ens_a:
                res += 'A'
            elif texte[i] in ens_c:
                res += 'C'
            elif texte[i] in ens_u:
                res += 'U'
            elif texte[i] in ens_y:
                res += 'Y'
            elif texte[i] == 'œ' or texte[i] == 'Œ':
                res += 'OE'
            elif texte[i] == 'æ' or texte[i] == 'Æ':
                res += "AE"
            elif est_lettre(texte[i]):
                res += min_en_maj(texte[i])
    return res


# a utiliser dans hill climbing : permuter tous les A d'un texte en B
def permutation(A, B, texte):
  texte_res = ""
  for i in range(len(texte)):
    if texte[i] == A:
      texte_res += B
    elif texte[i] == B:
      texte_res += A
    else:
      texte_res += texte[i]
  return texte_res


# a utiliser dans chiffrement aleatoire :  renvoie un dictionnaire contenant une clé de chiffrement aléatoire
def substitution_aleatoire():
  alphabet = string.ascii_uppercase
  alphabet_list = list(alphabet)
  # Mélanger la liste des lettres aléatoirement
  random.shuffle(alphabet_list)
  # Créer un dictionnaire de substitution aléatoire
  substitution_dict = {}
  for i in range(len(alphabet)):
    substitution_dict[alphabet[i]] = alphabet_list[i]
  return substitution_dict


# chiffre un texte donné pour pouvoir appliquer notre algorithme
def chiffrement_aleatoire(text):
  substitution = substitution_aleatoire()
  texte_chiffre = ''
  for c in text:
    texte_chiffre += substitution[c]
  return texte_chiffre

# renvoie un dictionnaire (ngram : occurences) (utilise dans score et dans les stats)
def get_ngram_frequencies(text, n):
  alphabet ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  ngrams = []
  for i in range(len(text) - n + 1):
    ngrams.append(text[i:i + n])
  for s in alphabet:
    if s not in ngrams:
      ngrams.append(s)
  ngram_counts = Counter(ngrams)
  return dict(ngram_counts)


def evaluation_lettres_en_commun(text, clef_text, clef_original):
  cpt = 0
  lettres = set(text)
  n = len(set(text))

  for i in range(26):
    if clef_text[i] == clef_original[i] and clef_text[i] in lettres:
      cpt += 1
  return round(100 * cpt / n, 2)


def convertir_clef(clef):
  #prend une clef de déchiffrement en majuscules et renvoie la clef de chiffrement correspondante
  alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  res = ""

  for lettre in alphabet:

    # Trouver l'index de la lettre correspondante dans la clé de déchiffrement
    index = clef.find(lettre)
    # Ajouter la lettre correspondante dans l'alphabet à la clé de chiffrement
    res += alphabet[index]

  return res

#trace un histogramme ordonne par ordre d'occurences croissant sur les dictionnaires de ngrams
def histogramme_ordonne(dico):
    dico_ordonne=dict(sorted(dico.items(), key=lambda item: item[1]))
    lettres=[cle for cle in dico_ordonne]
    frequences=[dico[cle] for cle in dico_ordonne]
    plt.figure(figsize=[26,13])
    plt.bar(lettres,frequences)
    plt.title('nombres d occurences des lettres par ordre croissant')
    plt.savefig("Histogramme_ordonne.png",dpi=300);
    plt.show();
