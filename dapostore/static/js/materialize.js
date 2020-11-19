document.addEventListener('DOMContentLoaded', function() {
    // navbar
    var elems = document.querySelectorAll('.sidenav');
    var instances = M.Sidenav.init(elems);
    // parallax
    var elems = document.querySelectorAll('.parallax');
    var instances = M.Parallax.init(elems);

    // carousel
    var elems = document.querySelectorAll('.carousel');
    var instances = M.Carousel.init(elems,
        {

        });

    var elems = document.querySelectorAll('.scrollspy');
    var instances = M.ScrollSpy.init(elems);

    var elems = document.querySelectorAll('.collapsible');
    var instances = M.Collapsible.init(elems);

    var elems = document.querySelectorAll('.modal');
    var instances = M.Modal.init(elems, {
      opacity:0.5,
      inDuration: 100,
      outDuration:100,
    });


    var elems = document.querySelectorAll('select');
    var instances = M.FormSelect.init(elems);

    var elems = document.querySelectorAll('.dropdown-trigger');
    var instances = M.Dropdown.init(elems, {});

    var elems = document.querySelectorAll('.fixed-action-btn');
    var instances = M.FloatingActionButton.init(elems, {});
});


div = document.getElementById('flotante');
var x = document.getElementById("myDIV");

window.addEventListener('load', function(event){
  x.style.display = 'none';
});

function myFunction(){

    if(x.style.display == "none"){
      x.style.display = "block";
    }else{
      x.style.display = "none";
    }
}


const btnToggle = document.querySelector('.toggle-btn');
btnToggle.addEventListener('click', function(event){
    document.getElementById('sidebar').classList.toggle('active');
});
