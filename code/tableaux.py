#imported libraries
import pandas as pd
import string
import time
import os

#imported files
import scores as scores
import stats as stats
import auxiliaires as aux
import hillclimbing as hc
import recuitsimule as rs

#global variable
caracteristiques = ("", 0, string.ascii_uppercase, string.ascii_uppercase, 100,
                    1, 200, 10, 1000, 0.0)


data = []
repertoire_entree = "repertoire"
#repertoire_sortie = "res"

for nom_fichier in os.listdir(repertoire_entree):

  chemin_entree = os.path.join(repertoire_entree, nom_fichier)
  if nom_fichier[1] == 'h':
    with open(chemin_entree, "r") as f:
      contenu = f.read()
      # diviser le nom de fichier en trois parties
      parties = nom_fichier.split("_")
      nom_cle = "repertoire/clef" + nom_fichier[7:]
      with open(nom_cle, "r") as file:
        cle = file.read()

      
      #cas fonction d'evaluation score_ngram
      for i in range(1,5):
        if i==1:
          ngram_stats = stats.monograms_stats
          score = scores.score_1gram
        elif i==2:
          ngram_stats = stats.bigrams_stats
          score = scores.score_2gram
        elif i==3:
          ngram_stats = stats.trigrams_stats
          score = scores.score_3gram
        else :
          ngram_stats = stats.quatregrams_stats
          score = scores.score_4gram
        
        
      #cas fonction d'evaluation score_pearson
      """ 
      score = scores.score_pearson
      """
        #indentation : si fonction d'évaluation score_ngram : dans la boucle for i in ... ; sinon non
      for j in range(10):
        start = time.time()
        
        #cas methode de dechiffrement hill_climbing
         
        dechiffrement = hc.hill_climbing(contenu, score, 2000, 250)
        
        
        #cas methode de dechiffrement recuit_simule_paliers
  
        """dechiffrement = rs.recuit_simule_paliers(contenu, score, 1000, 100, 0.8, 1)"""
    
        end = time.time()
        nom, taille, cle_u, cle_t, lettres_com, ngram_u, nb_it, nb_max_it, score_f, temps= stats.caracteristiques
        temps = end - start
        nom = nom_fichier
        """
        #cas fonction d'evaluation score_pearson
        ngram_u = 1
        """
        
        #cas fonction d'evaluation score_ngram 
        ngram_u = i
          
          
        taille = int(parties[3])
        cle_u = cle
        lettres_com = aux.evaluation_lettres_en_commun(contenu, cle_t, cle_u)
        print("texte dechiffre ",j ," :", dechiffrement)
        data.append([nom, taille, cle_u, cle_t, lettres_com, ngram_u, nb_it, nb_max_it, score_f, temps])
    
df = pd.DataFrame(data,
                  columns=[
                    'nom', 'taille', 'cle_utilisee', 'cle_trouvee',
                    '%_caracteres_egaux', 'ngram_utilise',
                    'nb_iterations', 'nbmax_iter', 'score_final', 'temps'
                  ])
df.to_csv('tableau.csv', index=False)
