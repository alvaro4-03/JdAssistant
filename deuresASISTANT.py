#TODO Futur mirar de sincronitzar amb calendari Moodle

#TODO Per què quatre setmanes?
stm0=[[[],[],[],[],[],[]],[[],[],[],[],[],[]],[[],[],[],[],[],[]],[[],[],[],[],[],[]],[[],[],[],[],[],[]]]
stm1=[[[],[],[],[],[],[]],[[],[],[],[],[],[]],[[],[],[],[],[],[]],[[],[],[],[],[],[]],[[],[],[],[],[],[]]]
stm2=[[[],[],[],[],[],[]],[[],[],[],[],[],[]],[[],[],[],[],[],[]],[[],[],[],[],[],[]],[[],[],[],[],[],[]]]
stm3=[[[],[],[],[],[],[]],[[],[],[],[],[],[]],[[],[],[],[],[],[]],[[],[],[],[],[],[]],[[],[],[],[],[],[]]]
mes=[stm0,stm1,stm2,stm3]
dies=["DILLUNS","DIMARTS","DIMECRES","DIJOUS","DIVENDRES"]
hores=["8-9","9-10","10-11","11:30-12:30","12:30-13:30","13:30-14:30"]
s=[[]]
#botó per consultar o per apuntar

#TODO Més que deures és per apuntar dates de lliurament, no?
for m in s:
    # TODO Per què bucle? No si no escriu APUNTAR es fa bucle n cops i no s'entèn.
    op=input("Escriu 'apuntar' per poder apuntar deures nous   ").upper()
    if op == "APUNTAR":
        #per apuntar deures, les llistes de dalt representen el calendari d'un mes.
        dque=input("De quina matèria? ").upper()
        que=input("Quins deures tens? ").upper()
        dia=input("Per a quin dia són? ").upper()
        hora=input("A quina hora? ")
        stm=input("Quina setmana del mes? ")
        x=dies.index(dia)
        y=hores.index(hora)
        n=int(stm)-1
        mes[n][x][y].append(dque + ", " + que)
        print("S'ha apuntat correctament: "+str(mes[n][x][y]).lower()+"per al "+dia.lower())
        s.append([])
        
        
#TODO Posar cada espai en funcions. Diferents.

#consultar deures del mes per dia
a= input("clica la tecla a per fer una consulta a través del dia ").upper()
if a == "A":
    c=input("De quin dia vols saber els deures? ").upper()
    d=input("De quina setmana del mes? ").upper()
    e=dies.index(c)
    f=int(d)-1
    for h in hores:
        b=hores.index(h)
        print("De "+h+"; "+str(mes[e][f][b]).lower())
        
        
        
#consultar deures del mes per materia
             
b=input("clica la tecla b per fer una consulta a través de la materia ").upper()
if b == "B":
    materia=input().upper()
    for d in stm0:
        if materia in mes or materia in stm0 or materia in stm1 or materia in stm2 or materia in stm3:# Excel·lent
            print(str(mes[materia in mes or materia in stm0 or materia in stm1 or materia in stm2 or materia in stm3][1:5][materia.index]))

#TODO Consultar deures per setmana actual
#TODO Consultar deures per dia actual 