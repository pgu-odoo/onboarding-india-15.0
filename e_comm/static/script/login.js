function check(form) {
    if (form.userid.value == "a" && form.pswrd.value == "a") {
        window.open('/homepage', '_self')
    } else {
        alert("Error Password or Username")
    }
}
