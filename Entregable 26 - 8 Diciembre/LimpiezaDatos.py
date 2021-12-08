# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 12:07:31 2021

@author: Jose Luis
"""

import pandas as pd

datos = pd.read_csv("Datos demográficos.csv")



datos.columns = ["FechaEnc", "Edad", "Genero", "Estado", "EsLic", "AreaEst",
                 "InternetHogar","DispDispone", "DispMas", "TiempoDisp", "Permisos",
                 "OpcionUbi", "Antivirus", "TipoConex", "ConfNombre", "ConfCorreo",
                 "ConfTel","ConfTarjeta", "ConfId", "ConfDir", "ConfFecha", 
                 "Informado", "Confiado", "InfoTerceros", "SaberCookies", 
                 "HacerACookies", "LeerTerm", "AceptarTerm", "RedesSoc", 
                 "TiempoRedes", "TipoRedes","PreocRedes", "DatosNoRedes", "SitRedes", 
                 "HistRedes", "PorcEcom", "FrecEcom", "EsDatoNoEcom", "DatoNoEcom",
                 "SitEcom", "ConfNoFraude", "ConfNoRobo", "ConfBienDatos", "MasPago",
                 "ConfPago", "OpcionNoEcom", "HisEcom"]

#Se crean las columnas que faltan

datos["DispTel"] = [False for i in range (len(datos))]
datos["DispCom"] = [False for i in range (len(datos))]
datos["DispLap"] = [False for i in range (len(datos))]
datos["DispTab"] = [False for i in range (len(datos))]
datos["DispVid"] = [False for i in range (len(datos))]
datos["DispOtr"] = [False for i in range (len(datos))]
datos["DispNin"] = [False for i in range (len(datos))]

datos["PermCam"] = [False for i in range (len(datos))]
datos["PermMic"] = [False for i in range (len(datos))]
datos["PermUbi"] = [False for i in range (len(datos))]
datos["PermGal"] = [False for i in range (len(datos))]
datos["PermCon"] = [False for i in range (len(datos))]
datos["PermNin"] = [False for i in range (len(datos))]

datos["Facebook"] = [False for i in range (len(datos))]
datos["Instagram"] = [False for i in range (len(datos))]
datos["Twitter"] = [False for i in range (len(datos))]
datos["WhatsApp"] = [False for i in range (len(datos))]
datos["TikTok"] = [False for i in range (len(datos))]
datos["Citas"] = [False for i in range (len(datos))]
datos["AppNinguna"] = [False for i in range (len(datos))]

datos["RedNom"] = [False for i in range (len(datos))]
datos["RedCor"] = [False for i in range (len(datos))]
datos["RedNum"] = [False for i in range (len(datos))]
datos["RedEda"] = [False for i in range (len(datos))]
datos["RedDir"] = [False for i in range (len(datos))]
datos["RedNin"] = [False for i in range (len(datos))]

datos["ExtTel"] = [False for i in range (len(datos))]
datos["ExtCor"] = [False for i in range (len(datos))]
datos["RoboCon"] = [False for i in range (len(datos))]
datos["NoAcce"] = [False for i in range (len(datos))]
datos["Acoso"] = [False for i in range (len(datos))]
datos["SitRedNin"] = [False for i in range (len(datos))]

datos["SinCargo"] = [False for i in range (len(datos))]
datos["Fraude"] = [False for i in range (len(datos))]
datos["RoboID"] = [False for i in range (len(datos))]
datos["SitEcomNin"] = [False for i in range (len(datos))]

datos["NoCert"] = [False for i in range (len(datos))]
datos["NoEsc"] = [False for i in range (len(datos))]
datos["MalExp"] = [False for i in range (len(datos))]
datos["MalExpAm"] = [False for i in range (len(datos))]
datos["NoEst"] = [False for i in range (len(datos))]
datos["NoComNin"] = [False for i in range (len(datos))]


datos2 = pd.DataFrame()
for i in (["FechaEnc", "Edad", "Genero", "Estado"]):
    datos2[i] = []
k = len(datos2)
lista = []



for i in range(len(datos)):
    if (datos["Edad"][i] == "30+"):
        datos["Edad"][i] = "30"

    #Editar los estados que tienen acentos
    if datos["Estado"][i] == "Ciudad de México":
        datos["Estado"][i] = "Ciudad de Mexico"
    elif datos["Estado"][i] == "Estado de Mexico":
        datos["Estado"][i] = "Estado de Mexico"
    elif datos["Estado"][i] == "Michoacán":
        datos["Estado"][i] = "Michoacan"
    elif datos["Estado"][i] == "Nuevo León":
        datos["Estado"][i] = "Nuevo Leon"
    elif datos["Estado"][i] == "Querétaro":
        datos["Estado"][i] = "Queretaro"
    elif datos["Estado"][i] == "San Luis Potosí":
        datos["Estado"][i] = "San Luis Potosi"
    elif datos["Estado"][i] == "Yucatán":
        datos["Estado"][i] = "Yucatan"
    
    #Editar la columna por valores booleanos de si son estudiantes de Lic
    if (datos["EsLic"][i] == "No"):
        datos2.loc[k] = [datos[j][i] for j in ["FechaEnc", "Edad", "Genero", "Estado"]]
        lista.append(i)
        k += 1
        
    #Editar la columna del área de estudio por su valor en las tablas
    #Nota: se va revisando en órden del más respondido al menos (al día de hoy)
    #Para disminuir operaciones.
    if (datos["AreaEst"][i] == "Ciencias Sociales y de la comunicación"):
        datos["AreaEst"][i] = 4
    elif (datos["AreaEst"][i] == "Ingenierías"):
        datos["AreaEst"][i] = 3
    elif (datos["AreaEst"][i] == "Humanidades y Artes"):
        datos["AreaEst"][i] = 2
    elif (datos["AreaEst"][i] == "Salud y Medicina"):
        datos["AreaEst"][i] = 5
    elif (datos["AreaEst"][i] == "Ciencias Puras"):
        datos["AreaEst"][i] = 1
    
    if (datos["InternetHogar"][i] == "Sí"):
        datos["InternetHogar"][i] = True
    if (datos["InternetHogar"][i] == "No"):
        datos["InternetHogar"][i] = False
        
    try:
        a = datos["DispDispone"][i].split(";")
        if ("Teléfono inteligente") in a:
            datos["DispTel"][i] = True
        if ("Computadora de escritorio") in a:
            datos["DispCom"][i] = True
        if ("Computadora portátil") in a:
            datos["DispLap"][i] = True
        if ("Tablet") in a:
            datos["DispTab"][i] = True
        if ("Consola de videojuegos") in a:
            datos["DispVid"][i] = True
        if ("Otro") in a:
            datos["DispOtr"][i] = True
        if ("Ninguno") in a:
            datos["DispNin"][i] = True
    except:
        a = []
    
    if (datos["DispMas"][i] == "Teléfono inteligente"):
        datos["DispMas"][i] = 1
    elif (datos["DispMas"][i] == "Computadora de escritorio"):
        datos["DispMas"][i] = 2
    elif (datos["DispMas"][i] == "Computadora portátil"):
        datos["DispMas"][i] = 3
    elif (datos["DispMas"][i] == "Tablet"):
        datos["DispMas"][i] = 4
    elif (datos["DispMas"][i] == "Consola de videojuegos"):
        datos["DispMas"][i] = 5
    elif (datos["DispMas"][i] == "Otro"):
        datos["DispMas"][i] = 6
    elif (datos["DispMas"][i] == "Ninguno"):
        datos["DispMas"][i] = 7
    
    if(datos["TiempoDisp"][i] == "Menos de 1 hora"):
        datos["TiempoDisp"][i] = 0.5
    elif(datos["TiempoDisp"][i] == "1 – 2 horas"):
        datos["TiempoDisp"][i] = 1.5
    elif(datos["TiempoDisp"][i] == "2 – 3 horas"):
        datos["TiempoDisp"][i] = 2.5
    elif(datos["TiempoDisp"][i] == "3 – 5 horas"):
        datos["TiempoDisp"][i] = 4
    elif(datos["TiempoDisp"][i] == "6 – 8 horas"):
        datos["TiempoDisp"][i] = 7
    elif(datos["TiempoDisp"][i] == "Más de 8 horas"):
        datos["TiempoDisp"][i] = 9
    
    try:
        a = datos["Permisos"][i].split(";")
        if ("Cámara") in a:
            datos["PermCam"][i] = True
        if ("Micrófono") in a:
            datos["PermMic"][i] = True
        if ("Ubicación") in a:
            datos["PermUbi"][i] = True
        if ("Galería (Fotos)") in a:
            datos["PermGal"][i] = True
        if ("Contactos") in a:
            datos["PermCon"][i] = True
        if ("Ninguno") in a:
            datos["PermNin"][i] = True
    except:
        a = []
        
    if (datos["Antivirus"][i] == "Sí"):
        datos["Antivirus"][i] = True
    elif (datos["Antivirus"][i] == "No"):
        datos["Antivirus"][i] = False
     
    if (datos["TipoConex"][i] == "Red privada (como datos móviles, o Wi-Fi en tu casa)"):
        datos["TipoConex"][i] = "Privada"
    elif (datos["TipoConex"][i] == "Red en tu trabajo o universidad"):
        datos["TipoConex"][i] = "Trabajo"
    elif (datos["TipoConex"][i] == "Red en espacios públicos (como conexión WiFi del gobierno)"):
        datos["TipoConex"][i] = "Publica"
    elif (datos["TipoConex"][i] == "No sé"):
        datos["TipoConex"][i] = "No se"
        
    for j in ["ConfNombre", "ConfCorreo","ConfTel","ConfTarjeta", "ConfId", 
              "ConfDir", "ConfFecha"]:
        if datos[j][i] == "Muy seguro":
            datos[j][i] = 4
        elif datos[j][i] == "Seguro":
            datos[j][i] = 3
        elif datos[j][i] == "Poco seguro":
            datos[j][i] = 2
        elif datos[j][i] == "Nada seguro":
            datos[j][i] = 1
    
    if (datos["SaberCookies"][i] == "Sí"):
        datos["SaberCookies"][i] = True
    elif (datos["SaberCookies"][i] == "No"):
        datos["SaberCookies"][i] = False
        
    for j in ["LeerTerm", "AceptarTerm"]:
        if datos[j][i] == "Siempre":
            datos[j][i] = 4
        if datos[j][i] == "Casi siempre":
            datos[j][i] = 2
        if datos[j][i] == "Casi nunca":
            datos[j][i] = 3
        if datos[j][i] == "Nunca":
            datos[j][i] = 1
    
    try:
        a = datos["RedesSoc"][i].split(";")
        if ("Facebook") in a:
            datos["Facebook"][i] = True
        if ("Instagram") in a:
            datos["Instagram"][i] = True
        if ("Twitter") in a:
            datos["Twitter"][i] = True
        if ("WhatsApp") in a:
            datos["WhatsApp"][i] = True
        if ("TikTok") in a:
            datos["TikTok"][i] = True
        if ("Aplicaciones de citas") in a:
            datos["Citas"][i] = True
        if ("Ninguna") in a:
            datos["AppNinguna"][i] = True
    except:
        a = []
        
    if(datos["TiempoRedes"][i] == "Menos de 1 hora"):
        datos["TiempoRedes"][i] = 0.5
    elif(datos["TiempoRedes"][i] == "1 – 2 horas"):
        datos["TiempoRedes"][i] = 1.5
    elif(datos["TiempoRedes"][i] == "2 – 3 horas"):
        datos["TiempoRedes"][i] = 2.5
    elif(datos["TiempoRedes"][i] == "3 – 5 horas"):
        datos["TiempoRedes"][i] = 4
    elif(datos["TiempoRedes"][i] == "6 – 8 horas"):
        datos["TiempoRedes"][i] = 7
    elif(datos["TiempoRedes"][i] == "Más de 8 horas"):
        datos["TiempoRedes"][i] = 9
        
    if (datos["TipoRedes"][i]=="Públicas"):
        datos["TipoRedes"][i] = "Publicas"
        
    try:
        a = datos["DatosNoRedes"][i].split(";")
        if ("Nombre") in a:
            datos["RedNom"][i] = True
        if ("Correo") in a:
            datos["RedCor"][i] = True
        if ("Número de teléfono") in a:
            datos["RedNum"][i] = True
        if ("Edad") in a:
            datos["RedEda"][i] = True
        if ("Dirección") in a:
            datos["RedDir"][i] = True
        if ("Ninguno") in a:
            datos["RedNin"][i] = True

    except:
        a = []
        
    try:
        a = datos["SitRedes"][i].split(";")
        if ("Extorsión por teléfono") in a:
            datos["ExtTel"][i] = True
        if ("Extorsión por mensaje (correo)") in a:
            datos["ExtCor"][i] = True
        if ("Robo de contraseñas") in a:
            datos["RoboCon"][i] = True
        if ("Accesos no autorizados a tus redes sociales") in a:
            datos["NoAcce"][i] = True
        if ("Acoso o bullying en tus redes sociales") in a:
            datos["Acoso"][i] = True
        if ("Ninguno") in a:
            datos["RedNin"][i] = True

    except:
        a = []
        
    if(datos["PorcEcom"][i] == "0%"):
        datos["PorcEcom"][i] = 0
    elif(datos["PorcEcom"][i] == "1% a 20%"):
        datos["PorcEcom"][i] = .105
    elif(datos["PorcEcom"][i] == "21% a 40%"):
        datos["PorcEcom"][i] = .305
    elif(datos["PorcEcom"][i] == "41% a 60%"):
        datos["PorcEcom"][i] = .505
    elif(datos["PorcEcom"][i] == "61% a 80%"):
        datos["PorcEcom"][i] = .705
    elif(datos["PorcEcom"][i] == "81% a 99%"):
        datos["PorcEcom"][i] = .90
    elif(datos["PorcEcom"][i] == "100%"):
        datos["PorcEcom"][i] = 1
    
    if (datos["FrecEcom"][i]=="Una vez al año"):
        datos["FrecEcom"][i] = "Una vez al anio"
        
    if (datos["DatoNoEcom"][i] == "Nombre"):
        datos["DatoNoEcom"][i] = 1
    elif (datos["DatoNoEcom"][i] == "Correo"):
        datos["DatoNoEcom"][i] = 2
    elif (datos["DatoNoEcom"][i] == "Número de teléfono"):
        datos["DatoNoEcom"][i] = 3
    elif (datos["DatoNoEcom"][i] == "Tarjeta de crédito"):
        datos["DatoNoEcom"][i] = 6
    elif (datos["DatoNoEcom"][i] == "Fotografía de una identificación"):
        datos["DatoNoEcom"][i] = 7
    elif (datos["DatoNoEcom"][i] == "Dirección"):
        datos["DatoNoEcom"][i] = 5
    elif (datos["DatoNoEcom"][i] == "Fecha de nacimiento"):
        datos["DatoNoEcom"][i] = 8
    elif (datos["DatoNoEcom"][i] == "Otro"):
        datos["DatoNoEcom"][i] = 10
    elif (datos["EsLic"][i]):
        datos["DatoNoEcom"][i] = 9
    
    try:
        a = datos["SitEcom"][i].split(";")
        if ("Cargos sin autorizar") in a:
            datos["SinCargo"][i] = True
        if ("Fraude en alguna compra") in a:
            datos["Fraude"][i] = True
        if ("Robo de indentidad") in a:
            datos["RoboID"][i] = True
        if ("Ninguno") in a:
            datos["SitEcomNin"][i] = True

    except:
        a = []
        
    for j in ["ConfNoFraude", "ConfNoRobo", "ConfBienDatos"]:
        if (datos[j][i] == "Completamente seguro"):
            datos[j][i] = 4
        if (datos[j][i] == "Seguro"):
            datos[j][i] = 3
        if (datos[j][i] == "Poco seguro"):
            datos[j][i] = 2
        if (datos[j][i] == "Nada seguro"):
            datos[j][i] = 1
            
    for j in ["MasPago","ConfPago"]:
        if (datos[j][i] == "Tarjeta de crédito/débito"):
            datos[j][i] = 1
        if (datos[j][i] == "Transferencia bancaria"):
            datos[j][i] = 2
        if (datos[j][i] == "Paypal/Apple Pay"):
            datos[j][i] = 3
        if (datos[j][i] == "Tarjeta digital"):
            datos[j][i] = 4
        if (datos[j][i] == "Efectivo en puntos de pago (Oxxo, 7eleven, ...)"):
            datos[j][i] = 5
        if (datos[j][i] == "Otro"):
            datos[j][i] = 6
    
    try:
        a = datos["OpcionNoEcom"][i].split(";")
        if ("Que la página web no esté certificada digitalmente, es decir, que no tenga el candado en la barra de direcciones (imagen mostrada en la parte superior)") in a:
            datos["NoCert"][i] = True
        if ("No haber escuchado de la página web") in a:
            datos["NoEsc"][i] = True
        if ("Haber tenido una mala experiencia con esa plataforma") in a:
            datos["MalExp"][i] = True
        if ("Haber escuchado una mala experiencia de un amigo") in a:
            datos["MalExpAm"][i] = True
        if ("Que la página web no tenga estructura estética") in a:
            datos["NoEst"][i] = True
        if ("Ninguno") in a:
            datos["NoComNin"][i] = True

    except:
        a = []
  
datos = datos.drop(['DispDispone'], axis=1) 
datos = datos.drop(['Permisos'], axis=1) 
datos = datos.drop(['RedesSoc'], axis=1) 
datos = datos.drop(['DatosNoRedes'], axis=1) 
datos = datos.drop(['SitRedes'], axis=1) 
datos = datos.drop(['SitEcom'], axis=1) 
datos = datos.drop(['OpcionNoEcom'], axis=1)  
datos = datos.drop(['EsDatoNoEcom'], axis=1) 
datos = datos.drop(['EsLic'], axis=1)  

datos = datos.drop(lista, axis = 0)   

#%%        
datos.to_csv("Datos_limpios_lic.csv", sep = ",", encoding = "utf-8", index = False)
datos2.to_csv("Datos_limpios_no_lic.csv", sep = ",", encoding = "utf-8", index = False)    
