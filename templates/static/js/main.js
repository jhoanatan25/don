
console.log("main.js run");
//*************************__________URL_________*************************************
/*----->*/var url = window.location.protocol+"//"+window.location.host+"/";
//*************************__________URL_________*************************************
var urlC;
var anoAct;
var anoFin=1990;

$(document).ready(function(){

	$(window).scroll(function() {
		if ( $(this).scrollTop() > 0 && $(window).width()>992) {
			$('nav').addClass('fixed');
			$('#btn_top').addClass('ver');
			$('#btn_top').removeClass('no_ver');
			$('#btn_top_b').addClass('ver');
			$('#btn_top_b').removeClass('no_ver');
		}
		else{
			$('nav').removeClass('fixed');
			$('#btn_top').removeClass('ver');
			$('#btn_top').addClass('no_ver');
			$('#btn_top_b').removeClass('ver');
			$('#btn_top_b').addClass('no_ver');
		}
	});

});

function resume(id,id2,val,btn1,btn2){
		if (val==0) {
			console.log("more resume "+id+" "+id2);
			$(id).removeClass('ver');
			$(id).addClass('no_ver');
			$(id2).removeClass('no_ver');
			$(id2).addClass('ver');
			$(btn1).removeClass('ver');
			$(btn1).addClass('no_ver');
			$(btn2).removeClass('no_ver');
			$(btn2).addClass('ver');
		}
		if (val==1) {
			console.log("more resume "+id+" "+id2);
			$(id2).removeClass('ver');
			$(id2).addClass('no_ver');
			$(id).removeClass('no_ver');
			$(id).addClass('ver');
			$(btn2).removeClass('ver');
			$(btn2).addClass('no_ver');
			$(btn1).removeClass('no_ver');
			$(btn1).addClass('ver');
		}
}

	$(document).ready(function() {
			precios =["1,000","2,000","3,000","4,000","5,000","6,000","7,000","8,000","9,000","10,000","11,000","12,000","13,000","14,000","15,000","16,000","17,000","18,000","19,000","20,000","22,000","24,000","26,000","28,000","30,000","35,000","40,000","45,000","50,000","55,000","60,000","65,000","70,000","75,000","80,000","85,000","90,000","95,000","100,000"];
			anoAct = (new Date).getFullYear();
			var sel = document.getElementById('byear');
			sel.options[0] = new Option("From Year","0","1");
			var j=0;
			for (var i=anoAct; i >=anoFin ; i--) {
					sel.options[j+1] = new Option(i,i,"1");
					j++;
			}
			var sel2 = document.getElementById('fyear');
			sel2.options[0] = new Option("To Year","10000","1");
			var j=0;
			for (var i=anoAct; i >=anoFin ; i--) {
					sel2.options[j+1] = new Option(i,i,"1");
					j++;
			}

			var sel5 = document.getElementById('bprice');
			sel5.options[0] = new Option("Price Min","0","1");
			sel5.options[1] = new Option("Any Price","1","1");
			var j=1;
			for (var i=0; i <precios.length ; i++ ) {
					sel5.options[j+1] = new Option("$ "+precios[i],precios[i],"1");
					j++;
			}

			var sel6 = document.getElementById('fprice');
			sel6.options[0] = new Option("Price Max","100000000000","1");
			sel6.options[1] = new Option("Any Price","110000000000","1");
			var j=1;
			for (var i=0; i <precios.length ; i++ ) {
					sel6.options[j+1] = new Option("$ "+precios[i],precios[i],"1");
					j++;
			}

			$("#byear").change(function(){
								var act =$('#fyear').val();
								$('#fyear')
								    .find('option')
								    .remove()
								    .end();

								var Fin =$('#byear').val();
								var sel3 = document.getElementById('fyear');
								sel3.options[0] = new Option("To Year","10000","1");
								var j=0;
								for (var i=anoAct; i >Fin ; i--) {
										sel3.options[j+1] = new Option(i,i,"1");
										j++;
								}
								$('#fyear').val(act);
		        });

				$("#fyear").change(function(){
									var act =$('#byear').val();
									$('#byear')
											.find('option')
											.remove()
											.end();

									var Fin =$('#fyear').val();
									var sel4 = document.getElementById('byear');
									sel4.options[0] = new Option("From Year","0","1");
									var j=0;
									for (var i=Fin-1; i >=anoFin ; i--) {
											sel4.options[j+1] = new Option(i,i,"1");
											j++;
									}
									$('#byear').val(act);
							});
							$("#bprice").change(function(){
												var act =$('#fprice').val();
												$('#fprice')
												    .find('option')
												    .remove()
												    .end();
												var Fin;
												var Fin2 =$('#bprice').val();
												for (var i = 0; i < precios.length; i++) {
													if (precios[i]==Fin2) {
														Fin=i;
													}
												}
												var sel6 = document.getElementById('fprice');
												sel6.options[0] = new Option("Price Max","100000000000","1");
												sel6.options[1] = new Option("Any Price","110000000000","1");
												var j=1;
												for (var i=Fin+1; i <precios.length ; i++ ) {
														sel6.options[j+1] = new Option("$ "+precios[i],precios[i],"1");
														j++;
												}
											$('#fprice').val(act);
						        });

										$("#fprice").change(function(){
															var act =$('#bprice').val();
															$('#bprice')
																	.find('option')
																	.remove()
																	.end();
															var Fin;
															var Fin2 =$('#fprice').val();
															for (var i = 0; i < precios.length; i++) {
																if (precios[i]==Fin2) {
																	Fin=i;
																}
															}

															var sel5 = document.getElementById('bprice');
															sel5.options[0] = new Option("Price Min","0","1");
															sel5.options[1] = new Option("Any Price","1","1");
															var j=1;
															for (var i=0; i <Fin ; i++ ) {
																	sel5.options[j+1] = new Option("$ "+precios[i],precios[i],"1");
																	j++;
															}
														$('#bprice').val(act);
													});

 	});
