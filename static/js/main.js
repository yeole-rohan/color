var $ = jQuery.noConflict();

$(document).ready(function(){
    $('#paths').on("click", function() {
        if($(this).hasClass('paths')){
            $('#path').css({ fill: "#0000003b" });
            $(this).removeClass('paths')
        }else{
            $('#path').css({ fill: "#EF465A" });
            $(this).addClass('paths')
        }
    });
    $('.add-cart').on('click', function(params){
        params.preventDefault();
        $.ajax({
            url: $(this).attr('href'),
            data:{
                'id': $(this).attr('data-id'),
                'csrfmiddlewaretoken' : $('input[type=hidden]').val(),
            },
            type:'POST',
            dataType: 'json',
            success: function (res, status) {
                if (res['status'] == 'ok') {
                    $(this).html('added to cart');
                    // var previous_action = $('.like').eq(index).attr('action');
                    // $('.like').eq(index).attr('action', previous_action == 'like' ? 'liked' : 'like');
                    // // var under = $(this).parent('.more').siblings('.like-count')
                    // var under = $(this).closest('.more').children('.like-count')
                    // var like_num = $('.like-num').index(this)
                    // console.log(under)
                    // // toggle link text
                    // if (previous_action == 'like') {
                    //     $('.like').eq(index).removeClass('likes')
                    //     $('.like').eq(index).addClass('unlike')
                    //     $('.like').eq(index).find('svg').css('display', 'none')
                    // }
                    // if (previous_action == 'liked') {
                    //     $('.like').eq(index).removeClass('unlike')
                    //     $('.like').eq(index).addClass('likes')
                    //     $('.like').eq(index).find('svg').css('display', 'none')
                    // }
                }
            },
            error: function (res) {
                console.log(res.status);
            }
        })
    });
}( jQuery ) );