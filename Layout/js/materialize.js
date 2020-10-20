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
      opacity:0.9,
      inDuration: 600,
      outDuration:300,
    });

    
    var elems = document.querySelectorAll('select');
    var instances = M.FormSelect.init(elems);
});
