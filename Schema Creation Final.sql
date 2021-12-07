create table usuarios (
	usuario_id numeric(4) constraint pk_usuarios primary key,
	genero varchar(50) not null,
	edad numeric(2) not null,
	estado_republica varchar(50) not null,
	estudiante boolean not null
);

create sequence usuarios_seq start 1 increment 1;
alter table usuarios alter column usuario_id
set default nextval('usuarios_seq');

create table area_estudio (
	area_estudio_id numeric(4) constraint pk_area_estudio primary key,
	descripcion varchar(50) not null
);

create sequence area_estudio_seq start 1 increment 1;
alter table area_estudio alter column area_estudio_id
set default nextval('area_estudio_seq');

alter table usuarios add column area_estudio_id numeric(4) references area_estudio(area_estudio_id);

create table perfil_usuario (
	perfil_usuario_id numeric(4) constraint pk_perfil_usuario primary key,
	usuario_id numeric(4) references usuarios (usuario_id) not null,
	internet_casa boolean not null,
	tiempo_diario numeric(4) not null,
	tipo_conexion varchar(50) not null,
	antivirus boolean not null
);

create sequence perfil_usuario_seq start 1 increment 1;
alter table perfil_usuario alter column perfil_usuario_id
set default nextval('perfil_usuario_seq');

create table dispositivos (
	dispositivo_id numeric(4) constraint pk_dispositivos primary key,
	nombre varchar(50) not null
);

create sequence dispositivos_seq start 1 increment 1;
alter table dispositivos alter column dispositivo_id
set default nextval('dispositivos_seq');

alter table perfil_usuario add column dispositivo_fav numeric(4) references dispositivos (dispositivo_id) not null;

create table perfil_permisos (
	perfil_permisos_id numeric(4) constraint pk_perfil_permisos primary key,
	perfil_usuario_id numeric(4) references perfil_usuario(perfil_usuario_id) not null,
	camara boolean not null,
	microfono boolean not null,
	ubicacion boolean not null,
	galeria boolean not null,
	contactos boolean not null
);

create sequence perfil_permisos_seq start 1 increment 1;
alter table perfil_permisos alter column perfil_permisos_id
set default nextval('perfil_permisos_seq');

create table usuario_dispositivos (
	usuario_dispositivos_id numeric(4) constraint pk_usuario_dispositivos primary key,
	usuario_id numeric(4) references usuarios (usuario_id) not null,
	telefono boolean not null,
	desktop boolean not null,
	laptop boolean not null,
	tablet boolean not null,
	consola boolean not null,
	other boolean not null
);

create sequence usuario_dispositivos_seq start 1 increment 1;
alter table usuario_dispositivos alter column usuario_dispositivos_id
set default nextval('usuario_dispositivos_seq');

create table social_media (
	social_media_id numeric(4) constraint pk_social_media primary key,
	usuario_id numeric(4) references usuarios (usuario_id) not null,
	tipo_redes varchar(20) not null,
	uso_historial varchar(50) not null
);

create sequence social_media_seq start 1 increment 1;
alter table social_media alter column social_media_id
set default nextval('social_media_seq');


create table redes (
	redes_id numeric(4) constraint pk_redes primary key,
	social_media_id numeric(4) references social_media (social_media_id) not null,
	facebook boolean not null,
	instagram boolean not null,
	twitter boolean not null,
	whatsapp boolean not null,
	tiktok boolean not null,
	dating boolean not null
);

create sequence redes_seq start 1 increment 1;
alter table redes alter column redes_id
set default nextval('redes_seq');

create table escalares_social_media (	
	escalares_social_media_id numeric(4) constraint pk_escalares_social_media primary key,
	pregunta varchar(70) not null
);

create sequence escalares_social_media_seq start 1 increment 1;
alter table escalares_social_media alter column escalares_social_media_id
set default nextval('escalares_social_media_seq');

create table respuestas_social_media (
	social_media_id numeric(4) references social_media (social_media_id) on update cascade,
	escalares_social_media_id numeric(4) references escalares_social_media (escalares_social_media_id) on update cascade,
	constraint pk_respuestas_social_media primary key (social_media_id, escalares_social_media_id)
);

create table web (
	web_id numeric(4) constraint pk_web primary key,
	usuario_id numeric(4) references usuarios(usuario_id) not null,
	saber_cookies boolean not null,
	accion_cookies varchar(50) not null
);

create sequence web_seq start 1 increment 1;
alter table web alter column web_id
set default nextval('web_seq');

create table escalares_web (
	escalares_web_id numeric(4) constraint pk_escalares_web primary key,
	pregunta varchar(70) not null
);

create sequence escalares_web_seq start 1 increment 1;
alter table escalares_web alter column escalares_web_id
set default nextval('escalares_web_seq');

create table respuestas_web (
	web_id numeric(4) references web (web_id) on update cascade,
	escalares_web_id numeric(4) references escalares_web (escalares_web_id) on update cascade,
	constraint pk_respuestas_web primary key (web_id, escalares_web_id)
);

