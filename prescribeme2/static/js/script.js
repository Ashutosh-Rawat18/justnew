let menu = document.querySelector('#menu-btn');
let navbar = document.querySelector('.header .nav');
let header = document.querySelector('.header');
menu.onclick = () => {
menu.classList.toggle('fa-times');
navbar.classList.toggle('active');
}
window.onscroll = () => {
menu.classList.remove('fa-times');
navbar.classList.remove('active');
if (window.scrollY > 0) {
header.classList.add('active');
} else {
header.classList.remove('active');
}
}
function validateemail() {
var x = document.myform.email.value;
var atposition = x.indexOf("@");
var dotposition = x.lastIndexOf(".");
if (atposition < 1 || dotposition < atposition + 2 || dotposition + 2 >= x.length)
{
alert("Please enter a valid e-mail address \n");
return false;
}
}