// $(document).ready(function() {
//
// 			var hrefH = url + "header.html";
// 			$('header').empty(); // Limpia el div 'contenido'
// 			$('header').load(hrefH); // Esta línea simplemente carga el contenido dentro del div 'contenido'
//
// 			var hrefF = url + "footer.html";
// 			$('footer').empty(); // Limpia el div 'contenido'
// 			$('footer').load(hrefF); // Esta línea simplemente carga el contenido dentro del div 'contenido'
//
// 			var URLactual = window.location.href;
// 			console.log(URLactual);
//
// 			var URLactual = window.location.host;
// 			console.log(URLactual);
//
// 			var URLactual = window.location.pathname;
// 			console.log(URLactual);
// 		});

function facebook()
{
	var URLactual = window.location.href;
	var link = "https://www.facebook.com/sharer/sharer.php?u="+URLactual;
	console.log(link);
	window.location.href=link;
}

function twitter()
{
	var URLactual = window.location.href;
	var link = "https://twitter.com/intent/tweet?url="+URLactual;
	console.log(link);
	window.location.href=link;
}


function _google()
{
	var URLactual = window.location.href;
	var link = "https://plus.google.com/share?url="+URLactual;
	console.log(link);
	window.location.href=link;
}


function home()
{

	var URLactual = window.location.href;
	console.log(URLactual);
	window.location = (url);
}


function clic(ruta)
{

	var URLactual = window.location.href;
	console.log(URLactual);
	window.location = (url+ruta);
}


function menu(op)
{
	console.log(op);
	$('.option').removeClass('active')

	if(op!="none")
		$(op).addClass('active')
}



function cajas()
{
	$('#box').addClass('active')
	$('#list').removeClass('active')
	$('#list').addClass('inactive')
	$('#box').removeClass('inactive')

	$('#cambiar').addClass('box')
	$('#cambiar').addClass('col-sm-6')
	$('#cambiar').addClass('col-md-3')
	$('#cambiar').removeClass('list')

	$(".box__cajas__cambiar").addClass('col-md-4');
	$(".box__cajas__cambiar").addClass('col-sm-6');
	$(".box__cajas__cambiar").removeClass('listado__carros');
}

function listas()
{
	$('#list').addClass('active')
	$('#box').removeClass('active')
	$('#box').addClass('inactive')
	$('#list').removeClass('inactive')


	$('#cambiar').removeClass('box')
	$('#cambiar').removeClass('col-sm-6')
	$('#cambiar').removeClass('col-md-3')
	$('#cambiar').addClass('list')

	$(".box__cajas__cambiar").removeClass('col-md-4');
	$(".box__cajas__cambiar").removeClass('col-sm-6');
	$(".box__cajas__cambiar").addClass('listado__carros');


}


