#imported libraries
import random
import string

#imported files
import stats
import auxiliaires as aux

def hill_climbing(text, score, MAXiter, MAXsurplace, key=string.ascii_uppercase, *args):

  nom, taille, cle_u, cle_t, lettres_com, ngram_u, nbmax_it, nb_it, score_f, temps = stats.caracteristiques

  current_text = text
  optimized_text = text
  optimized_score = score(optimized_text,aux.convertir_clef(key), *args)
  clef =key
  
  i = 0
  surplace = 0
  while  i < MAXiter and surplace < MAXsurplace:
    indice1 = random.randint(0, 25)
    indice2 = random.randint(0, 25)
    while (indice1 == indice2):
      indice2 = random.randint(0, 25)
    if(indice1>indice2) :
      indice1, indice2 = indice2, indice1
      
    current_text = aux.permutation(clef[indice1], clef[indice2], current_text)
    clef_temp =clef[:indice1]+clef[indice2]+clef[indice1+1:indice2]+clef[indice1]+clef[indice2+1:]
    current_score = score(current_text, aux.convertir_clef(clef_temp), *args) 

    if current_score >= optimized_score:
      optimized_text = current_text
      optimized_score = current_score
      surplace = 0
      clef = clef_temp
    else: 
      current_text = optimized_text
      surplace += 1
    i += 1
    
  print("Le score final apres ", i, " iterations est ", optimized_score)
  print("On a stagné ", surplace, " fois")

  score_f = optimized_score 
  cle_t = aux.convertir_clef(clef)
  nbmax_it = MAXiter
  nb_it = i
  stats.caracteristiques = (nom, taille, cle_u, cle_t, lettres_com, ngram_u, nbmax_it, nb_it, score_f, temps)

  return optimized_text
