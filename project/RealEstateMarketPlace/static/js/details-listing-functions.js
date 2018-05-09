window.onload = function() {

	function getCookie(name) {
		var cookieValue = null;
		if (document.cookie && document.cookie !== '') {
			var cookies = document.cookie.split(';');
			for (var i = 0; i < cookies.length; i++) {
				var cookie = jQuery.trim(cookies[i]);
				// Does this cookie string begin with the name we want?
				if (cookie.substring(0, name.length + 1) === (name + '=')) {
					cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
					break;
				}
			}
		}
		return cookieValue;
	}
	var csrftoken = getCookie('csrftoken');
	
	$("#submitMessage").click(function(ev) {
		ev.preventDefault();

		listing_id = $(this).attr("data-list");
		var post_data = {
			'csrfmiddlewaretoken':csrftoken,
			'message':$("#messageContent").val(),
		}
		$.ajax({
			url:"/"+listing_id+"/message/",
			type:'POST',
			data:post_data,
			success: function(data){
				$("#alertMessage").text(data["message"]);
				$("#alertMessage").css("display", "block");
				$("#alertMessage").delay(1000).fadeOut(400);
			},
		});
		
	}); 

	$("#favButton").click(function(ev) {
		ev.preventDefault();

		listing_id = $(this).attr("data-list");

		$.get("/" + listing_id + "/favorite", function(data) {
			if(data["status"] == "ok") {
				if(data["message"].indexOf("added") != -1)
					$("#favButton").html('<i class="fas fa-star"></i> Remove from favorites');
				else
					$("#favButton").html('<i class="far fa-star"></i> Add to favorites');

				$("#alertMessage").text(data["message"]);
				$("#alertMessage").css("display", "block");
				$("#alertMessage").delay(1000).fadeOut(400);
			} else
				alert("Error");
		});
	});

	$("#closeButton").click(function(ev) {
		ev.preventDefault();

		listing_id = $(this).attr("data-list");

		$.get("/" + listing_id + "/close", function(data) {
			if(data["status"] == "ok") {
				if(data["message"].indexOf("opened") != -1)	//if listing is opened
				{
					$("#closeButton").html('<i class="fas fa-lock"></i> Close');
					$("#closeButton").attr('class','btn btn-dark fav-button');
					$("#listing-header").removeClass('listing-closed');
				}
				else
				{
					$("#listing-header").addClass('listing-closed');
					$("#closeButton").html('<i class="fas fa-lock-open"></i> Open');
					$("#closeButton").attr('class','btn btn-light fav-button');
				}

				$("#alertMessage").text(data["message"]);
				$("#alertMessage").css("display", "block");
				$("#alertMessage").delay(1000).fadeOut(400);
			} else
				alert("Error");
		});
	});
}