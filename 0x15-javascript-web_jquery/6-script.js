#!/usr/bin/node

$(function () {
  /* Attach a click event handler to the id "update_header" of element '<div>' */
  $('#update_header').click(function () {
    /* updates the text of the <header> element to New Header!!! on click */
    $('header').text('New Header!!!');
  });
});
