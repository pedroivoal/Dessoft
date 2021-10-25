#
q1 = input("Já assistiu todos os filmes?")
q2 = input("Tem camiseta temática?")
q3 = input("Já se fantasiou de algum personagem?")
q4 = input("Tem algum action figure/nave/etc?")
q5 = input("Já foi no Galaxy's Edge, o parque temático da franquia?")

if q1==q2 and q2==q3 and q3==q4 and q4==q5 and q1=='sim':
    print("One with the Force")

elif (q1!='sim' and q2!='sim' and q3!='sim' and q4!='sim' and q5!='sim' ) or (q1=='sim' and q2!='sim' and q3!='sim' and q4!='sim' and q5!='sim' )  or (q2=='sim' and q1!='sim' and q3!='sim' and q4!='sim' and q5!='sim' ) or (q3=='sim' and q2!='sim' and q1!='sim' and q4!='sim' and q5!='sim' ) or (q4=='sim' and q2!='sim' and q3!='sim' and q1!='sim' and q5!='sim' ) or (q5=='sim' and q2!='sim' and q3!='sim' and q4!='sim' and q1!='sim' ):
    print("Inocente")

elif (q1=='sim' and q2=='sim' and q3!='sim' and q4!='sim' and q5!='sim' ) or (q1=='sim' and q2!='sim' and q3=='sim' and q4!='sim' and q5!='sim' ) or (q1=='sim' and q2!='sim' and q3!='sim' and q4=='sim' and q5!='sim' ) or (q1=='sim' and q2!='sim' and q3!='sim' and q4!='sim' and q5=='sim' ) or (q1!='sim' and q2=='sim' and q3=='sim' and q4!='sim' and q5!='sim' ) or (q1!='sim' and q2=='sim' and q3!='sim' and q4=='sim' and q5!='sim' ) or (q1!='sim' and q2=='sim' and q3!='sim' and q4!='sim' and q5=='sim' ) or (q1!='sim' and q2!='sim' and q3=='sim' and q4=='sim' and q5!='sim' ) or (q1!='sim' and q2!='sim' and q3=='sim' and q4!='sim' and q5=='sim' ) or (q1!='sim' and q2!='sim' and q3!='sim' and q4=='sim' and q5=='sim' ):
    print("Padawan")

else:
    print("Jedi")

#tem como fazer o código menor?