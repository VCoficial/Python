document.addEventListener("DOMContentLoaded", init);
const URL_API = "http://127.0.0.1:3000/api/";

let usuarios = [];

function init (){
    verUsuarios();
}

// funcion ver usuarios ********************************************
async function verUsuarios() {

    let url = URL_API + "usuarios";

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
            <td>${usuario.usuario}</td>
            <td>${usuario.password}</td>
            <td>
                <a href="#" class="myButton" onclick = "editarUsuario(${usuario.id})"> 
                    Editar
                </a>
                <a href="#" class="btnDelete" onclick = "eliminarUsuario(${usuario.id})"> 
                    Eliminar
                </a>
            </td>
        </tr>`;
        html = html + row;
    }
    document.querySelector("#usuarios > tbody").outerHTML = html;
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















