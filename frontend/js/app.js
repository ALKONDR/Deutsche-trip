const authorize = () => {
	$.get('localhost:5000/', (data, status) => {
		console.log(data, status);
	});
}

$(document).ready(() => {
	$('.parallax').parallax();
	$('ul.tabs').tabs();
});