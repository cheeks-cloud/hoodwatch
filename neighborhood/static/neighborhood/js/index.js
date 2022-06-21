let avatar = document.querySelector(".toggle");
let username = document.querySelector(".normal");
let edit = document.querySelector(".hover");

avatar.addEventListener("mouseover", () => {
  username.style.display = "none";
  edit.style.display = "block";
});

avatar.addEventListener("mouseout", () => {
  edit.style.display = "none";
  username.style.display = "block";
});
