$(document).ready(function(){
  $("#thankyouMessage").hide();
  $("#thumbs-up").click(function(){
      $("#thumbs-up").html("<i class=\"fas fa-thumbs-up faico\"></i>");


    });
    $("#thumbs-down").click(function(){
        $("#thumbs-down").html("<i class=\"fas fa-thumbs-down faico\"></i>");
  
        
    });

    $('form').on('submit', function(event){

        $.ajax({

          data : {
              mail : $('#mail').val(),
              feedback : $('#feedback').val()
            },
            type : 'POST',
            url : '/contact/form' 
          })
          .done(function(data){
            if(data){
              $('#thankyouMessage').show();
              alert("Your response has been recorded");
            }


          });
      event.preventDefault();
    });

    $('#thumbs-up').click(function(){
      $.ajax({
        data : {
          hfg2 : 'likeS'
        },
        type : 'POST',
        url : '/contact/like'
      })
      .done(function(data){
        if(data){
          alert("Your response has been recorded")
        }
      });
    });

    $('#thumbs-down').click(function(){
      $.ajax({
        data : {
          hfg2 : 'likeS'
        },
        type : 'POST',
        url : '/contact/dislike'
      })
      .done(function(data){
        if(data){
          alert("Your response has been recorded")
        }
      });
    });

  });