magas = ["e","é","i","í","ü","ű","ö","ő"]
mély = ["a","á","o","ó","u","ú"]



szavak = ["rózsa", "alma", "körte", "burgonya", "sütemény", "gyerek", "iskola", "tanár", "hal", "bor", "sárkány", "portálfegyver", "dimenziókapu"]
ragok = ["nak", "nek"]
valvel =["val","vel"]

def elso():
 print("Első feladat")
 print("")
 for szo in szavak:
      for maganhangzo in mély:
         if maganhangzo in szo:
             print(szo+ragok[0])
             break
         else:
            continue
         for maganhangzo in magas:
            if maganhangzo in szo:
                print(szo+ragok[1])
                break
            else:
               continue

 print("")
             

myNumbers = [1, 5, 12, 0, -2, 91, -12, 30, 32]

def masodik():
    print("Második feladat")
    print("")
    myNumbers.sort()
    print(myNumbers[0])
    print(myNumbers[-1])
    print("")

def harmadik():
 print("Harmadik feladat")
 print("")
 for szo in szavak:
      for maganhangzo in mély:
         if maganhangzo in szo:
             #print(szo)
             utolsobetu = szo[-1]
             if utolsobetu == "a":
                 ujszo=szo.replace(utolsobetu,"á")
                 print(ujszo+ragok[0])
                 break
             else:
                 print(szo+ragok[0])
                 break   
         else:
            continue
         for maganhangzo in magas:
            if maganhangzo in szo:
                #print(szo)
                utolsobetu = szo[-1]
                if utolsobetu == "e":
                     ujszo=szo.replace(utolsobetu,"é")
                     print(ujszo+ragok[1])
                     break
            else:
                   continue
 print("")

def negyedik():
 print("Negyedik feladat")
 print("")
 for szo in szavak:
      for maganhangzo in mély:
         if maganhangzo in szo:
             #print(szo)
             utolsobetu = szo[-1]
             ujrag = valvel[0]
             if utolsobetu == "a":
                 ujszo=szo.replace(utolsobetu,"á")
                 print(ujszo+ujrag)
                 break
             if utolsobetu in mély:
                 ujszo=szo+ujrag
                 print (ujszo)
                 break
             if utolsobetu not in mély:
                 ujszo=szo+ujrag.replace("v",utolsobetu)
                 print (ujszo)
                 break
             else:
                 print(szo+valvel[0])
                 break   
         else:
            continue
         for maganhangzo in magas:
            if maganhangzo in szo:
                #print(szo)
                ujrag = valvel[1]
                utolsobetu = szo[-1]
                if utolsobetu != maganhangzo:
                     ujszo=szo+ujrag.replace("v",utolsobetu)
                     print (ujszo+ujrag)
                     break
                if utolsobetu == "e":
                     ujszo=szo.replace(utolsobetu,"é")
                     print(ujszo+ujrag)
                     break
            else:
                   continue
 print("")


elso()
masodik()        
harmadik()
negyedik()