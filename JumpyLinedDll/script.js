var myButton= document.getElementById("button");

var myParagraph = document.getElementById("id");

myButton.addEventListener("click", pizza);

function pizza() {
  myParagraph.innerHTML = "YOu clicked tghe buttrn";
}