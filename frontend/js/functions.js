const month2Num = {
	'January,': '01',
	'February,': '02',
	'March,': '03',
	'April,': '04',
	'May,': '05',
	'June,': '06',
	'July,': '07',
	'August,': '08',
	'September,': '09',
	'October,': '10',
	'November,': '11',
	'December,': '12',
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

const getDateQuery = (rawData) => {
	let tmp = rawData.value.split(' ');
	console.log(tmp);
	return tmp[2] + month2Num[tmp[1]] + (tmp[0] < 10 ? '0' + tmp[0] : tmp[0]);
}

const rawFactory = (photos) => {

	let carousel = document.createElement("div");
	carousel.class = 'carousel carousel-slider';
	carousel.id = 'carousel';

	photos.forEach(element => {
		let a = document.createElement('a');
		a.className = "carousel-item";

		let img = document.createElement('img');
		img.src = element.photo_url;

		a.appendChild(img);

		// carousel = document.getElementById('carousel');
		carousel.appendChild(a);
	});

	let trans = document.createElement('a');
	trans.className = "waves-effect waves-teal btn-flat";
	let text = document.createTextNode("Transactions");
	trans.appendChild(text);
}

const tableFactory = (payments) => {
	let modal = document.createElement('div');
	modal.className = 'modal';
	modal.id = 'table' + String(payments.sum);

	let content = document.createElement('div');
	content.className = 'modal-content';

	let h4 = document.createElement('div');

	content.appendChild(h4);

	let table = document.createElement('table');
	table.className = 'striped';
	let thread = document.createElement('thread');
	let trHead = document.createElement('tr');

	let th1 = document.createElement('th');
	let th2 = document.createElement('th');
	let th3 = document.createElement('th');

	
}

const fillTable = (payments) => {

}

const saveAndClose = () => {

	let country = document.getElementById('autocomplete-input');
	let start = getDateQuery(document.getElementById('start-day'));
	let finish = getDateQuery(document.getElementById('finish-day'));

	// console.log(country.value, start.value, finish.value);

	let payments = undefined;
	$.ajax({
		url: `http://127.0.0.1:5000/api/deutsche/transactions/${start}/${finish}`,
		header:{'Access-Control-Allow-Origin': 'http://127.0.0.1:5000/'},
		success: function(result) {
			payments = result;
		},
	}).done(() => {

	});

	let photos = undefined;
	$.ajax({
		url: `http://127.0.0.1:5000/api/get_photos_any/${country}/${start}/${finish}`,
		header:{'Access-Control-Allow-Origin': 'http://127.0.0.1:5000/'},
		success: function(result) {
			photos = result;
		},
	}).done(() => {

	});

	rawFactory(photos);


	$('#addModal').modal('close');
}

// const loadData = () => {
// 	if (localStorage["Transactions"] === undefined)
// 		localStorage["Transactions"] = '{}';

// 	const dataTable = JSON.parse(localStorage["Transactions"]);

// }