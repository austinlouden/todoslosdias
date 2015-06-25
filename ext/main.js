document.addEventListener('DOMContentLoaded', function() {
  Parse.initialize("NtKF1qDEmxpwm2OWLc2rFbxfDfetUAnfu4NRfZVF", "OGjvXV3nKnf5Pp9g6QOijtYZF9LATNqIaiTQJQjQ");
  var Card = Parse.Object.extend("Card");
  var query = new Parse.Query(Card);
  query.equalTo("cid", 1);

  query.find({
    success: function(results) {
      for (var i = 0; i < results.length; i++) {
        var object = results[i];
        var imageFile = object.get('picture');
        var imageURL = imageFile.url();
        document.getElementById('spanish').textContent = object.get('spanish');
        document.getElementById('english').textContent = object.get('english');
        document.getElementById('speech').textContent = object.get('speech');
        document.getElementById('ex_span').textContent = object.get('ex_span');
        document.getElementById('image').src = imageURL;
        document.getElementById('ex_span').title = object.get('ex_eng');

        $(function () {
          $('[data-toggle="tooltip"]').tooltip()
        }) 
      }
    },
    error: function(error) {
    }
  });
});
