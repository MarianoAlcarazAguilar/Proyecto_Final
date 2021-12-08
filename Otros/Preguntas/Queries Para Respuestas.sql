--Relación entre tiempo, confianza e informado?
with 
informado as (select  pu.tiempo_diario,  avg(rw.respuesta) as informado_prom
	from perfil_usuario pu join usuarios u using (usuario_id)
	join web w using (usuario_id)
	join respuestas_web rw using (web_id)
	join escalares_web ew using (escalares_web_id)
	where ew.escalares_web_id in (8)
	group by tiempo_diario 
	order by tiempo_diario), 
confianza as (select  pu.tiempo_diario,  avg(rw.respuesta) as confianza_prom
	from perfil_usuario pu join usuarios u using (usuario_id)
	join web w using (usuario_id)
	join respuestas_web rw using (web_id)
	join escalares_web ew using (escalares_web_id)
	where ew.escalares_web_id in (9)
	group by tiempo_diario 
	order by tiempo_diario)
select tiempo_diario, (informado_prom)*100/3 as prom_info, (confianza_prom)*100/3 as prom_conf
from informado join confianza using (tiempo_diario);





--Relación entre informado y confianza
with 
informado as (select usuario_id, rw.respuesta as resp_info
	from usuarios u join web w using (usuario_id)
	join respuestas_web rw using (web_id)
	join escalares_web ew using (escalares_web_id)
	where ew.escalares_web_id = 8),
confianza as (select usuario_id, rw.respuesta as resp_conf
	from usuarios u join web w using (usuario_id)
	join respuestas_web rw using (web_id)
	join escalares_web ew using (escalares_web_id)
	where ew.escalares_web_id = 9)
select resp_info, (avg(resp_conf)) * 100 / 3 as prom_confianza
from informado join confianza using (usuario_id)
group by resp_info
order by resp_info asc;


--¿Cómo afecta tu acción con cookies qué tan de acuerdo estás con compartir información con terceros?
select accion_cookies, avg(respuesta)*100/3 as prom_compartir_con_terceros
from web w join respuestas_web rw using (web_id)
join escalares_web ew using (escalares_web_id)
where ew.escalares_web_id = 10
group by accion_cookies
order by avg(respuesta) desc;


--De los que aceptan los términos, qué tantos lo leen
with
leer as (select usuario_id, rw.respuesta as resp_leer_terminos
	from usuarios u join web w using (usuario_id)
	join respuestas_web rw using (web_id)
	join escalares_web ew using (escalares_web_id)
	where ew.escalares_web_id = 11),
aceptar as (select usuario_id, rw.respuesta as resp_aceptar_terminos
	from usuarios u join web w using (usuario_id)
	join respuestas_web rw using (web_id)
	join escalares_web ew using (escalares_web_id)
	where ew.escalares_web_id = 12)
select resp_aceptar_terminos, avg(resp_leer_terminos)*100/3 as promedio_leer_terminos
from leer join aceptar using (usuario_id)
group by resp_aceptar_terminos
having resp_aceptar_terminos != 0
order by resp_aceptar_terminos;



--De los que leen los términos, que tantos los aceptan
with
leer as (select usuario_id, rw.respuesta as resp_leer_terminos
	from usuarios u join web w using (usuario_id)
	join respuestas_web rw using (web_id)
	join escalares_web ew using (escalares_web_id)
	where ew.escalares_web_id = 11),
aceptar as (select usuario_id, rw.respuesta as resp_aceptar_terminos
	from usuarios u join web w using (usuario_id)
	join respuestas_web rw using (web_id)
	join escalares_web ew using (escalares_web_id)
	where ew.escalares_web_id = 12)
select resp_leer_terminos, avg(resp_aceptar_terminos)*100/3 as promedio_aceptar_terminos
from leer join aceptar using (usuario_id)
group by resp_leer_terminos
order by resp_leer_terminos;


--De las personas que tienen sus cuentas en privada o pública que tanto les importa su el uso de su información personal en redes
select tipo_redes, avg(respuesta)*100/3 as prom_preocup_info
from usuarios u join social_media sm using (usuario_id)
join respuestas_social_media rsm using (social_media_id)
join escalares_social_media esm using (escalares_social_media_id)
group by tipo_redes;


--Cómo afecta tu tiempo en línea tu porcentaje de compras en línea
select tiempo_diario , avg(ec.porcentaje_compras)*100 as prom_online_compras
from perfil_usuario pu join usuarios u using (usuario_id)
join e_commerce ec using (usuario_id)
group by tiempo_diario
order by tiempo_diario;

--Cómo afecta tu confianza general en tus compras en línea 
select rw.respuesta as conf_uso_info, avg(ec.porcentaje_compras) * 100 as prom_online_compras
from escalares_web ew join respuestas_web rw using (escalares_web_id)
join web w using (web_id)
join usuarios u using (usuario_id)
join e_commerce ec using (usuario_id)
where ew.escalares_web_id = 9
group by rw.respuesta 
order by rw.respuesta;


--Confianza para subir correo de los que han sido o no extorsionados por correo
select ss.extorsion_mensaje, avg(respuesta) *100/3
from social_media sm join situaciones_sm ss using (social_media_id)
join usuarios u using (usuario_id)
join web w using (usuario_id)
join respuestas_web rw using (web_id)
join escalares_web ew using (escalares_web_id)
where ew.escalares_web_id = 2
group by ss.extorsion_mensaje;


--Porcentaje de hombres y mujeres que han sufrido acoso
--Cuántos hombres y mujeres han sufrido acoso
select genero, count(*) as absoluto, count(*)*100/44 as porcentaje
from usuarios u join social_media sm using (usuario_id)
join situaciones_sm ss using (social_media_id)
where ss.bullying = true
group by genero;


--Pagos favoritos vs pagos confiables
with
favoritos as (select fp.forma_pago_id,  count(*) as favs
	from forma_pago fp join e_commerce ec on fp.forma_pago_id = ec.pago_favorito
	group by fp.forma_pago_id 
	order by favs desc),
confiables as (select fp.forma_pago_id , count(*) as confs
	from forma_pago fp join e_commerce ec on fp.forma_pago_id = ec.pago_confiable 
	group by fp.forma_pago_id 
	order by confs desc)
select  nombre, favs as total_fav_abs, favs*100/256 as total_fav_porc, confs as total_conf_abs, confs*100/256 as total_conf_porc
from favoritos  join confiables using (forma_pago_id)
join forma_pago using (forma_pago_id)
order by total_fav_abs desc;



















