window.onload = init;

// Function called when page loaded
function init(){
    generateFooter();
}

// Appends current year to the page footer of copyright
function generateFooter(){
    var copyrightParagraph = document.getElementById("copyright");
    var currentYear = document.createTextNode(new Date().getFullYear());
    copyrightParagraph.appendChild(currentYear);
}