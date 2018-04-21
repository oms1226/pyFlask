$(document).ready(function(){
    //alert("load");
    //sumit 이벤트 인터셉트 --> page 이동하지 않도록 막는다.
    $('form').on('submit', function(evt){
        //클릭 이벤트 외에 별도의 브라우저 행동을 막기 위해 사용됩니다.
        evt.preventDefault();

        //해당 로그는 webbrower 로그이벤트에 찍힌다
        //console.log("전송 이벤트");

        //Jquery가 Ajax를 wrapping하고 있으며, $.post 라는 것이 post를 특화한 것이다. 
        $.post({
            url:'/search',
            data:$('form').serialize(),
            dataType:'json',
            success:function( data ){
                console.log("성공", data);
                parseResultShow( data );
            },
            error:function( err ){
                console.log("실패", err);
            }
        });
        return false;
    });
});
function parseResultShow( data ) 
{
    // 키워드 획득
    var keyword = $('input[name=keyword]').val();
    // 기존 결과 삭제
    $('#result').empty();
    // 결과를 반복
    $.each(data, function(index, item){
        console.log( "each", index, item );
        var html = "<li>" + item.name.replace(keyword, "<b>" + keyword + "</b>") + "</li>"
        $('#result').append(html);
        $('#result>li:last').on('click', function(evt){//append된 결과에 click이벤트를 붙힌다.
            alert(item.name + " 클릭 ");
        });
    });

}