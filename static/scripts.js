// to show tab "order history" in profile
document.addEventListener('DOMContentLoaded', function () {
    var tabs = document.querySelectorAll('#profileTab a');
    tabs.forEach(function(tab) {
        tab.addEventListener('click', function(e) {
            e.preventDefault();
            var tabContent = new bootstrap.Tab(tab);
            tabContent.show();
        });
    });
});

// to remove alert "successful login, logout, etc." after 4 seconds
document.addEventListener('DOMContentLoaded', function() {
    setTimeout(function() {
        var alertElement = document.getElementById('alert-message');
        if (alertElement) {
            alertElement.classList.remove('show');
            alertElement.classList.add('fade');
            setTimeout(function() {
                if (alertElement && alertElement.parentNode) {
                    alertElement.parentNode.removeChild(alertElement);
                }
            }, 150); // Delay to allow fade out
        }
    }, 4000); // 4 seconds
});