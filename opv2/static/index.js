function onLoadHandler() {
  console.log("Loaded");
  document.getElementById("floatingPassword").addEventListener("keydown", function (e) {
    if (e.key === "Enter") {
      sendLogin();
    }
  });

  document.getElementById("floatingEmail").addEventListener("keydown", function (e) {
    if (e.key === "Enter") {
      sendLogin();
    }
  });
}


/*function sendLogin() {
  var email = document.getElementById("floatingEmail").value;
  var password = document.getElementById("floatingPassword").value;

  login = {}
  login.email = email;
  login.password = password;

  const xhr = new XMLHttpRequest();
  xhr.open("POST", "ok");
  xhr.send();
  xhr.onload = function () {
    if (xhr.status === 200) {

      data = JSON.parse(xhr.responseText);
      console.log(data.status);
      if (data.status === "ok") {
        document.getElementById("floatingPassword").classList.remove("is-invalid");
        document.getElementById("floatingEmail").classList.remove("is-invalid");

        document.getElementById("floatingPassword").classList.add("is-valid");
        document.getElementById("floatingEmail").classList.add("is-valid");
        //setTimeout(function () {window.location.href = `${window.location.href}home`;}, 2000);
        window.location.href = `${window.location.href}home`;
      }

      else if (data.status === "not_found") {
        document.getElementById("floatingEmail").classList.add("is-invalid");
        document.getElementById("floatingPassword").classList.remove("is-invalid")
      }

      else if (data.status === "wrong_pass") {
        document.getElementById("floatingPassword").classList.add("is-invalid");
        document.getElementById("floatingEmail").classList.remove("is-invalid");

      }
      //console.log(xhr.responseText);

    } else if (xhr.status === 404) {
      console.log("No records found");
    }
  }

}*/