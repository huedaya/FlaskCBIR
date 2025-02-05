// ----- custom js ----- //

// hide initial
// $("#searching").hide();
// $("#results-table").hide();
$("#error").hide();

// global
var url = 'https://mk-main.sgp1.digitaloceanspaces.com/cbir-dataset/example/example/';
var data = [];

$(function() {

  // sanity check
  console.log( "ready!" );

  // image click
  $(".query img").click(function() {
    $('.query img').removeClass("active");
    // empty/hide results
    $("#results").empty();
    // $("#results-table").hide();
    $("#error").hide();

    // add active class to clicked picture
    $(this).addClass("active")

    // grab image url
    var image = $(this).attr("src")
    console.log(image)

    // show searching text
    $("#searching").show();
    console.log("searching...")

    // ajax request
    $.ajax({
      type: "POST",
      url: "/search",
      data : { img : image },
      // handle success
      success: function(result) {
        console.log(result.results);
        var data = result.results

		for (var i = 0; i < data.length; i++) {
		  $("#results-table").append('<tr><th><a href="'+url+data[i].image+'"><img src="'+url+data[i].image+
		    '" class="result-img"></a></th><th>'+data[i].score+'</th></tr>')
		};
      },
      // handle error
      error: function(error) {
        console.log(error);
        // append to dom
        $("#error").append()
      }
    });

    // show table
$("#results-table").show();

  });

});