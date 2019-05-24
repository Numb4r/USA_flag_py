# 7 linhas de estrelas
# 6 linhas normais depois
# 20 colunas estrelas
# 26 colunas normais
for i in range(1,14):
        for j in range(46):
            if j == 0 or j == 45:
	    	          print("\033[1;37;40m",end="")
            elif i < 8:
                if i%2!=0:
                    if j < 22:
                        if j%2!=0:
                            print("\033[1;37;44m*", end="")
                        else:
                            print("\033[1;34;44m ",end="")
                    else:
                        print("\033[1;31;41m0",end="")
                elif i%2==0:
                    if j< 22:
                        if j%2==0:
                            print("\033[1;37;44m*",end="")
                        else:
                            print("\033[1;34;44m ",end="")
                    else:
                        print("\033[1;37;47m:",end="")
            elif i  > 7:
                if i%2!=0:
                    print("\033[1;31;41m0",end="")
                else:
                    print("\033[1;47;47m:",end="")

        print("")
