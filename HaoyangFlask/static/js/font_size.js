$(function(){
    function sizeIn(){
        var sizeCont = parseInt($(".newshow_cont").css("fontSize")); // 鑾峰彇鍘熻瀹氱殑font-size鐨勫€�
        if(sizeCont == 30){ // 鍒ゆ柇font-size澧炲ぇ鍒�30鍍忕礌鏃跺仠姝�
            $(".newshow_cont").css({fontSize:sizeCont});
        }else{
            $(".newshow_cont").css({fontSize:sizeCont + 2});
        }
    }
    function sizeOut(){
        var sizeCont = parseInt($(".newshow_cont").css("fontSize"));
        if(sizeCont == 12){ // 鍒ゆ柇font-size鍑忓皬鍒�10鍍忕礌鏃跺仠姝�
            $(".newshow_cont").css({fontSize:sizeCont});
        }else{
            $(".newshow_cont").css({fontSize:sizeCont - 2});
        }
    }
    function sizeDefault(){
        $(".newshow_cont").css({fontSize:""})
    }
    $(".newshow_ctrl a").click(function(){
        if($(this).index() == 0){
            sizeIn();
        }else if($(this).index() == 1){
            sizeOut();
        }else{
            sizeDefault();
        }

    })
});