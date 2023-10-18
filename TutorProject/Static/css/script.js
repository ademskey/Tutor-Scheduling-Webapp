document.querySelector('#closeSidebarBtn').addEventListener('click', function() {
    var sidebar = document.querySelector('#sidebar');
    var closeBtn = document.querySelector('#closeSidebarBtn');
    var openBtn = document.querySelector('#openSidebarBtn');
    var wrapper = document.querySelector(".wrapper");

    // Toggle the collapsed class on wrapper
    wrapper.classList.toggle("collapsed");

    // Toggle the closed class on sidebar
    sidebar.classList.toggle('closed');

    if (sidebar.classList.contains('closed')) {
        sidebar.style.width = '50px';  // Closed width
        closeBtn.style.display = 'none';  // Hide close button
        openBtn.style.display = 'block';  // Show menu button
    } else {
        sidebar.style.width = '250px';  // Opened width
        closeBtn.style.display = 'block';  // Show close button
        openBtn.style.display = 'none';  // Hide menu button
    }
});

// Event listener to open the sidebar when the menu button is clicked
document.querySelector('#openSidebarBtn').addEventListener('click', function() {
    var sidebar = document.querySelector('#sidebar');
    var closeBtn = document.querySelector('#closeSidebarBtn');
    var openBtn = document.querySelector('#openSidebarBtn');
    var wrapper = document.querySelector(".wrapper");

    wrapper.classList.remove("collapsed");
    sidebar.classList.remove('closed');
    sidebar.style.width = '250px';  // Opened width
    closeBtn.style.display = 'block';  // Show close button
    openBtn.style.display = 'none';  // Hide menu button
});
