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

const transactions = {
  "sum": -2162.2999999999997, 
  "transactions": [
    {
      "amount": -52.96, 
      "bookingDate": "2016-09-30", 
      "counterPartyName": "Lidl", 
      "originIban": "DE10000000000000000997", 
      "usage": "POS MIT PIN. Einkauf"
    }, 
    {
      "amount": -223.45, 
      "bookingDate": "2016-09-29", 
      "counterPartyName": "Rewe AG", 
      "originIban": "DE10000000000000000997", 
      "usage": "POS MIT PIN. Einkauf"
    }, 
    {
      "amount": -400.0, 
      "bookingDate": "2016-09-25", 
      "counterPartyName": "Deutsche Bank", 
      "originIban": "DE10000000000000000997", 
      "usage": "Barauszahlung, Markt"
    }, 
    {
      "amount": -60.95, 
      "bookingDate": "2016-09-24", 
      "counterPartyName": "Hotel sales", 
      "originIban": "DE10000000000000000997", 
      "usage": "POS MIT PIN. Danke, dass wir bei uns \u00fcbernachtet haben"
    }, 
    {
      "amount": -9.55, 
      "bookingDate": "2016-09-23", 
      "counterPartyName": "Starbucks", 
      "originIban": "DE10000000000000000997", 
      "usage": "Rechnung"
    }, 
    {
      "amount": -29.99, 
      "bookingDate": "2016-09-21", 
      "counterPartyName": "Fintechs rule!", 
      "originIban": "DE10000000000000000997", 
      "usage": "POS MIT PIN. Danke f\u00fcr ihren Besuch unserer Messe"
    }, 
    {
      "amount": -7.99, 
      "bookingDate": "2016-09-20", 
      "counterPartyName": "Levitating Noodle Creature Chinese food", 
      "originIban": "DE10000000000000000997", 
      "usage": "Rechnung 35457124346"
    }, 
    {
      "amount": -60.0, 
      "bookingDate": "2016-09-19", 
      "counterPartyName": "Deutsche Bahn Bu\u00dfgeldstelle", 
      "originIban": "DE10000000000000000997", 
      "usage": "Fahren ohne g\u00fcltigen Fahrausweis Strecke W\u00fcrzburg - Frankfurt"
    }, 
    {
      "amount": -29.99, 
      "bookingDate": "2016-09-19", 
      "counterPartyName": "Muckibude am Stachus", 
      "originIban": "DE10000000000000000997", 
      "usage": "SEPA-BASISLASTSCHRIFT Allin or nothing"
    }, 
    {
      "amount": -19.99, 
      "bookingDate": "2016-09-19", 
      "counterPartyName": "Telekom AG", 
      "originIban": "DE10000000000000000997", 
      "usage": "SEPA-BASISLASTSCHRIFT  Abrechnung 0171-658811RNGNR FLAT L"
    }, 
    {
      "amount": -650.0, 
      "bookingDate": "2016-09-18", 
      "counterPartyIban": "DE90100400000123456789", 
      "counterPartyName": "Norbert H\u00fcgelhof", 
      "originIban": "DE10000000000000000997", 
      "usage": "Miete"
    }, 
    {
      "amount": -63.58, 
      "bookingDate": "2016-09-16", 
      "counterPartyName": "Lidl", 
      "originIban": "DE10000000000000000997", 
      "usage": "POS MIT PIN. Einkauf"
    }, 
    {
      "amount": -19.05, 
      "bookingDate": "2016-09-13", 
      "counterPartyName": "Rossmann", 
      "originIban": "DE10000000000000000997", 
      "usage": "POS MIT PIN. Mein Drogeriemarkt, Leipziger Str."
    }, 
    {
      "amount": -350.0, 
      "bookingDate": "2016-09-13", 
      "counterPartyName": "Deutsche Bank", 
      "originIban": "DE10000000000000000997", 
      "usage": "Barauszahlung, Bahnhof"
    }, 
    {
      "amount": -15.25, 
      "bookingDate": "2016-09-08", 
      "counterPartyName": "Lidl", 
      "originIban": "DE10000000000000000997", 
      "usage": "POS MIT PIN. Einkauf"
    }, 
    {
      "amount": -169.55, 
      "bookingDate": "2016-09-02", 
      "counterPartyName": "Alte Leipziger", 
      "originIban": "DE10000000000000000997", 
      "usage": "SEPA-BASISLASTSCHRIFT Rente Ref 8897654"
    }
  ]
}

const saveAndClose = () => {

	let country = document.getElementById('autocomplete-input');
	let start = document.getElementById('start-day');
	let finish = document.getElementById('finish-day');

	// console.log(country.value, start.value, finish.value);



	$('#addModal').modal('close');
}