function subir(id)
{
	var pathname = window.location.pathname;
	if (pathname == "/") {
		$('html,body').animate({
	    	scrollTop: $("#search").offset().top
		}, 1000);
	}
	else {
		window.location.href="/";
		setTimeout(function(){jQuery(id).attr('checked', true);},500);
	}

}

function arriba()
{
	$('html,body').animate({
    	scrollTop: $("#top").offset().top
	}, 1000);

}

function copyToClipboard(urlCopy) {
  var $temp = $("<input>")
  $("body").append($temp);
  $temp.val(urlCopy).select();
  document.execCommand("copy");
  $temp.remove();
}

function desplegar()
{
	$('#open').addClass('invisible')
	$('#open').removeClass('visible')

	$('#close').addClass('visible')
	$('#close').removeClass('invisible')


	$('#mostrar').addClass('view')
	$('#mostrar').removeClass('no-view')

	$('html,body').animate({
    	scrollTop: $("#mostrar").offset().top
	}, 1000);
}

function plegar()
{
	$('#close').addClass('invisible')
	$('#close').removeClass('visible')

	$('#open').addClass('visible')
	$('#open').removeClass('invisible')


	$('#mostrar').addClass('no-view')
	$('#mostrar').removeClass('view')

}

function tags(op)
{
	if (op==1) {
		$('#op1').addClass('active')
		$('#op2').removeClass('active')
		$('#op3').removeClass('active')

		$('.tag1').addClass('view')
		$('.tag1').removeClass('no-view')

		$('.tag2').addClass('no-view')
		$('.tag2').removeClass('view')

		$('.tag3').addClass('no-view')
		$('.tag3').removeClass('view')
	}
	else if (op==2){
		$('#op2').addClass('active')
		$('#op1').removeClass('active')
		$('#op3').removeClass('active')

		$('.tag2').addClass('view')
		$('.tag2').removeClass('no-view')

		$('.tag1').addClass('no-view')
		$('.tag1').removeClass('view')

		$('.tag3').addClass('no-view')
		$('.tag3').removeClass('view')

	}else{
		$('#op3').addClass('active')
		$('#op2').removeClass('active')
		$('#op1').removeClass('active')

		$('.tag3').addClass('view')
		$('.tag3').removeClass('no-view')

		$('.tag2').addClass('no-view')
		$('.tag2').removeClass('view')

		$('.tag1').addClass('no-view')
		$('.tag1').removeClass('view')
	}

}

$(document).ready(function() {
	$("#id_user").attr("placeholder", "Username");
	$('#id_user').addClass('form-control')
	$("#id_email").attr("placeholder", "Email");
	$('#id_email').addClass('form-control')
	$("#id_pasword").attr("placeholder", "Password");
	$('#id_pasword').addClass('form-control')
});

$(document).ready(function() {
	$("#id_user_D").attr("placeholder", "Username");
	$('#id_user_D').addClass('form-control')
	$("#id_email_D").attr("placeholder", "Email");
	$('#id_email_D').addClass('form-control')
	$("#id_pasword_D").attr("placeholder", "Password");
	$('#id_pasword_D').addClass('form-control')
});
// Funcion de validacion de email y paswoord del User
$(document).ready(function() {
	var pass1 = $('#id_pasword');
	var pass2 = $('#id_confirm_pass');
	function coincidePassword(){
		var valor1 = pass1.val();
		var valor2 = pass2.val();
		if(valor1 != valor2)
		{
			$('#addForm').addClass('disabled')
			$('#Mpass').addClass('view')
			$('#Mpass').removeClass('no-view')

		}
		if(valor1==valor2){
			$('#addForm').removeClass('disabled')
			$('#Mpass').removeClass('view')
			$('#Mpass').addClass('no-view')
		}
	}
	//ejecuto la función al soltar la tecla
	pass2.keyup(function(){
	coincidePassword();
	});
});

