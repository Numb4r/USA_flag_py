# 7 linhas de estrelas
# 6 linhas normais depois
# 20 colunas estrelas
# 26 colunas normais
for i in range(1,14):
        for j in range(46):
            if j == 0 or j == 45:
                print("|",end="")
            elif i < 8:
                if i%2!=0:
                    if j < 22:
                        if j%2!=0:
                            print("*", end="")
                        else:
                            print(" ",end="")
                    else:
                        print("0",end="")
                elif i%2==0:
                    if j< 22:
                        if j%2==0:
                            print("*",end="")
                        else:
                            print(" ",end="")
                    else:
                        print(":",end="")
            elif i  > 7:
                if i%2!=0:
                    print("0",end="")
                else:
                    print(":",end="")

        print("")
