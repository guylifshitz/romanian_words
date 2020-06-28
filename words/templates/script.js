
(function() {
    document.onmousedown = handleMouseDown;
    function handleMouseDown(event){
        window.location.reload();
    }

    document.onmousemove = handleMouseMove;
    function handleMouseMove(event) {
        var eventDoc, doc, body;

        event = event || window.event; // IE-ism

        // If pageX/Y aren't available and clientX/Y are,
        // calculate pageX/Y - logic taken from jQuery.
        // (This is to support old IE)
        if (event.pageX == null && event.clientX != null) {
            eventDoc = (event.target && event.target.ownerDocument) || document;
            doc = eventDoc.documentElement;
            body = eventDoc.body;

            event.pageX = event.clientX +
              (doc && doc.scrollLeft || body && body.scrollLeft || 0) -
              (doc && doc.clientLeft || body && body.clientLeft || 0);
            event.pageY = event.clientY +
              (doc && doc.scrollTop  || body && body.scrollTop  || 0) -
              (doc && doc.clientTop  || body && body.clientTop  || 0 );
        }

        // Use event.pageX / event.pageY here
        if (event.pageX > 700){
            $("#romanian").hide();
        }
        else{
            $("#romanian").show();
        }

        if (event.pageX < 500){
            $("#english").hide();
        }
        else{
            $("#english").show();
        }
    }
})();

document.onkeydown = checkKey;
function checkKey(e) {

    e = e || window.event;
    if (e.keyCode == '38') {
        window.location.href = "{{pk}}/increase_score";
    }
    else if (e.keyCode == '40') {
        window.location.href = "{{pk}}/decrease_score";
    }
    else if (e.keyCode == '37') {
       // left arrow
    }
    else if (e.keyCode == '39') {
       // right arrow
    }

}