  // This script runs after the DOM is fully loaded
  document.addEventListener('DOMContentLoaded', function () {
    console.log("printed");
var searchInput = document.querySelector('input[name="search_input"]');
var autocomplete = new google.maps.places.Autocomplete(searchInput, { 
  types: ['geocode'],
  componentRestrictions: {}
});

autocomplete.addListener('place_changed', function () { 
  var near_place = autocomplete.getPlace(); 
  console.log(near_place); // Log the selected place details
});
});