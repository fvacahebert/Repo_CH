import sys

if len(sys.argv)==3:
    nota1=float(sys.argv[1])
    nota2=float(sys.argv[2])

    if nota1>=7 and nota2>=7:
        print("Promocionado")
    elif nota1>=4 and nota2>=4:
        print("Aprobado, debe rendir final")
    elif nota1<4 and nota2<4:
        print("Desaprobado, debe recursar")    
    elif nota1<4:
        print("Debe recuperar primera parcial")
    elif nota2<4:
        print("Debe recuperar el segundo parcial")
    

else:
    print("Debe ingresar dos notas")
