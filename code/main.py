
#imported files
import scores as scores
import hillclimbing as hc
import recuitsimule as rs

algo = input("Choisissez une  metaheuristique (recuitsimule , hillclimbing ou recuitsimule_et_hillclimbing) : ")
score_txt = input("Choisissez une fonction score (ngram ou pearson) : ")
texte = input("Entrez le texte : ")

if score_txt == "ngram":
    choix = int(input("Choisissez un n (entre 1 et 4) : "))
    if choix == 1:
        score = scores.score_1gram
    elif choix == 2:
        score = scores.score_2gram
    elif choix == 3:
        score = scores.score_3gram
    elif choix == 4:
        score = scores.score_4gram

elif score_txt == "pearson":
    score = scores.score_pearson
else:
  print("La fonction score", score_txt, "n'est pas definie")
  exit(1)


if algo == "recuitsimule":
  choix_param = int(input("Vouliez- vous choisir les paramètres? Tapez 1 si oui, 2 si vous voulez les paramètres optimaux: "))
  if choix_param == 1:
    T = float(input("Entrez la valeur de T initial : "))
    nbiter_dans_palier = int(input("Entrez le nombre d'itérations dans un palier : "))
    c = float(input("Entrez la valeur de c : "))
    Tmin = float(input("Entrez la température minimale : "))
    print("Texte déchiffré avec recuit simulé: ", rs.recuit_simule_paliers(texte, score, T, nbiter_dans_palier, c, Tmin))
  elif choix_param == 2:
    print("Texte déchiffré avec recuit simulé: ", rs.recuit_simule_paliers(texte, score, 1000, 100, 0.8, 1))
    

elif algo == "hillclimbing":
  choix_param = int(input("Vouliez- vous choisir les paramètres? Tapez 1 si oui, 2 si vous voulez les paramètres optimaux: "))
  if choix_param == 1:
    MAXiter = int(input("Entrez le nombre maximum d'itérations : "))
    MAXsurplace = int(input("Entrez le nombre maximum de stagnations : "))
    print("Texte déchiffré avec hill climbing: ", hc.hill_climbing(texte, score, MAXiter, MAXsurplace))
  if choix_param == 2:
     print("Texte déchiffré avec hill climbing: ", hc.hill_climbing(texte,score, 2000, 250))
    
elif algo =="recuitsimule_et_hillclimbing":
  choix_param = int(input("Vouliez- vous choisir les paramètres? Tapez 1 si oui, 2 si vous voulez les paramètres optimaux: "))
  if choix_param == 1:
    T = float(input("Entrez la valeur de T initial : "))
    nbiter_dans_palier = int(input("Entrez le nombre d'itérations dans un palier : "))
    c = float(input("Entrez la valeur de c : "))
    Tmin = float(input("Entrez la température minimale : ")) 
    MAXiter = int(input("Entrez le nombre maximum d'itérations : "))
    MAXsurplace = int(input("Entrez le nombre maximum de stagnations : "))
    print("Texte déchiffré avec recuit simulé: ",rs.recuit_simule_paliers(texte, score, T, nbiter_dans_palier, c, Tmin))
    print("Texte déchiffré avec hill climbing: ", hc.hill_climbing(texte, score, MAXiter, MAXsurplace))
  if choix_param == 2:
    print("Texte déchiffré avec hill climbing: ", hc.hill_climbing(texte,score, 2000, 250))
    print("Texte déchiffré avec recuit simulé: ",rs.recuit_simule_paliers(texte, score, 1000, 100, 0.8, 1))

else:
  print("La metaheuristique", algo, "n'est pas definie")
  exit(1)