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

document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.add-to-cart-form').forEach(form => {
        form.addEventListener('submit', function(event) {
            event.preventDefault();

            let formData = new FormData(this);
            fetch(this.action, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': getCookie('csrftoken')
                },
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                document.querySelector('#cart-items').innerHTML = data.cart_items_html;
                document.querySelector('.badge').innerText = data.cart_total_quantity;

                // Update the cart quantity in the navbar
                document.querySelector('#cart-button .badge').innerText = data.cart_total_quantity;

                // Update the product controls with - + buttons
                let productId = formData.get('product_id');
                let productControls = document.querySelector('#product-controls-' + productId);
                productControls.innerHTML = `
                    <div class="input-group">
                        <button class="btn btn-outline-secondary decrement-quantity" data-product-id="${productId}">-</button>
                        <input type="text" class="form-control quantity" value="1" readonly>
                        <button class="btn btn-outline-secondary increment-quantity" data-product-id="${productId}">+</button>
                        <a href="/cart/" class="btn btn-primary">В корзину</a>
                    </div>
                `;

                // Add event listeners for new buttons
                productControls.querySelector('.decrement-quantity').addEventListener('click', updateQuantity);
                productControls.querySelector('.increment-quantity').addEventListener('click', updateQuantity);
            });
        });
    });
});

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function updateQuantity(event) {
    let button = event.target;
    let productId = button.getAttribute('data-product-id');
    let quantityInput = button.closest('.input-group').querySelector('.quantity');
    let newQuantity = parseInt(quantityInput.value);

    if (button.classList.contains('decrement-quantity')) {
        newQuantity = Math.max(newQuantity - 1, 1);
    } else if (button.classList.contains('increment-quantity')) {
        newQuantity += 1;
    }

    quantityInput.value = newQuantity;

    // Here you can also add an AJAX call to update the quantity on the server if needed
}