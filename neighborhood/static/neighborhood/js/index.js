let avatar = document.querySelector(".toggle");
let username = document.querySelector(".normal");
let edit = document.querySelector(".hover");

let businessToggle = document.querySelector(".add-business");
let businessDiv = document.querySelector("#business-form");
let closeBusiness = document.querySelector(".close-business");

let hoodToggle = document.querySelector(".add-hood");
let hoodDiv = document.querySelector("#hood-form");
let closeHood = document.querySelector(".close-hood");

let messageDiv = document.querySelector("#system-messages");
let closeMessages = document.querySelector(".close-messages");

avatar.addEventListener("mouseover", () => {
  username.style.display = "none";
  edit.style.display = "block";
});

avatar.addEventListener("mouseout", () => {
  edit.style.display = "none";
  username.style.display = "block";
});

businessToggle.addEventListener("click", () => {
  businessDiv.style.display = "flex";
});

closeBusiness.addEventListener("click", () => {
  businessDiv.style.display = "none";
});

hoodToggle.addEventListener("click", () => {
  hoodDiv.style.display = "flex";
});

closeHood.addEventListener("click", () => {
  hoodDiv.style.display = "none";
});

closeMessages.addEventListener("click", () => {
  messageDiv.style.display = "none";
});
