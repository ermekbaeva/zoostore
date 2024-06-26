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

