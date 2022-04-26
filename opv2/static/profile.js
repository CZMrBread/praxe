var email = document.getElementById("floatingEmail");
var phone = document.getElementById("floatingTelephone");
var form = document.getElementById("profileForm");
var psc = document.getElementById("floatingPSC");
var last = "";

window.onload = function () {
    console.log("loaded")

    phone.value = phoneFormat(phone.value); 

    psc.addEventListener("keyup", function (e) {
        if (psc.value.length >= 3 && psc.value.search(" ") == -1) {
            var upstr = psc.value.split("");
            upstr.splice(3, 0, " ");
            upstr = upstr.join("");
            console.log(upstr);
            psc.value = upstr;
        }
        else if (psc.value.length == 4 && psc.value.search(" ")) {
            console.log("ok")
            psc.value = psc.value.replace(" ", "");
        }
    });

    email.addEventListener("keyup", function (e) {
        var re = /\S+@\S+\.\S+/;
        if (re.test(email.value)) {
            email.classList.remove("is-invalid");
            email.classList.add("is-valid");
        }
        else {
            email.classList.add("is-invalid");
            email.classList.remove("is-valid");
        }
    });

    phone.addEventListener("keyup", function (e) {
        phone.value = phoneFormat(phone.value);
        last = e.key;

        /*if(phone.value.replace(" ", "").slice(0,1) != "+" && phone.value.replace(" ", "").slice(0,2) != "00"){ //kontrola jestli je na začátku 00 nebo +
            phone.classList.remove("is-valid")
            phone.classList.add("is-invalid")
        }
        else{
            phone.classList.add("is-valid")
            phone.classList.remove("is-invalid")
        }*/

    });

    phone.addEventListener("keydown", function (e) {
        var re = /^\d+$/;
        if (e.key == "Backspace" || //povolená tlačítka v inputu
            e.key == "ArrowRight" ||
            e.key == "ArrowLeft" ||
            e.key == "+" ||
            e.key == "Shift" ||
            e.key == "Alt" ||
            e.key == "Tab") {
            last = e.key;
            return
        }

        if (e.getModifierState("Control")) {
            return
        }
        if (!re.test(e.key)) {
            e.preventDefault();
            last = e.key;
        }
    });

    form.addEventListener("submit", function (e) {
        phone.value = phone.value.split(" ").join("").replace("+", "");

        if(phone.value.slice(0, 2) == 00){
            phone.value = phone.value.substring(2); 
        }

        psc.value = psc.value.split(" ").join("");
    });

}

function checkInput() {
    if (pass2.value != pass1.value) {
        pass1.classList.remove("is-valid");
        pass2.classList.remove("is-valid");

        pass1.classList.add("is-invalid");
        pass2.classList.add("is-invalid");
    }

    else if (pass1.value == "" || pass2.value == "") {
        pass1.classList.remove("is-invalid");
        pass2.classList.remove("is-invalid");
        pass1.classList.remove("is-valid");
        pass2.classList.remove("is-valid");
    }

    else {
        pass1.classList.remove("is-invalid");
        pass2.classList.remove("is-invalid");

        pass1.classList.add("is-valid");
        pass2.classList.add("is-valid");
    }
}

function phoneFormat(input) {
    //console.log(last);
    input = input.split(' ').join('');
    var size = input.length;

    if(phone.value.replace(" ", "").slice(0, 1) == "+"){
        console.log(phone.value)

        phone.setAttribute("maxlength", 16);

        if (size > 3) { input = input.slice(0, 4) + " " + input.slice(4, 20) }
        if (size > 6) { input = input.slice(0, 8) + " " + input.slice(8, 20) }
        if (size > 9) { input = input.slice(0, 12) + " " + input.slice(12, 20) }

        if (input.slice(-1) == " " && last == "Backspace") {
            input = input.slice(0, input.length - 1);
        }
    }

    else if(phone.value.replace(" ", "").slice(0, 2) == "00"){
        phone.setAttribute("maxlength", 17);

        if (size > 4) { input = input.slice(0, 5) + " " + input.slice(5, 20) }
        if (size > 7) { input = input.slice(0, 9) + " " + input.slice(9, 20) }
        if (size > 10) { input = input.slice(0, 13) + " " + input.slice(13, 20) }

        if (input.slice(-1) == " " && last == "Backspace") {
            input = input.slice(0, input.length - 1);
        }
    }

    else if (phone.value.replace(" ", "").slice(0, 1) != "+" && phone.value.replace(" ", "").slice(0, 2) != "00") {
        phone.setAttribute("maxlength", 11);

        if (size > 2) { input = input.slice(0, 3) + " " + input.slice(3, 15) }
        if (size > 5) { input = input.slice(0, 7) + " " + input.slice(7, 15) }
        if (input.slice(-1) == " " && last == "Backspace") {
            input = input.slice(0, input.length - 1);
        }
    }
    return input;
}

