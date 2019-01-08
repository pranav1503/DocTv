function viewPass(){
  var pas = document.getElementById("passbox");
  if(pas.type === "password"){
    pas.type = "text";
  }else{
    pas.type = "password";
  }
}
