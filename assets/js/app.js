// hide after 2 sec
$(function() {
  setTimeout(function() { 
      $("#hideDiv").fadeOut(1500); 
  }, 2000)
});

// show hide password
function showHidePassword() {
  var x = document.getElementById("showPassword");
  var eye1 = document.getElementById("eye1");
  var eye2 = document.getElementById("eye2");

  if (x.type === "password") {
    x.type = "text";
    eye1.style.display = "none";
    eye2.style.display = "block";
  } else {
    x.type = "password";
    eye1.style.display = "block";
    eye2.style.display = "none";
  }
}

// clipboard copy
var clipboard = new ClipboardJS('.copy');
        
clipboard.on('success', function(e) {
console.log(e);
});

clipboard.on('error', function(e) {
console.log(e);
});