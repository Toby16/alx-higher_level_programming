#!/usr/bin/node

$(function () {
  /* Attach click event handler to id 'add_item' of element '<div>' */
  $('#add_item').click(function () {
    /* enable append to unordered-list element on click */
    $('ul.my_list').append('<li>Item</li>');
  });
});
