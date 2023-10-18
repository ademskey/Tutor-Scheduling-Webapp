document.querySelector('#closeSidebarBtn').addEventListener('click', function() {
    var sidebar = document.querySelector('#sidebar');
    if (sidebar.classList.contains('closed')) {
        sidebar.style.width = '250px';
        sidebar.classList.remove('closed');
    } else {
        sidebar.style.width = '50px';  // This value can be adjusted for desired closed width
        sidebar.classList.add('closed');
    }
});

document.getElementById("closeSidebarBtn").addEventListener("click", function() {
    var wrapper = document.querySelector(".wrapper");
    wrapper.classList.toggle("collapsed");
});