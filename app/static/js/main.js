document.addEventListener('DOMContentLoaded', function() {
	iniciarApp();
});

function iniciarApp() {
	navFix();
	scrollNav();
}

function navFix() {
	const barra = document.querySelector('.header');
	const onSobreN = document.querySelector('.title-sn');

	window.addEventListener('scroll', function() {
		if (onSobreN.getBoundingClientRect().top < 0){
			barra.classList.add('fijo');
		}
		else{
			barra.classList.remove('fijo');
		}
	});
}


function scrollNav(){
	const enlaces = document.querySelectorAll('.navbar a');
	
	enlaces.forEach( enlace => {
		enlace.addEventListener('click', function(e){
			e.preventDefault();
			
			const seccionScroll = e.target.attributes.href.value;
			const seccion = document.querySelector(seccionScroll);
			seccion.scrollIntoView({behavior:"smooth"});
		});
	});
}

