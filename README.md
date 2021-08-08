# LocalBitCoin Usage Example #

	Introduccion:
	Como todas las api, el ciclo de utilizacion de la misma consta de una autenticacion para luego 
	comenzar a consumir datos. De esta forma la app queda iterando de manera periodica conta la api
	consumiendo datos para procesarlos y comunmente mostrarlos para tomar deciciones con los mismos.
	
	Para la autenticacion y consumo de datos le recomedamos ir directo a los docs de la api en cuestion.
	
	Una vez que la app tiene los datos debemos prepararla, en primer lugar para organizar esos datos, mostrarlos y
	seguir consumiendo periodicamente para que esten siempre actualizados de tal forma de poder tomar siempre
	buenas deciciones soble los mismos.
	
	loop periodico de consumo.
	
	


# Using LocalBitCoin api
	docs -> https://github.com/LocalBitcoins/lbcapi
	
	la api para localbitcoin utiliza rest (request) para consumir datos.
		request doc's -> https://requests.readthedocs.io/en/master/

# Request con asyncio
	https://www.laac.dev/blog/concurrent-http-requests-python-asyncio/
	https://gist.github.com/debugtalk/3d26581686b63c28227777569c02cf2c
	
	
# timestamp
	https://stackoverflow.com/questions/21696323/epoch-time-with-dot-1391759952-7056
	https://stackoverflow.com/questions/16755394/what-is-the-easiest-way-to-get-current-gmt-time-in-unix-timestamp-format
	
# lbc monitor 
	https://github.com/panyz522/lbc-autotrader
	
# Currency & Countries codes
	https://www.currency-iso.org/en/home/tables/table-a1.html
	https://datahub.io/core/country-list
	
	sqlite3
	.open countriesCodes.db
	create table country(ctryCd varchar(2), ccyCd varchar(3), ccyNm varchar(50), ctryNm varchar(50));
	.quit

	