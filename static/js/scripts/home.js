

/*
$(function(){

    $("#send_button").click(function(){
        $("#myModal").modal("hide");
    });

    $("#myModal").on("hidden.bs.modal", function(){
        alert("OK");
    });
});
*/
function close_this_shit(){
    $("#modal_alert").modal("hide");
}
function myFunction() {
    setTimeout(function(){
        $("#modal_alert").modal("show");
    }, 500);
    $("#myModal").modal("hide");

}