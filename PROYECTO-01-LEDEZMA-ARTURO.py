#LIBRERIAS DEL PROYECTO
import getpass
import pandas as pd


#IMPORTAR LISTAS
from lifestore_file import lifestore_products,lifestore_sales,lifestore_searches

#asignando titulos de encabezado de columna

dflifestore_products = pd.DataFrame(lifestore_products, columns=['id_producto', 'Descripcion', 'precio', 'categoria', 'stock'])
dflifestore_sales = pd.DataFrame(lifestore_sales, columns=['id_venta', 'id_producto', 'score', 'fecha', 'devolucion'])
dflifestore_searches = pd.DataFrame(lifestore_searches, columns=['id_busqueda', 'id_producto'])

##unir dataframes
                  
df_product_sales = pd.merge(dflifestore_sales, dflifestore_products, on='id_producto', how='left')
         
#crear dataframe con el conteo de productos en venta
df2_product_sales=df_product_sales.groupby(['Descripcion'])[['id_producto']].count()

#ordenar de forma descendente las ventas
df2_product_sales.sort_values('id_producto', ascending=False,inplace=True)
        
#cambiando el encabezado de la columna
df2_product_sales.rename(columns={ 'id_producto': 'Frecuencia'}, inplace=True)

#pasamos el top a un listado limitado a 50 productos con mas venta
top_50 = df2_product_sales[:50]

## Por categoría, generar un listado con los 50 productos con menores ventas
df3_product_sales=df_product_sales.groupby(['Descripcion','categoria'])[['id_producto']].count()

#ordenar de forma descendente las ventas
df3_product_sales.sort_values('id_producto', ascending=True,inplace=True)
#cambiando el encabezado de la columna
df3_product_sales.rename(columns={ 'id_producto': 'Frecuencia'}, inplace=True)

#pasamos el bottom categorias a un listado limitado a 50 registros
bottom_50_cat_item = df3_product_sales[:50]

##para el listado con los 100 productos con mayor búsquedas.
##unir dataframes
df_product_searches = pd.merge(dflifestore_searches, dflifestore_products, on='id_producto', how='left')

#crear dataframe con el conteo de productos en venta
df2_product_searches=df_product_searches.groupby(['Descripcion'])[['id_producto']].count()

#ordenar de forma descendente las ventas
df2_product_searches.sort_values('id_producto', ascending=False,inplace=True)
#cambiando el encabezado de la columna
df2_product_searches.rename(columns={ 'id_producto': 'Frecuencia'}, inplace=True)
#pasamos el top de los mas buscados a un listado limitado a 100
top_100busquedas = df2_product_searches[:100]


##para el listado con los 100 productos con menores búsquedas.
df3_product_searches=df_product_searches.groupby(['Descripcion'])[['id_producto']].count()

#ordenar de forma descendente las ventas
df3_product_searches.sort_values('id_producto', ascending=True,inplace=True)
#cambiando el encabezado de la columna
df3_product_searches.rename(columns={ 'id_producto': 'Frecuencia'}, inplace=True)

bottom_100busquedas = df3_product_searches[:100]

#Listado 20 productos con mejores reseñas.
#agrupamos los score por descripción e id
bestscore_product_sales=df_product_sales.groupby(['Descripcion','score'])[['id_producto']].count()

#ordenamos
bestscore_product_sales.sort_values(['score','id_producto'], ascending=[False,False],inplace=True)

#cambiando el encabezado de la columna
bestscore_product_sales.rename(columns={'Descripcion': 'Descripcion','score': 'score', 'id_producto': 'Frecuencia'}, inplace=True)

#pasando el data frame  a otro limitandolo solo a 20 registros
top_score = bestscore_product_sales[:20]

#Listado 20 productos con peores reseñas.
#agrupamos los score por descripción e id
worstscore_product_sales=df_product_sales.groupby(['Descripcion','score'])[['id_producto']].count()

#ordenamos
worstscore_product_sales.sort_values(['score','id_producto'], ascending=[True,False],inplace=True)

#cambiando el encabezado de la columna
worstscore_product_sales.rename(columns={'Descripcion': 'Descripcion','score': 'score', 'id_producto': 'Frecuencia'}, inplace=True)

#pasando el data frame  a otro limitandolo solo a 20 registros
bottom_score = worstscore_product_sales[:20]


# Script login
print("Iniciar Sesión")

#Utilizamos libreria getpass para ocultar el pass


#Configuramos usuario y pass
Usr_Name = "Arturo"
Usr_Password = "1234" 

#creamos variable login que desencadenara el while
login = 'true'
while (login == 'true'):

