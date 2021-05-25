function startJS(){
    $(function () {
        $(document).ready(function () {
            $('.sidenav').sidenav();
        });
        $(".js-cerrar-modal").click(function () {
            $(".modal").hide()
            console.log("click")
        });
    });
}
window.onload=startJS();