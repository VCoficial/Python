async function iniciarsesion(){
    let api = "http://127.0.0.1:3000/valLogin";
    
        let data = {
            usuario: document.getElementById("user").value,
            password: document.getElementById("pass").value,
        };
    
        let response = await fetch (api, {
            method: "POST",
            body: JSON.stringify(data),
            headers:{
                "Content-Type": "application/json",
            },
        });    
}

