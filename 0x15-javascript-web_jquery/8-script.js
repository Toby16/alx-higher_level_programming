#!/usr/bin/node

$(function () {
  $.ajax({
    /* api url provided */
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    success: function (data) {
      // console.log(data["results"]);
      $.each(data.results, function (i, item) {
        /* append every movie title to ul list */
        $('#list_movies').append('<li>' + item.title + '</li>');
      });
    }
  });
});
