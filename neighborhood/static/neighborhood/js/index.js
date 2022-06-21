let avatar = document.querySelector(".toggle");
let username = document.querySelector(".normal");
let edit = document.querySelector(".hover");
let businessToggle = document.querySelector(".add-business");
let businessDiv = document.querySelector("#business-form");
let closeBusiness = document.querySelector(".close-business");

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
