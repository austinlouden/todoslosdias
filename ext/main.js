$(document).ready(function() {
  console.log("doc ready");
  // setup parse
  var appId = "NtKF1qDEmxpwm2OWLc2rFbxfDfetUAnfu4NRfZVF";
  var apiKey = "OGjvXV3nKnf5Pp9g6QOijtYZF9LATNqIaiTQJQjQ";
  Parse.initialize(appId, apiKey);

  var Card = Parse.Object.extend("Card");
  var query = new Parse.Query(Card);

  $(".container").hide();

  query.count({
    success: function(number) {
      var rand = Math.floor((Math.random() * number) + 1);
      query = new Parse.Query(Card);
      query.equalTo("cid", rand);

      query.find({
        success: function(results) {
          for (var i = 0; i < results.length; i++) {

            var object = results[i];

            // card text
            var spanish = object.get('spanish');
            var english = object.get('english');
            var speech = object.get('speech');
            var ex_span = object.get('ex_span');
            var ex_eng = object.get('ex_eng');
           
            document.getElementById('spanish').textContent = spanish;
            document.getElementById('english').textContent = english;
            document.getElementById('speech').textContent = speech;
            document.getElementById('ex_span').textContent = ex_span;
            document.getElementById('ex_span').title = ex_eng;

            // card image
            var imageFile = object.get('picture');
            var img = new Image();
            document.getElementById('image').src = imageFile.url();
            document.getElementById('image').onload = function(){$(".container").fadeIn(200)}
            //img.src = imageFile.url(); 
            //img.onload = function(){$(".container").show()}
            //$("#image").replaceWith(img);

            
            $(function () {
              $('[data-toggle="tooltip"]').tooltip()
            }) 


          }
        },
        error: function(error) {
        }
      });
    },
    error: function(error) {}
  });
});
