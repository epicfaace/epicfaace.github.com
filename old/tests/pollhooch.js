jQuery.ajax({
	type:"GET",
	url:"http://www.google.com/recaptcha/api/challenge?k=6LdXvuYSAAAAAJJhkODYw0X09bgn77lC-UXsOKqM&ajax=1&cachestop=0.6509875061456114&lang=en",
	error: function(data) {
	console.log(1,data); },
	beforeSend: function (xhr) {
    xhr.setRequestHeader('Accept','*/*');
    xhr.setRequestHeader('Cache-Control','max-age=0');
    xhr.setRequestHeader('Referer','http://lms.usatodayhss.com/atlanta/polls/viewpoll/14-vote-for-the-local-high-school-football-game-of-the-week-for-oct-11'),
    xhr.setRequestHeader('Access-Control-Allow-Origin','*') }
});

curl 'http://www.google.com/recaptcha/api/challenge?k=6LdXvuYSAAAAAJJhkODYw0X09bgn77lC-UXsOKqM&ajax=1&cachestop=0.6509875061456114&lang=en'
-H 'DNT: 1'
-H 'Accept-Encoding: gzip,deflate,sdch'
-H 'Host: www.google.com' 
-H 'Accept-Language: en-US,en;q=0.8,ta;q=0.6'
-H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.8 Safari/537.36'
-H 'X-Chrome-UMA-Enabled: 1'
-H 'X-Chrome-Variations: CLi1yQEIkrbJAQimtskBCKm2yQEIroTKAQi3hcoBCJWKygE='
-H 'Accept: */*'
-H 'Cache-Control: max-age=0'
-H 'Referer: http://lms.usatodayhss.com/atlanta/polls/viewpoll/14-vote-for-the-local-high-school-football-game-of-the-week-for-oct-11'
-H 'Connection: keep-alive' --compressed