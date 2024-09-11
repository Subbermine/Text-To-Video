var slider = document.getElementById("myRange");
var output = document.getElementById("sliderVal");
output.innerHTML = slider.value;

slider.oninput = function () {
  output.innerHTML = this.value;
};

var count = 0;
function myFunc() {
  document.getElementById("loader").setAttribute("style", "display:block;");
  document.getElementById("vid").setAttribute("src", "spm.mp4");
  setTimeout(function () {
    document.getElementById("loader").setAttribute("style", "display:none;");
    document.getElementById("output").setAttribute("style", "display:block");
  }, 2000);
  count = 1;
}
document.getElementById("goButton").addEventListener("click", myFunc());
if (count === 1) {
  myFunc();
}
