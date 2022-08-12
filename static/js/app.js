$(document).on('submit', '#convert-form', function (e) {
    const myDiv = document.getElementById('success')

    let myHeaders = new Headers();
    myHeaders.append("apikey", key);

    let requestOptions = {
        method: 'GET',
        redirect: 'follow',
        headers: myHeaders
    };

    fetch("https://api.apilayer.com/exchangerates_data/convert?to="+$("#to").val()+"&from="+$("#from").val()+"&amount="+$("#amount").val()+"", requestOptions)
        .then(response => response.json())
        .then(result => myDiv.innerHTML = Math.round((result.result + Number.EPSILON) * 100) / 100)
        .catch(error => console.log('error', error));

    e.preventDefault();
    $.ajax({
        type: 'POST',
        url: '/',
        data: {
            "user_name": $("#to").val(),
            "user_email": $("#from").val(),
            "user_subject": $("#amount").val()
        },
        success: function () {
            document.getElementById('success').style.visibility = 'visible';
        },
    })
});