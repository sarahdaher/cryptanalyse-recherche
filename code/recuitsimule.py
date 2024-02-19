#imported libraries
import numpy as np
import random
import string

#imported files
import stats
import auxiliaires as aux


def recuit_simule_paliers(text, score,T,nbiter_dans_palier,c,Tmin,key=string.ascii_uppercase, *args):
  nom, taille, cle_u, cle_t, lettres_com, ngram_u, nb_it, score_f, temps, other = stats.caracteristiques
  best_text = text
  best_score = score(best_text, aux.convertir_clef(key), *args)
  current_text = text
  optimized_text = text
  optimized_score = best_score
  clef = key
  r = 1

  nbiter = 0
  while T > Tmin:  #on peut ajouter des conditions de sortie : MAXiter..
    indice1 = random.randint(0, 25)
    indice2 = random.randint(0, 25)
    while (indice1 == indice2):
      indice2 = random.randint(0, 25)
    if (indice1 > indice2):
      indice1, indice2 = indice2, indice1

    current_text = aux.permutation(clef[indice1], clef[indice2], current_text)
    clef_temp = clef[:indice1] + clef[indice2] + clef[indice1 + 1:indice2] + clef[indice1] + clef[indice2 + 1:]
    current_score = score(current_text, aux.convertir_clef(clef_temp), *args)

    diff = current_score - optimized_score
    if diff < 0:
      r = random.random()
    if diff >= 0 or r < np.exp(diff / T):
      optimized_text = current_text
      optimized_score = current_score
      clef = clef_temp
      if best_score < optimized_score:
        best_text = optimized_text
        best_score = optimized_score
    else:
      current_text = optimized_text

    nbiter += 1
    if nbiter % nbiter_dans_palier == 0:
      T = c * T

  score_f = best_score
  cle_t = aux.convertir_clef(clef)
  nb_it = nbiter
  stats.caracteristiques = (nom, taille, cle_u, cle_t, lettres_com, ngram_u, nb_it, score_f, temps, other)

  return best_text
