#!/usr/bin/node

$(function () {
  /* Attach a click event handler to the element "<header>" */
  $('header').click(function () {
    $(this).addClass('red');
  });
});
