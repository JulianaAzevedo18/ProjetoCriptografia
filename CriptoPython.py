import getpass

def existeCadastro(acesso):
    arquivo = open('cadastro.txt','r')
    a = []
    for line in arquivo:
        a.append(line[line.index('['):line.index("+")])
    if(acesso in a):
        return True
    else:
        return False

def existeLogin(acesso):
    arquivo = open('cadastro.txt','r')
    a = []
    for line in arquivo:
        a.append(line[0:line.index("@")])
    if(acesso in a):
        return True
    else:
        return False
    

def criptografa(coluna, text):
        cripto = []
        for i in range(len(text)):
                linha = (list(text)[i])
                if(linha == "A"):
                    alf = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","@"," "]
                    cripLetra = (alf[coluna])
                    cripto.append(cripLetra)
                elif(linha == "B"):
                    alf = ["B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","@"," ","A"]
                    cripLetra = (alf[coluna])
                    cripto.append(cripLetra)
                elif(linha == "C"):
                    alf = ["C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","@"," ","A","B"]
                    cripLetra = (alf[coluna])
                    cripto.append(cripLetra)
                elif(linha == "D"):
                    alf = ["D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","@"," ","A","B","C"]
                    cripLetra = (alf[coluna])
                    cripto.append(cripLetra)
                elif(linha == "E"):
                    alf = ["E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","@"," ","A","B","C","D"]
                    cripLetra = (alf[coluna])
                    cripto.append(cripLetra)
                elif(linha == "F"):
                    alf = ["F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","@"," ","A","B","C","D","E"]
                    cripLetra = (alf[coluna])
                    cripto.append(cripLetra)
                elif(linha == "G"):
                    alf = ["G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","@"," ","A","B","C","D","E","F"]
                    cripLetra = (alf[coluna])
                    cripto.append(cripLetra)
                elif(linha == "H"):
                    alf = ["H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","@"," ","A","B","C","D","E","F","G"]
                    cripLetra = (alf[coluna])
                    cripto.append(cripLetra)
                elif(linha == "I"):
                    alf = ["I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","@"," ","A","B","C","D","E","F","G","H"]
                    cripLetra = (alf[coluna])
                    cripto.append(cripLetra)
                elif(linha == "J"):
                    alf = ["J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","@"," ","A","B","C","D","E","F","G","H","I"]
                    cripLetra = (alf[coluna])
                    cripto.append(cripLetra)
                elif(linha == "K"):
                    alf = ["K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","@"," ","A","B","C","D","E","F","G","H","I","J"]
                    cripLetra = (alf[coluna])
                    cripto.append(cripLetra)
                elif(linha == "L"):
                    alf = ["L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","@"," ","A","B","C","D","E","F","G","H","I","J","K"]
                    cripLetra = (alf[coluna])
                    cripto.append(cripLetra)
                elif(linha == "M"):
                    alf = ["M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","@"," ","A","B","C","D","E","F","G","H","I","J","K","L"]
                    cripLetra = (alf[coluna])
                    cripto.append(cripLetra)
                elif(linha == "N"):
                    alf = ["N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","@"," ","A","B","C","D","E","F","G","H","I","J","K","L","M"]
                    cripLetra = (alf[coluna])
                    cripto.append(cripLetra)
                elif(linha == "O"):
                    alf = ["O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","@"," ","A","B","C","D","E","F","G","H","I","J","K","L","M","N"]
                    cripLetra = (alf[coluna])
                    cripto.append(cripLetra)
                elif(linha == "P"):
                    alf = ["P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","@"," ","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O"]
                    cripLetra = (alf[coluna])
                    cripto.append(cripLetra)
                elif(linha == "Q"):
                    alf = ["Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","@"," ","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P"]
                    cripLetra = (alf[coluna])
                    cripto.append(cripLetra)
                elif(linha == "R"):
                    alf = ["R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","@"," ","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q"]
                    cripLetra = (alf[coluna])
                    cripto.append(cripLetra)
                elif(linha == "S"):
                    alf = ["S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","@"," ","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R"]
                    cripLetra = (alf[coluna])
                    cripto.append(cripLetra)
                elif(linha == "T"):
                    alf = ["T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","@"," ","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S"]
                    cripLetra = (alf[coluna])
                    cripto.append(cripLetra)
                elif(linha == "U"):
                    alf = ["U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","@"," ","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T"]
                    cripLetra = (alf[coluna])
                    cripto.append(cripLetra)
                elif(linha == "V"):
                    alf = ["V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","@"," ","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U"]
                    cripLetra = (alf[coluna])
                    cripto.append(cripLetra)
                elif(linha == "W"):
                    alf = ["W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","@"," ","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V"]
                    cripLetra = (alf[coluna])
                    cripto.append(cripLetra)
                elif(linha == "X"):
                    alf = ["X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","@"," ","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W"]
                    cripLetra = (alf[coluna])
                    cripto.append(cripLetra)
                elif(linha == "Y"):
                    alf = ["Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","@"," ","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X"]
                    cripLetra = (alf[coluna])
                    cripto.append(cripLetra)
                elif(linha == "Z"):
                    alf = ["Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","@"," ","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y"]
                    cripLetra = (alf[coluna])
                    cripto.append(cripLetra)
                elif(linha == "a"):
                    alf = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","@"," ","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
                    cripLetra = (alf[coluna])
                    cripto.append(cripLetra)
                elif(linha == "b"):
                    alf = ["b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","@"," ","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a"]
                    cripLetra = (alf[coluna])
                    cripto.append(cripLetra)
                elif(linha == "c"):
                    alf = ["c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","@"," ","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b"]
                    cripLetra = (alf[coluna])
                    cripto.append(cripLetra)
                elif(linha == "d"):
                    alf = ["d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","@"," ","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c"]
                    cripLetra = (alf[coluna])
                    cripto.append(cripLetra)
                elif(linha == "e"):
                    alf = ["e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","@"," ","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d"]
                    cripLetra = (alf[coluna])
                    cripto.append(cripLetra)
                elif(linha == "f"):
                    alf = ["f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","@"," ","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e"]
                    cripLetra = (alf[coluna])
                    cripto.append(cripLetra)
                elif(linha == "g"):
                    alf = ["g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","@"," ","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f"]
                    cripLetra = (alf[coluna])
                    cripto.append(cripLetra)
                elif(linha == "h"):
                    alf = ["h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","@"," ","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g"]
                    cripLetra = (alf[coluna])
                    cripto.append(cripLetra)
                elif(linha == "h"):
                    alf = ["h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","@"," ","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g"]
                    cripLetra = (alf[coluna])
                    cripto.append(cripLetra)
                elif(linha == "i"):
                    alf = ["i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","@"," ","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h"]
                    cripLetra = (alf[coluna])
                    cripto.append(cripLetra)
                elif(linha == "j"):
                    alf = ["j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","@"," ","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i"]
                    cripLetra = (alf[coluna])
                    cripto.append(cripLetra)
                elif(linha == "k"):
                    alf = ["k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","@"," ","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j"]
                    cripLetra = (alf[coluna])
                    cripto.append(cripLetra)
                elif(linha == "l"):
                    alf = ["l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","@"," ","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k"]
                    cripLetra = (alf[coluna])
                    cripto.append(cripLetra)
                elif(linha == "m"):
                    alf = ["m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","@"," ","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l"]
                    cripLetra = (alf[coluna])
                    cripto.append(cripLetra)
                elif(linha == "n"):
                    alf = ["n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","@"," ","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m"]
                    cripLetra = (alf[coluna])
                    cripto.append(cripLetra)
                elif(linha == "o"):
                    alf = ["o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","@"," ","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n"]
                    cripLetra = (alf[coluna])
                    cripto.append(cripLetra)
                elif(linha == "p"):
                    alf = ["p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","@"," ","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o"]
                    cripLetra = (alf[coluna])
                    cripto.append(cripLetra)
                elif(linha == "q"):
                    alf = ["q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","@"," ","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p"]
                    cripLetra = (alf[coluna])
                    cripto.append(cripLetra)
                elif(linha == "r"):
                    alf = ["r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","@"," ","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q"]
                    cripLetra = (alf[coluna])
                    cripto.append(cripLetra)
                elif(linha == "s"):
                    alf = ["s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","@"," ","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r"]
                    cripLetra = (alf[coluna])
                    cripto.append(cripLetra)
                elif(linha == "t"):
                    alf = ["t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","@"," ","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s"]
                    cripLetra = (alf[coluna])
                    cripto.append(cripLetra)
                elif(linha == "u"):
                    alf = ["u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","@"," ","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t"]
                    cripLetra = (alf[coluna])
                    cripto.append(cripLetra)
                elif(linha == "v"):
                    alf = ["v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","@"," ","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u"]
                    cripLetra = (alf[coluna])
                    cripto.append(cripLetra)
                elif(linha == "w"):
                    alf = ["w","x","y","z","0","1","2","3","4","5","6","7","8","9","@"," ","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v"]
                    cripLetra = (alf[coluna])
                    cripto.append(cripLetra)
                elif(linha == "x"):
                    alf = ["x","y","z","0","1","2","3","4","5","6","7","8","9","@"," ","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w"]
                    cripLetra = (alf[coluna])
                    cripto.append(cripLetra)
                elif(linha == "y"):
                    alf = ["y","z","0","1","2","3","4","5","6","7","8","9","@"," ","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x"]
                    cripLetra = (alf[coluna])
                    cripto.append(cripLetra)
                elif(linha == "z"):
                    alf = ["z","0","1","2","3","4","5","6","7","8","9","@"," ","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y"]
                    cripLetra = (alf[coluna])
                    cripto.append(cripLetra)
                elif(linha == "0"):
                    alf = ["0","1","2","3","4","5","6","7","8","9","@"," ","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
                    cripLetra = (alf[coluna])
                    cripto.append(cripLetra)
                elif(linha == "1"):
                    alf = ["1","2","3","4","5","6","7","8","9","@"," ","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0"]
                    cripLetra = (alf[coluna])
                    cripto.append(cripLetra)
                elif(linha == "2"):
                    alf = ["2","3","4","5","6","7","8","9","@"," ","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1"]
                    cripLetra = (alf[coluna])
                    cripto.append(cripLetra)
                elif(linha == "3"):
                    alf = ["3","4","5","6","7","8","9","@"," ","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2"]
                    cripLetra = (alf[coluna])
                    cripto.append(cripLetra)
                elif(linha == "4"):
                    alf = ["4","5","6","7","8","9","@"," ","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3"]
                    cripLetra = (alf[coluna])
                    cripto.append(cripLetra)
                elif(linha == "5"):
                    alf = ["5","6","7","8","9","@"," ","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4"]
                    cripLetra = (alf[coluna])
                    cripto.append(cripLetra)
                elif(linha == "6"):
                    alf = ["6","7","8","9","@"," ","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5"]
                    cripLetra = (alf[coluna])
                    cripto.append(cripLetra)
                elif(linha == "7"):
                    alf = ["7","8","9","@"," ","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6"]
                    cripLetra = (alf[coluna])
                    cripto.append(cripLetra)
                elif(linha == "8"):
                    alf = ["8","9","@"," ","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7"]
                    cripLetra = (alf[coluna])
                    cripto.append(cripLetra)
                elif(linha == "9"):
                    alf = ["9","@"," ","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8"]
                    cripLetra = (alf[coluna])
                    cripto.append(cripLetra)
                elif(linha == "@"):
                    alf = ["@"," ","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9"]
                    cripLetra = (alf[coluna])
                    cripto.append(cripLetra)
                else:
                    alf = [" ","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","@"]
                    cripLetra = (alf[coluna])
                    cripto.append(cripLetra)
        return cripto

def pegaColuna():
        return coluna
def pegaLogin():
        return login

print("***********************************************************************************************************************************")
print("***********************************************************************************************************************************")
print("***********************************************************************************************************************************")
print("***********************************************************************************************************************************")
print("***                                                                                                                             ***")
print("***                                              BEM VINDO AO CRIPTOPYTHON                                                      ***")
print("***                                                                                                                             ***")
print("***                                                                                                                             ***")
print("***                                                                                                                             ***")
print("***                                                                                                                             ***")
print("*** - DIGITE 1 PARA CADASRAR USUÁRIOS:                                                                                          ***")
print("*** - DIGITE 2 PARA LOGAR NO SISTEMA E ACESSO:                                                                                  ***")
opcao = str(input("*** - SELECIONE A OPÇÃO : "))
while(opcao != "2" and opcao != "1"):
                print("*** - A OPÇÃO ESCOLHIDA NÃO EXISTE !!! ")
                opcao = str(input("*** - SELECIONE A OPÇÃO: "))
if(opcao == "1"):
        print("***                                                                                                                             ***")
        print("***                                                                                                                             ***")
        print("*** -------------------------->  BEM VINDO AO CADASTRAMENTO DE USUÁRIOS  ...                                                    ***")
        print("***                                                                                                                             ***")
        print("***                                                                                                                             ***")
        print("*** - SÃO PERMITIDOS OS CARACTERES DO ALFABETO, NÚMERICOS E TAMBÉM @ OU ESPAÇO, APENAS !                                        ***")
        print("***                                                                                                                             ***")
        print("***                                                                                                                             ***")
        print("***                                                                                                                             ***")


        apenasnum = 0
        while(apenasnum == 0):
            coluna = input("*** - ESCOLHA SUA CHAVE DE CRIPTOGRAFIA - (EXISTEM APENAS AS CHAVES DE 1 ATÉ 63  !!!): ")
            if((coluna.isdigit() == False) or int(coluna) <1 or int(coluna) > 63):
                print("*** - LETRAS NÃO SÃO PERMITIDAS, NEM NÚMEROS FORA DO INTERVALO DE 1 À 63 - DIGITE NOVAMENTE ..." )
                apenasnum = 0
            else:
                apenasnum = 1
        
        
        
        gatilho = False
        gatilho2 = 0
        gatilho3 = 0
        while(gatilho3 == 0):
            gatilho2 = 0
            while(gatilho2 == 0):
                login = str(input("*** - CADASTRE O SEU NOME DE USUÁRIO: "))
                for i in range(len(login)):
                           alfP = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","@"," "] 
                           if(login[i] in alfP):
                               print("*** - Validando....")
                               gatilho = True
                           else:
                               print("*** - UTILIZE APENAS CARACTERES VÁLIDOS PARA CRIAR SENHA! : ")
                               gatilho = False
                               break
                if(gatilho == True):
                    gatilho2 = 1
                else:
                    gatilho2 = 0
            if(existeLogin(login) == True):
                print("*** - ESTE LOGIN JÁ EXISTE, FAVOR ESCOLHER OUTRO ! ")
                gatilho3 = 0
            else:
                gatilho3 = 1
            
        val = False
        fim = 0
        while(fim == 0):
            senha = str(input("*** - CADASTRE SUA SENHA DE ACESSO: "))
            for i in range(len(senha)):
                       alfP = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","@"," "] 
                       if(senha[i] in alfP):
                           print("*** - Validando....")
                           val = True
                       else:
                           print("*** - DIGITE APENAS CARACTERES PERMITIDOS PARA CRIAÇÃO DE SENHA! ")
                           val = False
                           break
            if(val == True):
                fim = 1
            else:
                fim = 0

                
        acesso = senha        
        
        arquivo = open('cadastro.txt','r')
        texto = arquivo.read()
        arquivo.close

        
        textoNovo = (texto + "\n" + login  + "@" + str(criptografa(int(coluna), login)) + str(criptografa(int(coluna), acesso)))
        mais = (textoNovo + "+")

        
        arquivo = open('cadastro.txt','w')
        texto = mais
        arquivo.writelines(texto)
        arquivo.close()
        print("*** - ACESSO CADASTRADO COM SUCESSO !!! \n \n \n \n \n")



        from time import sleep
        print("programa fechará em 10 segundos ....... ")
        sleep(10)
else:
        print("***********************************************************************************************************************************")
        print("***********************************************************************************************************************************")
        print("***********************************************************************************************************************************")
        print("***********************************************************************************************************************************")
        print("***                                                                                                                             ***")
        print("***                          BEM VINDO AO SISTEMA DE ACESSO DO COMPARTIMENTO XXXX DO NAVIO                                      ***")
        print("***                                                                                                                             ***")
        print("***                                                                                                                             ***")
        print("***                                                                                                                             ***")
        print("***                                                                                                                             ***")
        print("***                                                                                                                             ***")
        print("***                                                                                                                             ***")
        print("***                                                                                                                             ***")

        gatilho = 0
        while(gatilho == 0):
            apenasnum = 0
            while(apenasnum == 0):
                coluna = input("*** - ESCOLHA SUA CHAVE DE CRIPTOGRAFIA - (EXISTEM APENAS AS CHAVES DE 1 ATÉ 63  !!!): ")
                if((coluna.isdigit() == False) or int(coluna) <1 or int(coluna) > 63):
                    print("*** - LETRAS NÃO SÃO PERMITIDAS, NEM NÚMEROS FORA DO INTERVALO DE 1 À 63 - DIGITE NOVAMENTE ..." )
                    apenasnum = 0
                else:
                    apenasnum = 1
        
            loginAcesso = str(input("*** - LOGIN: "))
            senhaAcesso = getpass.getpass('*** - SENHA: ºººººººº')
            for i in range(len(senhaAcesso)):
                           alfP = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","@"," "] 
                           while(senhaAcesso[i] not in alfP):
                                   print("Digite Apenas caracteres válidos para senha")
                                   senhaAcesso.clear()
                                   senhaAcesso = getpass.getpass(prompt='*** - SENHA: : ')
                                   
            acesso = (str(criptografa(int(coluna), loginAcesso))) + (str(criptografa(int(coluna), senhaAcesso)))
            if(existeCadastro(acesso) == True):
                    print("*** - ACESSO LIBERADO - BEM VINDO, "+ loginAcesso +"!!! \n\n\n\n")
                    print("         ***")
                    print("         ***")
                    print("         ***")
                    print("        ***********")
                    print("        **.......**")
                    print("        **:     :**")
                    print("        **:     :**")
                    print("        **.......**")
                    print("        ***********")
                    print("*********************************************")
                    print(" *******************************************")
                    print("  ****************CRIPTOPYTHON*************")
                    print("   ***************************************")
                    print("    *************************************")
                    print("  -- _ -- _ -- _  -  _  --- _-- _ -- _ -- _  -  _  --- ___- ")
                    print("  -- _ -- _ -- _  -__- -- _ -- _ -- _  -  _  --- ___- __- ")
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

                    gatilho = 1
            else:
                    print("ACESSO NEGADO - TENTE NOVAMENTE ...")
                    gatilho = 0
                    
        from time import sleep
        print("programa fechará em 10 segundos ....... ")
        sleep(10)



