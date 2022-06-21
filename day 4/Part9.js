var firstName = prompt("First Name: ")
var lastName = prompt("Last Name: ")
var age = prompt("How old are you? ")
var heigth = prompt("How tall are you? ")
var petName = prompt("What is your pet's name? ")
alert("Thank you so much for the information!!")

// Logic and Conditions

var nameCond = null;
var ageCond = null;
var heightCond = null;
var petCond = null;


// Name Conditon
if (firstName[0] === lastName[0]) {
  nameCond = true;
}else {
  nameCond = false;
}

// Age
if (age > 20 && age < 30){
  ageCond = true;
}else {
  ageCond = false;
}

// Height
if (height >= 170){
  heightCond = true;
}else {
  heightCond = false;
}

// pet

if(petName[petName.length-1] ==="y"){
  petcond = false;
}

// all conditions check
if (nameCond && ageCond && heightCond && petCond){
  console.log("WELCOME HERETIC!!!");
}else{
  console.log("The Inquisition says there is nothing here ")
}