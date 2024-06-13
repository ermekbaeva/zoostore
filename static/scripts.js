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