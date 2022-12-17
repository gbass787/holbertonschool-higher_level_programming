$.get( "https://swapi-api.hbtn.io/api/films/?format=json", function( response ) {
  const result = response.hello
  $('DIV#hello').text(resp)
});
