$('#ask').click(function(){

    var query=$('#query').val();
    $('#chat').show()
    console.log(query);
    var code1='<div class="chatboxu"> </h3>';
    var code2=' &nbsp;&nbsp; <h3 class="fas fa-user" style="color: chocolate;"></div>';
    var prev=$('#chbox').html();
    $('#chbox').html(prev+code1+query+code2);
    var bot='<div class="chatboxr"> <h3 class="fas fa-robot" style="color: chocolate;"></h3> &nbsp; .  .  . </div>';
    var prev2=$('#chbox').html();
    $('#chbox').html(prev2+bot);


});


