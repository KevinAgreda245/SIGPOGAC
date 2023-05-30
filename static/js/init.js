function initTable(id,registros) {
    $(id).DataTable({
        "responsive": true,
        "language": {
            "decimal": "",
            "emptyTable": `No hay ${registros} registrados`,
            "info": `Mostrando _START_ a _END_ de _TOTAL_ ${registros}`,
            "infoEmpty": "Mostrando 0 a 0 de 0 "+registros,
            "infoFiltered": "(Filtrado de _MAX_ total " + registros +")",
            "infoPostFix": "",
            "thousands": ",",
            "lengthMenu": "Mostrar _MENU_ "+registros,
            "loadingRecords": "Cargando...",
            "processing": "Procesando...",
            "search": "Buscar:",
            "zeroRecords": "Sin resultados encontrados",
            "paginate": {
                "first": "Primero",
                "last": "Ultimo",
                "next": "Siguiente",
                "previous": "Anterior"
            }
        } 
    });
}