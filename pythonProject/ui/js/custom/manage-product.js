var productModal = $("#productModal");

$(function () {
    // Load product list
    $.get(productListApiUrl, function (response) {
        if (response) {
            var table = '';
            $.each(response, function (index, product) {
                table += '<tr data-id="' + product.product_id + '" data-name="' + product.name + '" data-unit="' + product.uom_id + '" data-price="' + product.price_per_unit + '">' +
                    '<td>' + product.name + '</td>' +
                    '<td>' + product.uom_name + '</td>' +
                    '<td>' + product.price_per_unit + '</td>' +
                    '<td><span class="btn btn-xs btn-danger delete-product">Delete</span></td>' +
                    '<td><span class="btn btn-xs btn-warning edit-product">Edit</span></td></tr>';
            });
            $("table").find('tbody').empty().html(table);
        }
    });

    // Save or Update Product
    $("#saveProduct").on("click", function () {
        var data = $("#productForm").serializeArray();
        var requestPayload = {
            product_id: $("#id").val(),
            product_name: null,
            uom_id: null,
            price_per_unit: null
        };

        for (var i = 0; i < data.length; ++i) {
            var element = data[i];
            switch (element.name) {
                case 'name':
                    requestPayload.product_name = element.value;
                    break;
                case 'uoms':
                    requestPayload.uom_id = element.value;
                    break;
                case 'price':
                    requestPayload.price_per_unit = element.value;
                    break;
            }
        }

        var apiUrl = requestPayload.product_id === "0" ? productSaveApiUrl : productUpdateApiUrl;
        callApi("POST", apiUrl, {
            'data': JSON.stringify(requestPayload)
        });
    });

    // Delete Product
    $(document).on("click", ".delete-product", function () {
        var tr = $(this).closest('tr');
        var data = {
            product_id: tr.data('id')
        };
        var isDelete = confirm("Are you sure to delete " + tr.data('name') + " item?");
        if (isDelete) {
            callApi("POST", productDeleteApiUrl, data);
        }
    });

    // Edit Product
    $(document).on("click", ".edit-product", function () {
        var tr = $(this).closest('tr');
        $("#id").val(tr.data('id'));
        $("#name").val(tr.data('name'));
        $("#uoms").val(tr.data('unit'));
        $("#price").val(tr.data('price'));
        productModal.find('.modal-title').text('Edit Product');
        productModal.modal('show');
    });

    productModal.on('hide.bs.modal', function () {
        $("#id").val('0');
        $("#name, #uoms, #price").val('');
        productModal.find('.modal-title').text('Add New Product');
    });

    productModal.on('show.bs.modal', function () {
        // Load UOM list
        $.get(uomListApiUrl, function (response) {
            if (response) {
                var options = '<option value="">--Select--</option>';
                $.each(response, function (index, uom) {
                    options += '<option value="' + uom.uom_id + '">' + uom.uom_name + '</option>';
                });
                $("#uoms").empty().html(options);
            }
        });
    });
});
