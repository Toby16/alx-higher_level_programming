#!/usr/bin/node

// Using jQuery to handle the "DOMContentLoaded" event
$(document).ready(function () {
  $.ajax({
    url: 'https://fourtonfish.com/hellosalut/?lang=fr',
    success: function (data) {
      $('#hello').text(data.hello);
    }
  });
});
