$(document).ready(function(){

  $("#formularioRegistro").submit(function(e){
    alert('success');
    console.log("Enviando Form");
    e.preventDefault();

  });

});