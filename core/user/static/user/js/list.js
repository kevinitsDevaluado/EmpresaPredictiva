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
            {"data": "id"},
            {"data": "full_name"},
            {"data": "username"},
            {"data": "date_joined"},
            {"data": "estado"},
            {"data": "groups"},
            {"data": "id"},
        ],
        columnDefs: [
            {
                targets: [-3],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    if(data==1){
                        return '<span class="badge badge-success">ACTIVO</span>'
                    }
                    return '<span class="badge badge-danger">INACTIVO</span>'
                }
            },
            {
                targets: [-2],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var html = '';
                    $.each(row.groups, function (key, value) {
                        html += '<span class="badge badge-success">' + value.name + '</span> ';
                    });
                    return html;
                }
            },
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var buttons = '<a href="/user/update/' + row.id + '/" class="btn btn-warning btn-xs btn-flat "><i class="fas fa-edit"></i></a> ';
                    buttons += '<a href="/user/activar2/' + row.id + '/" class="btn btn-success btn-xs btn-flat"><i class="fa fa-check" aria-hidden="true"></i></a> ';
                    buttons += '<a href="/user/desactivar2/' + row.id + '/" class="btn btn-danger  btn-xs btn-flat"><i class="fa fa-times" aria-hidden="true"></i> ';
                    return buttons;
                }
            },
        ],
        initComplete: function (settings, json) {

        }
    });
});