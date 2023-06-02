#!/usr/bin/node

$(function () {
  $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
    success: function (data) {
      // console.log("DATA: \n", data.name);
      /* Fetch name in the API provided */
      const charName = data.name;
      $('#character').text(charName);
    }
  });
});
