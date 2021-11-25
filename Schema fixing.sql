create table tipo_pregunta(
	tipo_pregunta_id numeric(4) constraint pk_tipo_pregunta primary key,
	descripcion varchar(50) not null
);

create sequence tipo_pregunta_seq start 1 increment 1;
alter table tipo_pregunta alter column tipo_pregunta_id
set default nextval('tipo_pregunta_seq');

create table preguntas_escalares (
	preguntas_escalares_id numeric(4) constraint pk_preguntas_escalares primary key,
	tipo_pregunta_id numeric(4) references tipo_pregunta (tipo_pregunta_id) not null,
	usuario_id numeric(4) references usuarios(usuario_id) not null,
	valor numeric(1) not null
);

create sequence preguntas_escalares_seq start 1 increment 1;
alter table preguntas_escalares alter column preguntas_escalares_id
set default nextval('preguntas_escalares_seq');

alter table preguntas_escalares drop column usuario_id;
alter table preguntas_escalares add column pregunta varchar(60);

create table respuestas_escalares(
	preguntas_escalares_id numeric(4) references preguntas_escalares (preguntas_escalares_id) on update cascade,
	usuario_id numeric(4) references usuarios (usuario_id) on update cascade,
	constraint pk_respuestas_escalares primary key (preguntas_escalares_id, usuario_id),
	respuesta numeric(1) not null
);

	
alter table perfil_usuario add column ubicacion varchar(50) not null;

alter table apps_web drop column tiempo_redes;

alter table social_media add column tiempo_redes numeric(4) not null;

create table dato (
	dato_id numeric(4) constraint pk_dato primary key,
	descricpion varchar(50) not null
);

create table dato_no_ingresado (
	social_media_id numeric(4) references social_media (social_media_id) on update cascade,
	dato_id numeric(4) references dato (dato_id) on update cascade,
	constraint pk_dato_no_ingresado primary key (social_media_id, dato_id)
);

create table situaciones (
	situacion_id numeric(4) constraint pk_situaciones primary key,
	tipo_pregunta numeric(4) references tipo_pregunta (tipo_pregunta_id) not null,
	descripcion varchar(50) not null
);

create table respuestas_situaciones (
	situacion_id numeric(4) references situaciones (situacion_id) on update cascade,
	usuario_id numeric(4) references usuarios(usuario_id) on update cascade,
	constraint pk_respuestas_situaciones primary key (situacion_id, usuario_id)
);

alter table e_commerce add column pago_favorito numeric(4) references formas_pago (forma_pago_id);
alter table e_commerce add column pago_confiable numeric(4) references formas_pago (forma_pago_id);
alter table e_commerce drop column razones_id;

create table razones (
	razon_id numeric(4) constraint pk_razones primary key,
	descripcion varchar(50) not null
);

create table razones_commerce (
	e_commerce_id numeric(4) references e_commerce (e_commerce_id) on update cascade,
	razon_id numeric(4) references razones (razon_id) on update cascade,
	constraint pk_razones_commerce primary key (e_commerce_id, razon_id)
);
	