$(document).ready(function() {
	var email1 = $('#id_email');
	var email2 = $('#id_confirm_email');
	function coincideemail(){
		var valor1 = email1.val();
		var valor2 = email2.val();
		if(valor1 != valor2)
		{
			$('#addForm').addClass('disabled')
			$('#Memail').addClass('view')
			$('#Memail').removeClass('no-view')

		}
		if(valor1==valor2){
			$('#addForm').removeClass('disabled')
			$('#Memail').removeClass('view')
			$('#Memail').addClass('no-view')
		}
	}
	//ejecuto la función al soltar la tecla
	email2.keyup(function(){
	coincideemail();
	});
});

//funcion de confirmacion de email y pasword del User Dealer
$(document).ready(function() {
	var pass1 = $('#id_pasword_D');
	var pass2 = $('#id_confirm_pass');
	function coincidePassword(){
		var valor1 = pass1.val();
		var valor2 = pass2.val();
		if(valor1 != valor2)
		{
			$('#addForm').addClass('disabled')
			$('#Mpass').addClass('view')
			$('#Mpass').removeClass('no-view')

		}
		if(valor1==valor2){
			$('#addForm').removeClass('disabled')
			$('#Mpass').removeClass('view')
			$('#Mpass').addClass('no-view')
		}
	}
	//ejecuto la función al soltar la tecla
	pass2.keyup(function(){
	coincidePassword();
	});
});

$(document).ready(function() {
	var email1 = $('#id_email_D');
	var email2 = $('#id_confirm_email');
	function coincideemail(){
		var valor1 = email1.val();
		var valor2 = email2.val();
		if(valor1 != valor2)
		{
			$('#addForm').addClass('disabled')
			$('#Memail').addClass('view')
			$('#Memail').removeClass('no-view')

		}
		if(valor1==valor2){
			$('#addForm').removeClass('disabled')
			$('#Memail').removeClass('view')
			$('#Memail').addClass('no-view')
		}
	}
	//ejecuto la función al soltar la tecla
	email2.keyup(function(){
	coincideemail();
	});
});

function collapse(id,btn)
{
	if($(id).hasClass('view'))
	{
		$(id).removeClass('view')
		$(id).addClass('no-view')

		$(btn).removeClass('glyphicon glyphicon-minus');
		$(btn).addClass('glyphicon glyphicon-plus');
	}
	else
	{
		$(id).addClass('view')
		$(id).removeClass('no-view')
		$(btn).addClass('glyphicon glyphicon-minus');
		$(btn).removeClass('glyphicon glyphicon-plus');
	}
}

function more(id,idbtn)
{
	if($(id).hasClass('view'))
	{
		$(id).removeClass('view')
		$(id).addClass('no-view')
		$(idbtn).html("Mostrar más");

	}
	else
	{
		$(id).addClass('view')
		$(id).removeClass('no-view')
		$(idbtn).html("Ocultar");

	}
}

$(document).ready(function() {
	$('#used').click(function(){
		$('#allc').removeClass('active')
		$('#used').removeClass('inactive')
		$('#allc').addClass('inactive')
		$('#used').addClass('active')
	});

	$('#allc').click(function(){
		$('#allc').removeClass('inactive')
		$('#used').removeClass('active')
		$('#allc').addClass('active')
		$('#used').addClass('inactive')
	});

	$('#ran0').click(function(){
		$('#ran0').removeClass('inactive')
		$('#ran30').removeClass('active')
		$('#ran60').removeClass('active')
		$('#alld').removeClass('active')
		$('#ran0').addClass('active')
		$('#ran30').addClass('inactive')
		$('#ran60').addClass('inactive')
		$('#alld').addClass('inactive')
	});

	$('#ran30').click(function(){
		$('#ran30').removeClass('inactive')
		$('#ran0').removeClass('active')
		$('#ran60').removeClass('active')
		$('#alld').removeClass('active')
		$('#ran30').addClass('active')
		$('#ran0').addClass('inactive')
		$('#ran60').addClass('inactive')
		$('#alld').addClass('inactive')
	});

	$('#ran60').click(function(){
		$('#ran60').removeClass('inactive')
		$('#ran0').removeClass('active')
		$('#ran30').removeClass('active')
		$('#alld').removeClass('active')
		$('#ran60').addClass('active')
		$('#ran0').addClass('inactive')
		$('#ran30').addClass('inactive')
		$('#alld').addClass('inactive')
	});

	$('#alld').click(function(){
		$('#alld').removeClass('inactive')
		$('#ran0').removeClass('active')
		$('#ran30').removeClass('active')
		$('#ran60').removeClass('active')
		$('#alld').addClass('active')
		$('#ran0').addClass('inactive')
		$('#ran30').addClass('inactive')
		$('#ran60').addClass('inactive')
	});

	$('#allp').click(function(){
		$('#allp').removeClass('inactive')
		$('#yes').removeClass('active')
		$('#no').removeClass('active')
		$('#allp').addClass('active')
		$('#yes').addClass('inactive')
		$('#no').addClass('inactive')
	});

	$('#yes').click(function(){
		$('#yes').removeClass('inactive')
		$('#allp').removeClass('active')
		$('#no').removeClass('active')
		$('#yes').addClass('active')
		$('#allp').addClass('inactive')
		$('#no').addClass('inactive')
	});

	$('#no').click(function(){
		$('#no').removeClass('inactive')
		$('#yes').removeClass('active')
		$('#allp').removeClass('active')
		$('#no').addClass('active')
		$('#yes').addClass('inactive')
		$('#allp').addClass('inactive')
	});
});


