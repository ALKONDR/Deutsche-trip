$(document).ready(() => {
	$('.parallax').parallax();
	$('.modal').modal();
	$('.datepicker').pickadate({
		selectMonths: true,
		selectYears: 15
	});

	let countries = [];
	let data = {};

	$.ajax({
		url: 'http://localhost:5000/api/countries',
		header:{'Access-Control-Allow-Origin': 'http://localhost:5000/'},
		success: function(result) {
			countries = result;
		},
	}).done(() => {
		countries.forEach(el => {data[el] = null});

		$('input.autocomplete').autocomplete({
			data: data,
			limit: 5,
		});
	});
});
