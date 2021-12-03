insert into usuarios (genero, edad, estado_republica, estudiante, area_estudio_id)
values ('Femenino', 20, 'Veracruz', true, 4);

insert into usuario_dispositivos (usuario_id, dispositivo_id)
values (1, 1), (1, 3), (1, 4), (1, 5);

insert into perfil_usuario (usuario_id, internet_casa, tiempo_diario, tipo_conexion, antivirus, dispositivo_fav, ubicacion)
values (1, true, 2.5, 'Red Privada', true, 1, 'Solo al usar');

insert into perfil_usuario_permiso (perfil_usuario_id, permiso_id)
values (1, 3);
--Este 1 corresponde al id de perfil_usuario

insert into social_media (usuario_id, tipo_redes, uso_historial, tiempo_redes)
values (1, 'Publicas', 'Desacuerdo', 1.5);

insert into social_media_redes (social_media_id, red_id)
values (1, 1), (1, 2), (1, 3), (1, 4), (1, 5);
-- 1 del perfil de social media

insert into respuestas_social_media (social_media_id, escalares_social_media_id, respuesta)
values (1, 1, 3);

insert into respuesta_situacion_sm (social_media_id, situacion_sm_id)
values (1, 6);

insert into dato_no_ingresado (social_media_id, dato_id)
values (1, 2), (1, 3), (1, 5);

insert into web (usuario_id, saber_cookies,accion_cookies)
values (1, true, 'Acepta');

insert into respuestas_web (web_id, escalares_web_id, respuesta)
values (1, 1, 3), (1, 2, 3), (1, 3, 2), (1, 4, 1), (1, 5, 1), (1, 6, 1),(1, 7, 3), (1, 8, 3), (1, 9, 2), (1, 10, 2), (1, 11, 1), (1, 12, 4);

insert into e_commerce (usuario_id, porcentaje_compras, frecuencia, dato_evitar_compra, pago_favorito, pago_confiable, uso_historial)
values (1, 10.5, 'Mes', 7, 5, 5, 'Desacuerdo');

insert into respuestas_situaciones_ec (e_commerce_id, situacion_ec_id)
values (1, 4);

insert into respuestas_e_commerce (e_commerce_id, escalares_e_commerce_id, respuesta)
values (1, 1, 3), (1, 2, 2), (1, 3, 2);

insert into razones_ec (e_commerce_id,razon_id)
values (1, 1), (1, 3), (1, 4);

select * from razones r;

select * from escalares_e_commerce eec;

select * from situaciones_ec se;

select * from forma_pago fp;

select * from escalares_web ew;

select * from datos;

select * from redes r;

select * from permisos;

select * from dispositivos d;
