document.addEventListener("DOMContentLoaded", init);
const URL_API = "http://127.0.0.1:8000/api/";

let usuarios = [];

function init (){
    verUsuarios();
}

// funcion ver usuarios ********************************************
async function verUsuarios() {

    let url = URL_API + "usuarios/3";

    // hacer peticion
    let response = await fetch (url, {
        method: "GET",
        headers: { 
            "Content-Type": "application/json",
        },
    });

    usuarios = await response.json();

    let html = "";

    for (usuario of usuarios){
        let row = `<tr>
               
            <td>${usuario.id}</td>
            
            <td>${usuario.nombre}</td>
            <td>${usuario.apellido}</td>
            <td>${usuario.id_tipo}</td>
            <td>${usuario.numeroDocumento}</td>
            <td>${usuario.id_rol}</td>
            <td>${usuario.estado}</td>
            <td>${usuario.correo}</td>
            <td>${usuario.telefono}</td>
            <td>${usuario.ficha}</td>
            <td>${usuario.id_centro}</td>
            
            
        </tr>`;
        html = html + row;
    }
    document.querySelector("#Usuarios > tbody").outerHTML = html;
}




// moficar y crear usuarios**************************************************
async function guardarUsuario(){

    let data = {
        usuario: document.getElementById("txtUsuario").value,
        password: document.getElementById("txtPassword").value,
    };

    let id = document.getElementById("txtId").value;

    if (id != ""){
        data.id = id;
    }

    let url = URL_API + "usuarios";
    let response = await fetch (url, {
        method: "POST",
        body: JSON.stringify(data),
        headers:{
            "Content-Type": "application/json",
        },
    });

    let respuesta = await response.json();

    if (respuesta[0] == "True"){
        alert ("Usuario guardado exitosamente");
    }else{
        alert ("Hubo un error al guardar el usuario");
    }

    window.location.reload();
}

function editarUsuario(id){
    abrirFormulario();
    let usuario = usuarios.find((x) => x.id == id);
    document.getElementById("txtId").value = usuario.id;
    document.getElementById("txtUsuario").value = usuario.usuario;
    document.getElementById("txtPassword").value = usuario.password;
}

async function eliminarUsuario(id){
    let respuesta = confirm("¿Esta sefuro de eliminarlo?");

    if (respuesta){
        let url = URL_API + "usuarios/" + id;

        let response = await fetch(url, {
            method: "DELETE",
            headers: {
                "Content-Type": "application/json",
            }
        });

        let respuesta = await response.json();

        if (respuesta[0] == "True"){
            alert("Usuario eliminado exitosamente");
        }else{
            alert("Hubo un error");
        }
        window.location.reload();
    }
}