#solicitamos el nombre de usuario
    username = input("Usuario: ")
    #sí el usuario es correcto continuamos, de lo contrario mandamos mensaje de usuario incorrecto e intentar nuevamente
    if (username == Usr_Name):
        login1 = 'true'
        #solicitamos el password y comparamos con el permitido siempre y cuando el usuario sea correcto
        while (login1 == 'true'):
            password = getpass.getpass("Password: ")
            if (password == Usr_Password):
                print("Bienvenido " + username)
                login = 'false'
                login1 = 'false'
                acceso="autorizado"
                # en caso de que sean correctas las credenciales enviamos confirmación de autorizado y la variable login permanecera en false para detener el while
            else:
              #en caso de que las credenciales sean incorrectas enviamos mensaje de error y de volver a intentar
                print("Password incorrecto!, intente de nuevo")
    else:
        print("Usuario incorrecto!, intente de nuevo")

#la variable acceso determina el mensaje de bienvenida y continuidad al menú
if(login=="false"):
   print(""" 
          """)
   print("""             Comencemos con el caso      """)
   print(""" 
          """)
   opcion=input("Desear ir a sección de reportes (s/n):  ")
   print(""" 
          """)
   #mientras se cumplan las condiciones de que sea un usuario autorizado quien selecciona ver el menu  el bucle while se mostrara       
   while opcion=="s" and login=='false':
      print("Selecciona el número del reporte que deseas: ")
      print(""" 
          """)
      print("Top 50 Ventas Productos    [1]")
      print("Bottom 50 Ventas productos [2]")
      print("Los 100 MAS buscados       [3]")
      print("Los 100 MENOS buscados     [4]")
      print("Las mejores reseñas =)     [5]")
      print("Las peores reseñas  =(     [6]")
      print("Ingresos al mes y Promedio [7]")
      print("Ingreso Anual y mejor mes  [8]")
      print("Salir                      [9]")

      print(""" 
          """)
          #dependiendo de la opción seleccionada se mostrara o ejecutara el reporte
      seleccion=input("ingresa una opción: ")
      print(""" 
          """)

      if seleccion=="1":
          print(""" 
          """)
          print("Top 50 Ventas Productos    [1]")
         #muestra el reporte configurado fuera del bucle while
          print(top_50)
          
          print(""" 
          """)
          opcion=input("Ir a sección de reportes (s/n):  ")
          print(""" 
          """)
      elif seleccion=="2":
          print(""" 
          """)
          print("Bottom 50 Ventas productos [2]")
          #muestra el reporte configurado fuera del bucle while
          print(bottom_50_cat_item)
          print(""" 
          """)
          opcion=input("Ir a sección de reportes (s/n):  ")
          print(""" 
          """)
       

      elif seleccion=="3":
          print(""" 
          """)
          print("Los 100 MAS buscados       [3]")
          #muestra el reporte configurado fuera del bucle while
          print(top_100busquedas)
          print(""" 
          """)
          opcion=input("Ir a sección de reportes (s/n):  ")
          print(""" 
          """)
 

      elif seleccion=="4":
          print(""" 
          """)
          print("Los 100 MENOS buscados     [4]")
          #muestra el reporte configurado fuera del bucle while
          print(bottom_100busquedas)
          print(""" 
          """)
          opcion=input("Ir a sección de reportes (s/n):  ")
          print(""" 
          """)


      elif seleccion=="5":
          print(""" 
          """)
          print("Las mejores reseñas =)     [5]")
          #muestra el reporte configurado fuera del bucle while
          print(top_score) 
          print(""" 
          """)
          opcion=input("Ir a sección de reportes (s/n):  ")
          print(""" 
          """)


      elif seleccion=="6":
          print(""" 
          """)
          print("Las peores reseñas  =(     [6]")
          #muestra el reporte configurado fuera del bucle while
          print(bottom_score) 
          print(""" 
          """)
          opcion=input("Ir a sección de reportes (s/n):  ")
          print(""" 
          """)


      elif seleccion=="7":
        #para el reporte quise hacerlo utilizando las listas originales y con la libreria datetima y time para descomponer la fecha en mes y año
        import datetime
        import time
        #creo una lista vacia que me servida para almacenar los datos con las fechas descompuestas
        ls_sales=[]
        for venta in lifestore_sales:  
          for producto in lifestore_products:
            if venta[1]==producto[0]:
              fecha=venta[3]
              #doy formato a la fecha
              fecha2=datetime.datetime.strptime(fecha,'%d/%m/%Y')
              #separo mes y año y creo una columna donde solo me agrupe mes y año
              mes=fecha2.month
              year=fecha2.year
              mes_year= fecha2.strftime('%Y.%m')
              #el siguiente if me servirá para determinar si existe una devolución asignar como negativo el ingreso
              if venta[4]==1:
                precio=producto[2]*-1
              else:
                precio=producto[2]
            #agrego todos los registros a la lista 
            ls_sales.append([venta[0],venta[1],venta[2],fecha,mes,year,mes_year,year,venta[4],precio])
        #print(ls_sales)   

        #ventas columnas:id_venta, id_producto,score,fecha,mes, año, devolucion, precio
        #Crearemos una lista de los periodos con registro unico año.mes
        lista_mes=[]
        lista_year=[]
        for periodo in ls_sales:
          lista_mes.append(periodo[6])
          lista_year.append(periodo[7])
        #las siguientes instrucciones me crean registros unicos de mes y años para recorrerlas y sumar ingresos
        meses_unique=set(lista_mes)
        year_unique=set(lista_year)
        meses=sorted(meses_unique)
        years=sorted(year_unique)


        # Generamos la suma de ingresos por mes_año y el conteo de ventas utilizando un recorrdido de las listas con resgistros unicos creada antes
        contador=0
        ingreso=0
        ingreso_mensual=[]
        for n in meses:  
          for fechas in ls_sales:
            if fechas[6]==n:
              contador+=1
              ingreso+=fechas[9]
              avg=int(ingreso/contador)

          ingreso_mensual.append(['periodo:',n,'Total ingreso: ',ingreso,'Promedio: ',avg])
          contador=0
          ingreso=0
        print("Ingresos al mes y Promedio [7]")
        print("El ingreso total y el ingreso promedio por mes es el siguiente: ")
        print("")
        for n in ingreso_mensual:
          print(n)   
        print("""
                   """)
        #Para obtener el mes con mejores ingresos utilizamos excluimos los valores de 2002 y 2019
        exclusion=['2002.05','2019.11']
        year2020=[]
        mes_max=[]
        for n in ingreso_mensual:
          if n[0] not in exclusion:
            year2020.append(n)
        year_ordenado = sorted(year2020, key=lambda x: x[3], reverse=True)
        #for n in year_ordenado:
         # print(n)

        print("el mes con mayores ingresos en 2020 fue: ",year_ordenado[0][1], "con un ingreso de: ",year_ordenado[0][3]) 

        print(""" 
          """)
          
        opcion=input("Ir a sección de reportes (s/n):  ")
        print(""" 
          """)
          
     
      elif seleccion=="8":
       
        ls_sales=[]
        for venta in lifestore_sales:  
          for producto in lifestore_products:
            if venta[1]==producto[0]:
              fecha=venta[3]
              fecha2=datetime.datetime.strptime(fecha,'%d/%m/%Y')
              mes=fecha2.month
              year=fecha2.year
              mes_year= fecha2.strftime('%Y.%m')
              if venta[4]==1:
                precio=producto[2]*-1
              else:
                precio=producto[2]
            ls_sales.append([venta[0],venta[1],venta[2],fecha,mes,year,mes_year,year,venta[4],precio])
        #print(ls_sales)   

        #ventas columnas:id_venta, id_producto,score,fecha,mes, año, devolucion, precio
        #Crearemos una lista de los periodos con registro unico año.mes
        lista_mes=[]
        lista_year=[]
        for periodo in ls_sales:
          lista_mes.append(periodo[6])
          lista_year.append(periodo[7])
        #print(lista_mes)
        meses_unique=set(lista_mes)
        year_unique=set(lista_year)
        meses=sorted(meses_unique)
        years=sorted(year_unique)
        
        #creamos la suma de ingresos por año y conteo
        contador2=0
        ingreso2=0
        ingreso_anual=[]
        for n in years:
          for fechas in ls_sales:
            if fechas[7]==n:
              contador2+=1
              ingreso2+=fechas[9]
              avg2=int(ingreso2/contador2)
          ingreso_anual.append(['Año:',n,'Ingreso Total: ',ingreso2,'Ingreso Promedio:',avg2])
          contador2=0
          ingreso2=0
        
        
        print("Ingreso Anual y mejor mes  [8]")
        print("El ingreso total y el ingreso promedio por año es el siguiente: ")
        print("")
        for yyy in ingreso_anual:
          print(yyy) 
      
        print(""" 
          """)
        opcion=input("Ir a sección de reportes (s/n):  ")
        print(""" 
          """)

      elif seleccion=="9":
          print(""" 
          """)
          opcion="n" 
          login='true'
          print("""
                   Fin del programa
                                    """)

# finaliza el programa y devuelve el valor a login en true para solicitar contraseña nuevamente
print("""
Fin del programa
""")
login=="true"
