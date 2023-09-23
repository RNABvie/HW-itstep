function myFunction() {
  let x = document.getElementById("passwordInput");
  let pic = document.getElementById('toggleButton');
  let arrow = document.getElementById('arrow');
  if (x.type === "password") {
    x.type = "text";
    pic.innerHTML = "&#216;";
    arrow.innerHTML = 'скрыть пароль';
  } else {
    x.type = "password";
    pic.innerHTML = "&#x1F441;";
    arrow.innerHTML = "показать пароль"
  }
};


function TextNewLine() {
    const text = document.querySelector('.JsTextnewline');
    if (text.innerText.length > 35) {
        const chunks = text.innerText.match(/.{1,35}/g);
        const formattedText = chunks.join('\n');
        text.innerText = formattedText + "...";

    }

};
