let url = "http://127.0.0.1:3000/"

function cerrarSesion(){
    
    let cerrarSesion = url + "cerrarSesion"
    if (confirm("¿Esta seguro de Cerrar Sesion?")){
        window.location.replace(cerrarSesion);
    }
}