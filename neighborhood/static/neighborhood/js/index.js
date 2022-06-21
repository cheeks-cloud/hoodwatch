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

let postDiv = document.querySelector("#post-form");
let closePost = document.querySelector(".close-post");
let postToggle = document.querySelector(".add-post");

let updateDiv = document.querySelector("#user-edit-form");
let closeUpdate = document.querySelector(".close-user-edit");

if (avatar) {
  avatar.addEventListener("mouseover", () => {
    username.style.display = "none";
    edit.style.display = "block";
  });

  avatar.addEventListener("mouseout", () => {
    edit.style.display = "none";
    username.style.display = "block";
  });

  avatar.addEventListener("click", () => {
    updateDiv.style.display = "flex";
  });
}

if (closeUpdate) {
  closeUpdate.addEventListener("click", () => {
    updateDiv.style.display = "none";
  });
}

if (businessToggle) {
  businessToggle.addEventListener("click", () => {
    businessDiv.style.display = "flex";
  });
}

if (closeBusiness) {
  closeBusiness.addEventListener("click", () => {
    businessDiv.style.display = "none";
  });
}

if (hoodToggle) {
  hoodToggle.addEventListener("click", () => {
    hoodDiv.style.display = "flex";
  });
}

if (closeHood) {
  closeHood.addEventListener("click", () => {
    hoodDiv.style.display = "none";
  });
}

if (closeMessages) {
  closeMessages.addEventListener("click", () => {
    messageDiv.style.display = "none";
  });
}

if (postToggle) {
  postToggle.addEventListener("click", (e) => {
    postDiv.style.display = "flex";
  });
}

if (closePost) {
  closePost.addEventListener("click", () => {
    postDiv.style.display = "none";
  });
}
