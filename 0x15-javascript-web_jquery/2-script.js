#!/usr/bin/node

$(function () {
  /* Attach a click event handler to an element with the ID "#red_header" */
  $('#red_header').click(function () {
    $(this).css('color', '#FF0000');
  });
});
