#print("Se ha iniciado el carrito. En total hay 0 manzanas.")
#for i in range(1,6):
#print("Se ha agregado una manzana a la canasta. Ahora hay "+str(i)+" manzanas.")
for i in range (5):
    print(i)
for i in range (1,20,5):  #1-(1+5=6)-(6+5=11)
    print(i)
for i in range(50,20,-5):
    print(i)
n=int(input("Valor a iniciar el rango: "))
m=int(input("Valor a finalizar el rango: "))
l=int(input("Ingrese el tamaño de intervalo: "))
for i in range(n,m,l):
    print(i)

for i in range (0,9):
    if i==4 or i==8:
        print("")
    else:
        print(i)

for i in range(9):
    if i==4 or i==8:
        continue
    print(i)
    
fact=1
for i in range(1,6):
    fact=i*fact
    print(fact)

num=int(input("Ingrese un número: "))
cont=0
for i in range(2,num+1):
    if num%i==0:
        cont=cont+1
if cont>1:
    print("El número no es primo")
else:
    print("El número es primo: "+str(num))
    
producto="" 
cantidad=0
total=0
pago=False
if pago==False:
    print("Pague para verificarle el total")
    pago=True
if pago==True:
    tipo=int(input("¿Cuántos productos diferentes lleva? "))
    for i in range (tipo):
        nombre=input("Escriba el nombre del producto: ")
        precio=int(input("Escriba el valor del producto: "))
        und=int(input("Escriba las unidades: "))
        producto=producto+"\n"+str(und)+" "+nombre+" $ "+str(precio*und)
        cantidad+=und
        total+=(precio*und)
print("Su lista de mercado es: "+producto+"\n"+"La cantidad de producto llevados son: "+str(und)+"\n"+"El total a pagar es: "+str(total))
    
x=int(input(("Escriba un número del 1 al 10: ")))
while x!=(7):
    print("siga intentando, ingrese otro número: ")
    x=int(input("Escriba un número nuevamente: "))
    if(x==7):
        print("Ganaste :D")






