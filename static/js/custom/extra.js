$(document).ready(function () {
    // Mesaj çubuğunu belirli bir süre sonra kaybolma efektiyle gizle
    setTimeout(function () {
        $('#message-bar').fadeOut(500); // 500 milisaniye içinde kaybolma efektiyle gizlenir
    }, 1000); // 3000 milisaniye (3 saniye) sonra kaybolur
});

CKEDITOR.replace( 'editor' );