function desmenu()
{
	if($('#menuDes').hasClass('view'))
	{
		$('#menuDes').removeClass('view')
		$('#menuDes').addClass('no-view')
	}
	else
	{
		$('#menuDes').addClass('view')
		$('#menuDes').removeClass('no-view')
	}
}

function dropdown(id){
	if($(id).hasClass('open')){
		$(id).removeClass('open')
	}
	else{
		$(id).addClass('open')
	}
}


function megusta(id)
{
	if($(id).hasClass('check')){
		$(id).removeClass('check')
		$(id).addClass('no-check')
	}
	else{
		$(id).removeClass('no-check')
		$(id).addClass('check')
	}
}
//
// $(function() {
// 	Morris.Donut({
// 	        element: 'photos',
// 	        data: [{
// 	            label: "With",
// 	            value: 72
// 	        },{
// 	            label: "With",
// 	            value: 28
// 	        }],
// 	        resize: true
// 	    });
//
// 	Morris.Donut({
// 	        element: 'videos',
// 	        data: [{
// 	            label: "Without",
// 	            value: 48
// 	        },{
// 	            label: "With",
// 	            value: 52
// 	        }],
// 	        resize: true
// 	    });
// });

function show_all()
{
	text = "#text-show-all";
	i = '[data-target="#morecars"] i';
	if($(i).hasClass('fa-chevron-down')){
		$(".collapse").css('display','flex')
		$(text).html('Ocultar <i class="fa fa-chevron-up" aria-hidden="true"></i>')

	}
	else{
		$(text).html('Desplegar <i class="fa fa-chevron-down" aria-hidden="true"></i>')
		$(".collapse").css('display','none')
	}
}

var des =0;
function sign_in_toogle(id){
	console.log(id);
if (des == 0 && id == 0) {
	des =1;
	$(".login-fixed").slideDown('medium',function(){
		if ($(this).is(':visible'))
				$(this).css('display','flex');
	});
	$("#log2").slideDown('medium',function(){
		if ($(this).is(':visible'))
				$(this).css('display','flex');
	});


} else {
	des =0;
	$(".login-fixed").slideUp('medium',function(){
		if ($(this).is(':visible'))
				$(this).css('display','flex');
	});
	$("#log2").slideUp('medium',function(){
		if ($(this).is(':visible'))
				$(this).css('display','flex');
	});

}


}

function sign_in_toogle2(){
	$(".login-fixed").slideUp('medium',function(){
		if ($(this).is(':visible'))
				$(this).css('display','flex');
	});
	$("#log2").slideUp('medium',function(){
		if ($(this).is(':visible'))
				$(this).css('display','flex');
	});
}


function backend(id,id2){


	if($(id).hasClass('ver')){
		console.log(id+"ver");
		$(id).addClass('no-ver')
		$(id).removeClass('ver')
		$(id2).addClass('no-ver')
		$(id2).removeClass('ver')
	}
	else{
		$(id).addClass('ver')
		$(id).removeClass('no-ver')
		$(id2).addClass('no-ver')
		$(id2).removeClass('ver')
		console.log(id+"no-ver");
		console.log(id2);
	}
}

function themeList(){



}
