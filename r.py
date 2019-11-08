from math import *


#liste des donnees
ls = [4,5,5,7,8,9,10,10,11,15,40]


#calcule la sommes de tous les element de la donnee
sum_ls = sum(ls)
print("{} = {}\n".format(ls,sum_ls))


#compte le nombre d'element dans la donnee
totol_elem = len(ls)



#calcule de la sommes des carres des ecarts
n_ls = []
print("Calcule chaque element par la sommes des donnees diviser par le nombre total d'element le tout au carree \n")
for i in ls:
    res= pow(i - (sum_ls/totol_elem), 2)
    print("({} - {}) ^ 2 =".format(i, round(sum_ls/totol_elem, 2)), round(res, 2))
    n_ls.append(res)

print("\n")

#compte la sommes des carres des ecarts
total_sum_pow = sum(n_ls)
print("Total des sommes des carres des ecart :", round(total_sum_pow, 2))
print()
#calcule de la Variance -> calcule des somme des carrés des écarts par le nombre de degrés de liberté
variance = 1/totol_elem * total_sum_pow
print("Variance : 1 / {} * {} = {}".format(totol_elem,round(total_sum_pow,2),round(variance,2)))
print()

#calcule de l'ecart type : c'est la racine carree de la variance
ecarType = sqrt(variance)
print("Ecart type : racine carree de la variance = {}".format(round(ecarType, 2)))
