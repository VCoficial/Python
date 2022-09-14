document.addEventListener("DOMContentLoaded", init);
const URL_API = "http://127.0.0.1:8000/api/";

let equipos = [];

function init (){
    verEquipos();
}
/* EQUIPOS ********************************************/

async function verEquipos(){
    let url = URL_API + "equipos";
    
    //hacer peticion
    let response = await fetch(url, {
        method: "GET",
        headers: {
            "Content-Type": "application/json",
        },
    });

    usuarios = await response.json();

    let html = "";
    let contenido;

    for (equipos of equipos){
        let row = `<tr>
            <td>${equipos.serie}</td>
            <td>${equipos.id_Marca}</td>
            <td>${equipos.detalle}</td>
            <td>${equipos.id_Usuario}</td>
            <td>${equipos.estado}</td>
            <td>${equipos.img}</td>
            <td>
                <a class="btn btn-primary" href="#" role="button" onclick= "editarEquipo(${equipos.serie})">Editar</a>
                <a class="btn btn-primary" href="#" role="button" onclick= "eliminarEquipo(${equipos.serie})">Eliminar</a>
            </td>
        </tr>`;
        html = html + row;
    }
    document.querySelector("#equipos > tbody").outerHTML = html;
    document.querySelector("equipos > div").outerHTML = html;
}



/* addLi();

function addLi() {
    var contenido;
    for (i = 0; i < pelis.length; i++) {
      var li = document.createElement("li");
      var p = document.createElement("p");
      contenido = "Nombre:" + pelis[i].Nombre + " || Genero: " + pelis[i].Genero;
      p.appendChild(document.createTextNode(contenido));
      document.querySelector("#lista-pelis").appendChild(li).appendChild(p);
    }
} */