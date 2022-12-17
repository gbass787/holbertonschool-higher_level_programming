$.get( "https://swapi-api.hbtn.io/api/films/?format=json", function( response ) {
  const result = response.results
  $.each(result, function (index, value) {
        $('UL#list_movies').append('<li>' + value.title + '</li>');
      });
});
