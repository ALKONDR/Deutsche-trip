const month2Num = {
	'January,': 1,
	'February,': 2,
	'March,': 3,
	'April,': 4,
	'May,': 5,
	'June,': 6,
	'July,': 7,
	'August,': 8,
	'September,': 9,
	'October,': 10,
	'November,': 11,
	'December': 12,
}

const openAddModal = () => {
	// let status = 0;
	// $.ajax({
	// 	url: 'http://localhost:5000/api/status',
	// 	header:{'Access-Control-Allow-Origin': 'http://localhost:5000/'},
	// 	success: function(result) {
	// 		status += result.deutsche_status + result.instagram_status;
	// 		// console.log(result);
	// 	}
	// }).done(() => {
	// 	if (status == 2)
	// 	else {
	// 		let $toastContent = $('<span>Sign in with instagram and DB please</span>');
	// 		Materialize.toast($toastContent, 5000);
	// 	}
	// });
	$('#addModal').modal('open');
}

const saveAndClose = () => {

	let country = document.getElementById('autocomplete-input');
	let start = document.getElementById('start-day');
	let finish = document.getElementById('finish-day');

	// console.log(country.value, start.value, finish.value);

	

	$('#addModal').modal('close');
}