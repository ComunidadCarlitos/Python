"""nombres=['David','Paula','Erik']
nombres.append('Laura')
print(nombres)

for i in range (2):
    nombre=input("Ingrese el nombre: ")
    nombres.append(nombre)
print(nombres)

#Apellidos
apellidos=['Esquea', 'Ortiz','Osorio','Lopez','nuñez','Ardila']
nombres.extend(apellidos)
print(nombres)
nombres=['David','Paula','Erik']
nombres.insert(1,'Dimo')
nombres.pop(0)
print(nombres)
nombres.pop()
nombres.remove('Dimo')
print(nombres)
datos=list(range(2,20,2))
print(datos)
print(len(datos))
#[1][0],para acceder una lista dentro de otra... 

n=int(input("Escriba el número de materias: "))
listamaterias=[]
for i in range (n):
    materia=input("Ingrese el nombre de la materia: ")
    nota=float(input("Escriba la nota final correspondiente a la asignatura anterior: "))
    if nota<3.0:
        listamaterias.append(materia)
print("Las materias que debe repetir son: ",listamaterias)

def Asignaturas():
    Asig=["Matematicas","Fisica","Quimica","Historia","Lengua"]
    i=0
    x=len(Asig)
    while i <=(x-1):
        print(i)#Llevar cuenta de i
        print(x)#Llevar cuenta de long lista
        nota=float(input("Ingrese la nota de la asignatura :"+Asig[i]))
        if nota>=3:
            Asig.pop(i)
            x=len(Asig)
            i-=1
        i+=1
    print ("Debes reptir",Asig)
##para dar orden al codigo
def run():
     Asignaturas()
 
##el main principal
if __name__ == "__main__":
    run()
    
    Aminus=palabra.count('a')
    Amayus=palabra.count('A')
    Atotal=Aminus+Amayus
    Eminus=palabra.count('e')
    Emayus=palabra.count('E')
    Etotal=Eminus+Emayus
    Iminus=palabra.count('i')
    Imayus=palabra.count('I')
    Itotal=Iminus+Imayus
    Ominus=palabra.count('o')
    Omayus=palabra.count('O')

abc=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
a=0
for i in range(len(abc)):
    a+=1
    if a>=3 and a%3==0 and a<len(abc)-1:
        abc.remove(abc[a-1])
        print(abc,"La posición eliminada es: ",(a-1))
    
palabra=input("Escriba una palabra: ")
x=1
while x!=0:
    Aminus=palabra.count('a')
    Amayus=palabra.count('A')
    Atotal=Aminus+Amayus
    Eminus=palabra.count('e')
    Emayus=palabra.count('E')
    Etotal=Eminus+Emayus
    Iminus=palabra.count('i')
    Imayus=palabra.count('I')
    Itotal=Iminus+Imayus
    Ominus=palabra.count('o')
    Omayus=palabra.count('O')
    Ototal=Ominus+Omayus
    Uminus=palabra.count('u')
    Umayus=palabra.count('U')
    Utotal=Uminus+Umayus
    x=0
vocales=[Atotal,Etotal,Itotal,Ototal,Utotal]
print("El número de veces que se repite cada vocal en orden A, E, I, O, U es: ",vocales,"\n","La palabra es: ",palabra)"""

"""num=["uno","tres"]
num.extend("Cuatro")
print(num)"""

#with open (Ruta del escritorio, 'r') as f:
#f.readlines()
#f.write('Hola mundo soy Paula')

"""def dicCuadrado(n):
    cuadro={}
    n=int(n)
    for i in range (n+1):
        cuadro[i]=i*i
    return cuadro
print(dicCuadrado(10))"""

meses=['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']
def calculadoraMes(registroDeAhorros,nombre):
    calculo={}
    x=registroDeAhorros.split(';')
    for j in x:
        y=j.split(',')
        total=0
        for k in y:
            if k in meses:
                mes=k
            else:
                total+=int(k)
            calculo[mes]=total
        nomb=y[-1]
    lista=(nombre,calculo)
    return(lista)
print(calculadoraMes("Enero,15000,18500,19350;Junio,40000,35000;Julio,43000,32000,46000;Agosto,47000,31000,28000,15000","Daniel"))

