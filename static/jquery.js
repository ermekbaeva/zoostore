// to show tab "order history" in profile
jQuery(function () {
    $('#profileTab a').on('click', function (e) {
        e.preventDefault();
        $(this).tab('show');
    });
});

// to remove alert "successful login, logout, etc." after 4 seconds
jQuery(function() {
    setTimeout(function() {
        var $alertElement = $('#alert-message');
        if ($alertElement.length) {
            $alertElement.removeClass('show').addClass('fade');
            setTimeout(function() {
                if ($alertElement.length) {
                    $alertElement.remove();
                }
            }, 150); // Delay to allow fade out
        }
    }, 4000); // 4 seconds
});

//to Switch to edit mode after clicking the 'Edit Profile' button  
jQuery(function(){
    $('#edit-profile').click(function(){
        $('.profile-info').hide();
        $('.edit-form').show();
    });
    $('#edit-password').click(function(){
        $('.profile-info').hide();
        $('.edit-password-form').show();
    });
    $('#cancel-edit').click(function(){
        $('.edit-form').hide();
        $('.profile-info').show();
    });
    $('#cancel-edit-password').click(function(){
        $('.edit-password-form').hide();
        $('.profile-info').show();
    });
});

//add item to cart
document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.add-to-cart').forEach(function(button) {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            var productId = this.dataset.productId;
            var addToCartUrl = this.getAttribute('href');
            fetch(addToCartUrl, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'X-CSRFToken': '{{ csrf_token }}'
                },
                body: new URLSearchParams({ product_id: productId })
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    showAlert(data.message, 'success');
                    document.getElementById('cart-counter').textContent = data.total_items;
                } else {
                    showAlert('Item was not added to cart', 'danger');
                }
            })
            .catch(error => {
                console.error('Error:', error);
            });
        });
    });
});

//delete item from cart
document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.remove-from-cart').forEach(function(button) {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            var cartId = this.dataset.cartId;
            var removeFromCartUrl = this.getAttribute('href');
            fetch(removeFromCartUrl, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'X-CSRFToken': '{{ csrf_token }}'
                },
                body: new URLSearchParams({ cart_id: cartId })
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    showAlert(data.message, 'success');
                    document.getElementById('cart-counter').textContent = data.total_items;
                    document.getElementById('total-price').textContent = data.total_price;
                    var cartItemElement = document.querySelector(`[data-cart-id="${cartId}"]`).closest('.cart-item');
                    if (cartItemElement) {
                        cartItemElement.remove();
                    }
                } else {
                    showAlert('Item was not deleted from cart', 'danger');
                }
            })
            .catch(error => {
                console.error('Error:', error);
            });
        });
    });
});

//show alert when you add or delete items in cart
function showAlert(message, type) {
    var alertContainer = document.getElementById('alert-container');
    var alertDiv = document.createElement('div');
    alertDiv.className = `alert alert-${type === 'success' ? 'success' : 'danger'} alert-dismissible fade show`;
    alertDiv.setAttribute('role', 'alert');
    alertDiv.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
    `;

    alertContainer.appendChild(alertDiv);

    setTimeout(function() {
        alertDiv.classList.remove('show');
        alertDiv.classList.add('fade');
        setTimeout(function() {
            alertContainer.removeChild(alertDiv);
        }, 500);
    }, 2000);
}

//change quantity of items in cart after press "-" and "+" buttons
document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.btn-decrease, .btn-increase').forEach(function(button) {
        button.addEventListener('click', function(e) {
            e.preventDefault();

            var isDecrease = this.classList.contains('btn-decrease');
            var form = this.closest('form');
            var input = form.querySelector('.product-quantity');
            var currentQuantity = parseInt(input.value);
            var newQuantity = isDecrease ? currentQuantity - 1 : currentQuantity + 1;

            if (isDecrease && currentQuantity === 1) {
                // If the quantity is 1 and the decrease button is clicked, do nothing
                return;
            }

            input.value = newQuantity;

            var formData = new FormData(form);
            formData.set('quantity', newQuantity);

            fetch(form.action, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': formData.get('csrfmiddlewaretoken')
                },
                body: new URLSearchParams(formData)
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    showAlert(data.message, 'success');
                    document.getElementById('cart-counter').textContent = data.total_items;
                    document.getElementById('total-price').textContent = data.total_price;
                    
                    var productPriceElement = document.querySelector(`#products-price-${formData.get('cart_id')}`);
                    if (productPriceElement) {
                        productPriceElement.textContent = data.products_price;
                    }
                    
                } else {
                    showAlert('Quantity was not changed', 'danger');
                }
            })
            .catch(error => {
                console.error('Error:', error);
            });
        });
    });
});