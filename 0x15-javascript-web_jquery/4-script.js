#!usr/bin/node

$(function () {
  /* Attach a click event handler to the id "#toggle_header" of element '<div>' */
  $('#toggle_header').click(function () {
    /* check is <header> is of class 'green' or 'red' */
    /* perform appropriate operations by toggling between class 'red' and 'green' */
    if ($('header').hasClass('green')) {
      $('header').removeClass('green');
      $('header').addClass('red');
    } else {
      $('header').removeClass('red');
      $('header').addClass('green');
    }
  });
});
