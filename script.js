function predict() {
    let data = {
        total: parseInt(document.getElementById("total").value),
        social: parseInt(document.getElementById("social").value),
        study: parseInt(document.getElementById("study").value),
        entertainment: parseInt(document.getElementById("entertainment").value),
        gaming: parseInt(document.getElementById("gaming").value)
    };

    fetch("/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data)
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("result").innerHTML = 
        `<b>User Status:</b> ${data.prediction}<br>
         <b>Most Used Category:</b> ${data.most_used}`;
    });
}
