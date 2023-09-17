function myFunction() {
  let x = document.getElementById("passwordInput");
  let pic = document.getElementById('toggleButton');
  let arrow = document.getElementById('arrow');
  if (x.type === "password") {
    x.type = "text";
    pic.innerHTML = "&#216;";
    arrow.innerHTML = 'скрыть пароль&#8595';
  } else {
    x.type = "password";
    pic.innerHTML = "&#x1F441;";
    arrow.innerHTML = "показать пароль&#8593;"
  }
}