create table e_commerce (
	e_commerce_id numeric(4) constraint pk_e_commerce primary key,
	usuario_id numeric(4) references usuarios (usuario_id) not null,
	porcentaje_compras numeric(4) not null,
	frecuencia varchar(50) not null,
	dato_evitar_compra boolean not null
);

create sequence e_commerce_seq start 1 increment 1;
alter table e_commerce alter column e_commerce_id
set default nextval('e_commerce_seq');

create table forma_pago (
	forma_pago_id numeric(4) constraint pk_forma_pago primary key,
	nombre varchar(50) not null
);

create sequence forma_pago_seq start 1 increment 1;
alter table forma_pago alter column forma_pago_id
set default nextval('forma_pago_seq');

alter table e_commerce add column forma_pago_id numeric(4) references forma_pago (forma_pago_id) not null;





create table escalares_e_commerce (
	escalares_e_commerce_id numeric(4) constraint pk_escalares_e_commerce primary key,
	descripcion varchar(70) not null
);

create sequence escalares_e_commerce_seq start 1 increment 1;
alter table escalares_e_commerce alter column escalares_e_commerce_id
set default nextval('escalares_e_commerce_seq');

create table respuestas_e_commerce (
	e_commerce_id numeric(4) references e_commerce (e_commerce_id) on update cascade,
	escalares_e_commerce_id numeric(4) references escalares_e_commerce (escalares_e_commerce_id) on update cascade,
	constraint pk_respuestas_e_commerce primary key (e_commerce_id, escalares_e_commerce_id),
	respuesta numeric(1) not null
);

alter table respuestas_social_media add column respuesta numeric(4) not null;
alter table respuestas_web add column respuesta numeric(4) not null;

alter table perfil_usuario add column ubicacion varchar(50) not null;

alter table social_media add column tiempo_redes varchar(50) not null;

create table datos (
	dato_id numeric(4) constraint pk_datos primary key,
	descripcion varchar(50) not null
);

create sequence datos_seq start 1 increment 1;
alter table datos alter column dato_id
set default nextval('datos_seq');

create table datos_no_ingresado (
	datos_no_ingresado_id numeric(4) constraint pk_datos_no_ingresado primary key,
	social_media_id numeric(4) references social_media(social_media_id) not null,
	nombre boolean not null,
	correo boolean not null,
	telfeono boolean not null,
	edad boolean not null,
	direccion boolean not null,
	tarjeta boolean not null,
	foto_id boolean not null,
	fecha_nacimiento boolean not null,
	ninguno boolean not null,
	otro boolean not null
);

create sequence datos_no_ingresado_seq start 1 increment 1;
alter table datos_no_ingresado alter column datos_no_ingresado_id
set default nextval('datos_no_ingresado_seq');

create table situaciones_sm (
	situacion_sm_id numeric(4) constraint pk_situaciones_sm primary key,
	social_media_id numeric(4) references social_media (social_media_id) not null,
	extorsion_telefono boolean not null,
	extorsion_mensaje boolean not null,
	robo_contrasena boolean not null,
	unauthorized_access boolean not null,
	bullying boolean not null,
	ninguno boolean not null
);

create sequence situaciones_sm_seq start 1 increment 1;
alter table situaciones_sm alter column situacion_sm_id
set default nextval('situaciones_sm_seq');



alter table e_commerce drop column dato_evitar_compra;
alter table e_commerce add column dato_evitar_compra numeric(4) references datos(dato_id) null;

create table situaciones_ec (
	situacion_ec_id numeric(4) constraint pk_situaciones_ec primary key,
	e_commerce_id numeric(4) references e_commerce(e_commerce_id) not null,
	unauthorized_charge boolean not null,
	fraude boolean not null,
	robo_identidad boolean not null,
	ninguno boolean not null
);

create sequence situaciones_ec_seq start 1 increment 1;
alter table situaciones_ec alter column situacion_ec_id
set default nextval('situaciones_ec_seq');

alter table e_commerce drop column forma_pago_id;
alter table e_commerce add column pago_favorito numeric(4) references forma_pago(forma_pago_id) not null;
alter table e_commerce add column pago_confiable numeric(4) references forma_pago(forma_pago_id) not null;



create table razones_ec (
	razones_ec_id numeric(4) constraint pk_razones_ec primary key,
	e_commerce_id numeric(4) references e_commerce (e_commerce_id) not null,
	no_certificada boolean not null,
	no_escuchado boolean not null,
	tenido_mala_experiencia boolean not null,
	escuchado_mala_experiencia boolean not null,
	no_estetica boolean not null,
	ninguno boolean not null
);

create sequence razones_ec_seq start 1 increment 1;
alter table razones_ec alter column razones_ec_id
set default nextval('razones_ec_seq');


alter table e_commerce add column uso_historial varchar(50) not null;







	











