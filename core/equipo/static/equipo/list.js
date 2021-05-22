$(function () {
    $('#data').DataTable({
        responsive: true,
        autoWidth: false,
        destroy: true,
        deferRender: true,
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: {
                'action': 'searchdata'
            },
            dataSrc: ""
        },
        columns: [
            {"data": "codigo"},
            {"data": "id_auth_user.username"},
            {"data": "nombre"},
            {"data": "estandar"},
            {"data": "creada_en"},
            {"data": "actualizada_en"},
            {"data": "estado"},
            {"data": "id"},
        ],
        columnDefs: [
            
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var buttons = '<a href="/equipo/update/' + row.id + '/" class="btn btn-info btn-xs btn-flat"><i class="fas fa-edit"></i></a> ';
                    buttons += '<a href="/equipo/document/invoice/pdf/' + row.id + '/" target="_blank" class="btn btn-warning  btn-xs btn-flat"><i class="fas fa-file-pdf"></i> ';
                    return buttons;
                }
            },
        ], 
        initComplete: function (settings, json) {

        }
    });
});