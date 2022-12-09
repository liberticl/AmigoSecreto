import { login, logout } from "./auth.js";
import { getSecretFriend } from "./firestore.js";
import { oneword } from "./utils.js";

let currentUser;
let data;

const buttonLogin = document.getElementById("button-login");
const buttonLogout = document.getElementById("button-logout");
const userInfo = document.getElementById("user-info");
const secretFriend = document.getElementById("result");
const body = document.getElementById("container")
const start = document.getElementById("start")

firebase.auth().onAuthStateChanged((user) => {
  if (user) {
    // User is signed in, see docs for a list of available properties
    // https://firebase.google.com/docs/reference/js/firebase.User
    var uid = user.uid;
    currentUser = user;
    init();
  } else {
  }
});



buttonLogin.addEventListener("click", async (e) => {
  try {
    currentUser = await login();
    init();
  } catch (error) {
    console.error(error);
  }
});

buttonLogout.addEventListener("click", (e) => {
  logout();
  buttonLogin.classList.remove("hidden");
  buttonLogout.classList.add("hidden");
  body.classList.add("hidden")
  start.classList.remove("hidden")
  userInfo.innerHTML = '';
  secretFriend.innerHTML = ''
});

async function init() {
  buttonLogin.classList.add("hidden");
  buttonLogout.classList.remove("hidden");
  body.classList.remove("hidden");
  start.classList.add("hidden");

  const thisSecretFriend = () => getSecretFriend(currentUser.email).then((a) => {
    return a;
  });
  data = await thisSecretFriend();

  userInfo.innerHTML = `
    <h1>Hola ${oneword(currentUser.displayName)}!</h1>
  `;
  
  secretFriend.innerHTML = `
    <h4>TU AMIGO SECRETO ES:<br></h4>
    <h2><strong>${data}</strong></h2>
  `;
}


//logout()