/* jshint esversion: 6 */

$(function() {
    function bindCaptchaBtnClick(){
        $("#captcha-btn").click(function(event) {
        let $this = $(this);
        let email = $("input[name=email]").val(); // 使用 val() 方法获取输入框的值
        if (!email) {
            alert("请先输入邮箱！");
            return;
        }
        $this.off('click');
        $.ajax("/register/captcha/?email="+email,{
            method:"GET";
            success:function (result){
               if(result['code']==200){
                   alert("验证码发送成功!");
               }
               else{
                   alert(result['message']);
               }
            }
            fail: function (error){
                console.log(error);
            }
        })

        let countdown=6;
        let timer = setInterval(function (){
            if(countdown<=0){
                $this.text("获取验证码");
                clearInterval(timer);
                bindCaptchaBtnClick();
            }
            else{
                countdown--;
                $this.text(countdown+"s");
            }
        }, 1000);
    });
    }
    bindCaptchaBtnClick();
});