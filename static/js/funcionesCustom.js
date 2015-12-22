$(document).on("ready", function () {
		var contador = 0;
		$('#buttonFormNA').on('click', function(){
			contador = contador+1;
			var clone = $( ".datosNA" ).clone(true);
			clone.find("#nombres").attr("id", "nombres"+contador);
			clone.find("#apellidos").attr("id", "apellidos"+contador);
			clone.find("#gestante").attr("id", "gestante"+contador);
			clone.find("#sexo").attr("id", "sexo"+contador);
			clone.find("#cernac").attr("id", "cernac"+contador);
			clone.find("#estudia").attr("id", "estudia"+contador);
			clone.find("#ucurso").attr("id", "ucurso"+contador);
			clone.find("#fnac").attr("id", "fnac"+contador);
			clone.find("#domiciliodir").attr("id", "domiciliodir"+contador);
			clone.find("#telefonodir").attr("id", "telefonodir"+contador);
			clone.find("#domiciliocomunidaddir").attr("id", "domiciliocomunidaddir"+contador);
			$(clone).removeClass("datosNA").addClass("datosNA"+contador);
			$('#buttonFormNA').before(clone);
		});
		/*$('#botonDir').on('click', function(){
			contador = contador+1;
			var clone = $( ".datosDir" ).clone();
			clone.find("#domiciliodir").attr("id", "domiciliodir"+contador);
			clone.find("#telefonodir").attr("id", "telefonodir"+contador);
			clone.find("#domiciliocomunidaddir").attr("id", "domiciliocomunidaddir"+contador);
			$(clone).removeClass("datosDir").addClass("datosDir"+contador);
			$('#botonDir').before(clone);
		});*/
		$('#botonGF').on('click', function(){
			contador = contador+1;
			var clone = $( ".datosGF" ).clone();
			clone.find("#nombresgf").attr("id", "nombresgf"+contador);
			clone.find("#apellidosgf").attr("id", "apellidosgf"+contador);
			clone.find("#parentescogf").attr("id", "parentescogf"+contador);
			clone.find("#edadgf").attr("id", "edadgf"+contador);
			clone.find("#sexogf").attr("id", "sexogf"+contador);
			clone.find("#gradogf").attr("id", "gradogf"+contador);
			clone.find("#ocupaciongf").attr("id", "ocupaciongf"+contador);
			$(clone).removeClass("datosGF").addClass("datosGF"+contador);
			$('#botonGF').before(clone);
		});
		$('#botonDenunciado').on('click', function(){
			contador = contador+1;
			var clone = $( ".datosDenunciado" ).clone();
			clone.find("#anonimo").attr("id", "anonimo"+contador);
			clone.find("#nombresdeno").attr("id", "nombresdeno"+contador);
			clone.find("#apellidosdeno").attr("id", "apellidosdeno"+contador);
			clone.find("#sexodeno").attr("id", "sexodeno"+contador);
			clone.find("#edaddeno").attr("id", "edaddeno"+contador);
			clone.find("#parentescodeno").attr("id", "parentescodeno"+contador);
			clone.find("#domiciliocomunidaddeno").attr("id", "domiciliocomunidaddeno"+contador);
			clone.find("#telefonodeno").attr("id", "telefonodeno"+contador);
			clone.find("#lugardetrabajodeno").attr("id", "lugardetrabajodeno"+contador);
			clone.find("#ocupaciondeno").attr("id", "ocupaciondeno"+contador);
			clone.find("#denuncias").attr("id", "denuncias"+contador);
			clone.find("#lugardeno").attr("id", "lugardeno"+contador);
			$(clone).removeClass("datosDenunciado").addClass("datosDenunciado"+contador);
			$('#botonDenunciado').before(clone);
		});
		$('#botonAc').on('click', function(){
			contador = contador + 1;
			var clone = $( ".acciones" ).clone();
			clone.find("#acciones").attr("id", "acciones"+contador);
			$(clone).removeClass("acciones").addClass("acciones"+contador);
			$('#botonAc').before(clone);
		});
	});