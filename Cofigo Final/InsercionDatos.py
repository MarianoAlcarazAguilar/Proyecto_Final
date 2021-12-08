# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 16:55:36 2021

@author: Jose Luis
"""
import psycopg2
import pandas as pd

datos = pd.read_csv("Datos_limpios_lic.csv")

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="admin",
    port = "5432")

cur = conn.cursor()

for i in range(len(datos)):
    
    usuarios = "INSERT INTO encuesta.usuarios (genero, edad, estado_republica, "
    usuarios += "area_estudio_id) values ('"+str(datos["Genero"][i])+"', "
    usuarios += str(datos["Edad"][i])+",'"+str(datos["Estado"][i])+"', "
    usuarios += str(datos["AreaEst"][i])+")"
   
    cur.execute (usuarios)
    
conn.commit()

for i in range(len(datos)):
    
    usuario_dispositivos = "INSERT INTO encuesta.usuario_dispositivos (usuario_id,"
    usuario_dispositivos += " telefono, desktop, laptop, tablet, consola, other, ninguno) " 
    usuario_dispositivos += "values ("+str(i+1)+", "+str(datos["DispTel"][i])+","
    usuario_dispositivos += str(datos["DispCom"][i])+","+str(datos["DispLap"][i])+","
    usuario_dispositivos += str(datos["DispTab"][i])+","+str(datos["DispVid"][i])+","
    usuario_dispositivos += str(datos["DispOtr"][i])+","+str(datos["DispNin"][i])+")"
    
    cur.execute (usuario_dispositivos)
    
conn.commit()

for i in range(len(datos)):
    
    perfil_usuario = "INSERT INTO encuesta.perfil_usuario (usuario_id, internet_casa, "
    perfil_usuario += "tiempo_diario, tipo_conexion, antivirus, dispositivo_fav, ubicacion)"
    perfil_usuario += " values ("+str(i+1)+", "+str(datos["InternetHogar"][i])
    perfil_usuario += ", "+str(datos["TiempoDisp"][i])+", '"+str(datos["TipoConex"][i])
    perfil_usuario += "', "+str(datos["Antivirus"][i])+", "+str(datos["DispMas"][i])
    perfil_usuario += ", '"+str(datos["OpcionUbi"][i])+"')"
    
    cur.execute(perfil_usuario)
    
conn.commit()
    
for i in range(len(datos)):
    
    perfil_permisos = "INSERT INTO encuesta.perfil_permisos (perfil_usuario_id, camara, microfono, "
    perfil_permisos += "ubicacion, galeria, contactos, ninguno) values ("+str(i+1)
    perfil_permisos += ", "+str(datos["PermCam"][i])+", "+str(datos["PermMic"][i])+", "
    perfil_permisos += str(datos["PermUbi"][i])+", "+str(datos["PermGal"][i])+", "
    perfil_permisos += str(datos["PermCon"][i])+", "+str(datos["PermNin"][i])+")"
    
    cur.execute(perfil_permisos)
    
conn.commit()

for i in range(len(datos)):
    
    social_media = "INSERT INTO encuesta.social_media (usuario_id, tipo_redes, "
    social_media += "uso_historial, tiempo_redes) values ("+str(i+1)+", '"
    social_media += str(datos["TipoRedes"][i])+"', '"+str(datos["HistRedes"][i])
    social_media += "', '"+str(datos["TiempoRedes"][i])+"')"
    
    cur.execute(social_media)
    
conn.commit()

for i in range(len(datos)):
    
    redes = "INSERT INTO encuesta.redes (social_media_id, facebook, instagram, "
    redes += "twitter, whatsapp, tiktok, dating, ninguna) values ("+str(i+1)
    redes += ", "+str(datos["Facebook"][i])+", "+str(datos["Instagram"][i])
    redes += ", "+str(datos["Twitter"][i])+", "+str(datos["WhatsApp"][i])
    redes += ", "+str(datos["TikTok"][i])+", "+str(datos["Citas"][i])
    redes += ", "+str(datos["AppNinguna"][i])+")"
    
    cur.execute (redes)
    
conn.commit()

for i in range(len(datos)):
    
    respuestas_social_media = "INSERT INTO encuesta.respuestas_social_media ("
    respuestas_social_media += "social_media_id, escalares_social_media_id, respuesta)"
    respuestas_social_media += " values ("+str(i+1)+", "+str(1)+", "+str(datos["PreocRedes"][i])+")"
    
    cur.execute (respuestas_social_media)
    
conn.commit()

for i in range(len(datos)): 
    
    situaciones_sm = "INSERT INTO encuesta.situaciones_sm (social_media_id, extorsion_telefono, "
    situaciones_sm += "extorsion_mensaje, robo_contrasena, unauthorized_access, bullying, ninguno)"
    situaciones_sm += " values ("+str(i+1)+", "+str(datos["ExtTel"][i])+", "+str(datos["ExtCor"][i])
    situaciones_sm += ", "+str(datos["RoboCon"][i])+", "+str(datos["NoAcce"][i])+", "
    situaciones_sm += str(datos["Acoso"][i])+", "+str(datos["SitRedNin"][i])+")"
    
    cur.execute (situaciones_sm)
    
conn.commit()

for i in range(len(datos)):
    
    datos_no_ingresado = "INSERT INTO encuesta.datos_no_ingresado (social_media_id, nombre, "
    datos_no_ingresado += "correo, telefono, edad, direccion, ninguno) values ("
    datos_no_ingresado += str(i+1)+", "+str(datos["RedNom"][i])+", "
    datos_no_ingresado += str(datos["RedCor"][i])+", "+str(datos["RedNum"][i])
    datos_no_ingresado += ", "+str(datos["RedEda"][i])+", "+str(datos["RedDir"][i])
    datos_no_ingresado += ", "+str(datos["RedNin"][i])+")"
    
    cur.execute (datos_no_ingresado)
    
conn.commit()

for i in range(len(datos)):
    
    web = "INSERT INTO encuesta.web (usuario_id, saber_cookies, accion_cookies) "
    web += "values ( " + str(i+1) + ", " + str(datos["SaberCookies"][i])
    web += ", '" + str(datos["HacerACookies"][i]) + "')"
    
    cur.execute (web)

conn.commit()

for i in range(len(datos)):
    
    e_commerce = "INSERT INTO encuesta.e_commerce (usuario_id, porcentaje_compras, "
    e_commerce += "frecuencia, dato_evitar_compra, pago_favorito, pago_confiable, uso_historial) "
    e_commerce += "values (" + str(i+1) + ", " + str(datos["PorcEcom"][i])
    e_commerce += ", '" + str(datos["FrecEcom"][i]) + "', " + str(datos["DatoNoEcom"][i])
    e_commerce += ", " + str(datos["MasPago"][i]) + ", " + str(datos["ConfPago"][i])
    e_commerce += ", '" + str(datos["HisEcom"][i]) + "')"
    
    cur.execute (e_commerce)

conn.commit()

for i in range(len(datos)):
    
    respuestas_web = "INSERT INTO encuesta.respuestas_web (web_id, "
    respuestas_web += "escalares_web_id, respuesta) values "
    respuestas_web += "("+str(i+1)+", "+str(1)+", "+str(datos["ConfNombre"][i])+"), "
    respuestas_web += "("+str(i+1)+", "+str(2)+", "+str(datos["ConfCorreo"][i])+"), "
    respuestas_web += "("+str(i+1)+", "+str(3)+", "+str(datos["ConfTel"][i])+"), "
    respuestas_web += "("+str(i+1)+", "+str(4)+", "+str(datos["ConfTarjeta"][i])+"), "
    respuestas_web += "("+str(i+1)+", "+str(5)+", "+str(datos["ConfId"][i])+"), "
    respuestas_web += "("+str(i+1)+", "+str(6)+", "+str(datos["ConfDir"][i])+"), "
    respuestas_web += "("+str(i+1)+", "+str(7)+", "+str(datos["ConfFecha"][i])+"), "
    respuestas_web += "("+str(i+1)+", "+str(8)+", "+str(datos["Informado"][i])+"), "
    respuestas_web += "("+str(i+1)+", "+str(9)+", "+str(datos["Confiado"][i])+"), "
    respuestas_web += "("+str(i+1)+", "+str(10)+", "+str(datos["InfoTerceros"][i])+"), "
    respuestas_web += "("+str(i+1)+", "+str(11)+", "+str(datos["LeerTerm"][i])+"), "
    respuestas_web += "("+str(i+1)+", "+str(12)+", "+str(datos["AceptarTerm"][i])+")"
    
    cur.execute(respuestas_web)

conn.commit()

for i in range(len(datos)):
    
    razones_ec = "INSERT INTO encuesta.razones_ec (e_commerce_id, no_certificada, no_escuchado, "
    razones_ec += "tenido_mala_experiencia, escuchado_mala_experiencia, no_estetica, ninguno) "
    razones_ec += "values (" + str(i+1) + ", " + str(datos["NoCert"][i])
    razones_ec += ", " + str(datos["NoEsc"][i]) + ", " + str(datos["MalExp"][i])
    razones_ec += ", " + str(datos["MalExpAm"][i]) + ", " + str(datos["NoEst"][i])
    razones_ec += ", " + str(datos["NoComNin"][i]) + ")"
    
    cur.execute (razones_ec)
    
conn.commit()

for i in range(len(datos)):
    
    respuestas_e_commerce = "INSERT INTO encuesta.respuestas_e_commerce (e_commerce_id, "
    respuestas_e_commerce += "escalares_e_commerce_id, respuesta) values "
    respuestas_e_commerce += "("+str(i+1)+", "+str(1)+", "+str(datos["ConfNoFraude"][i])+"), "
    respuestas_e_commerce += "("+str(i+1)+", "+str(2)+", "+str(datos["ConfNoRobo"][i])+"), "
    respuestas_e_commerce += "("+str(i+1)+", "+str(3)+", "+str(datos["ConfBienDatos"][i])+")"

    cur.execute (respuestas_e_commerce)    


conn.commit()

conn.close()


