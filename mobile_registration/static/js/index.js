class Base{
    template=``

    async render(){
        var parse=new DOMParser();
        let elm = document.getElementsByClassName("card-text");
        var tmpl=parse.parseFromString(this.template,"text/html").body.childNodes;
        elm[0].append(tmpl[0])
    }
}

class Register extends Base{
    template=`
        <div id="div_frmlogin" name="div_frmlogin" style="display:'';">
            <h3 class="card-title text-center">Register</h3>
            <form name="frmlogin" id="frmlogin" method="POST" action="/">
                <div class="form-group">
                    <label for="Number">Mobile Number</label>
                    &#9990<input type="tel"  class="form-control form-control-sm" id="mobile" name="mobile" required="true" maxlength="10" minlength="10">
                </div>                                               
                <button type="submit" id="sign_in" class="btn btn-primary btn-block">Sign in</button>
                <br></br>
                <div id="reg_m">
                    <strong><small><b>ALREADY REGISTERD ?</b></small></small></strong>
                    <button type="button" class="btn btn-primary btn-block w-50" id="lgn_btn" >Login</button>
                </div>
            </form>
        </div>
    `
    
    async render(){
        await super.render();
        document.getElementById("sign_in").addEventListener('click',(e)=>{this.sendMessage()});
        document.getElementById("lgn_btn").onclick=function(){
            document.getElementById("div_frmlogin").style.display='none';
            let lgn = new Login()
            lgn.render();
        }
    }

    sendMessage(){
        let mobile = document.getElementById("mobile").value;
        var act_otp = Math.floor(1000 + Math.random() * 9000);
        localStorage.setItem("mobile",mobile);
        localStorage.setItem("act_otp",act_otp);
        console.log(act_otp)
        const data = {
          method: 'POST',
          body: JSON.stringify({'mobile':mobile,'act_otp':act_otp}),
          headers: {'Content-Type':'application/json'}
        };

        fetch('/sendOTP',data)
        .then((response)=>{
            return response.json();
        })
        .then((jsondata)=>{
            if(jsondata['is_registerd']){
                let msg = '<div class="alert alert-success"><strong>&#128519 Mobile Already Registered</strong></div>'
                document.getElementById("div_msg").style.display='';
                document.getElementById("div_msg").innerHTML=msg;   

            }
            else{
                let ver = new Verify()
                ver.render()
                setTimeout(function () {
                    alert('Session Time Out');
                    location.reload();
                }, 50000);
            }
        })
        .catch((err)=>{
            alert(err)
        });
        document.getElementById("div_frmlogin").style.display='none';
        event.preventDefault();
    }    
}

class Verify extends Base{
    template=`
        <div id="div_frmverify" style="display:'';">
            <h3 class="card-title text-center">Verify</h3>
            <form name="frmverify" id="frmverify" method="post" action="" >
                <div class="form-group">
                        <label for="Otp">Please enter you OTP</label>
                        <input type="tel" class="form-control form-control-sm" id="verify_otp" name="verify_otp"  required="true" minlength="4" maxlength="4">
                </div>
                    <button type="submit" id="btn_sbmt" name="submit" class="btn btn-primary btn-block"  >Verify</button>
            </form>
        </div>
    `
    async render(){
        await super.render();
        document.getElementById("btn_sbmt").addEventListener('click',(e)=>{this.verifyOTP()});
    }

    verifyOTP(){
        let otp = document.getElementById("verify_otp").value;
        var mobile = localStorage.getItem("mobile")
        var act_otp=localStorage.getItem("act_otp")
        let dict = {'mobile':mobile,'act_otp':act_otp,'otp':otp}

        const data = {
          method: 'POST',
          body: JSON.stringify(dict),
          headers: {'Content-Type':'application/json'}
        };

        fetch('/verifyOTP',data)
        .then((response)=>{
            return response.json();
        })
        .then((jsondata)=>{
            var msg = '<div class="alert alert-danger"><strong>Please check your OTP &#128533</strong></div>'
            if(jsondata['is_registerd']){
                msg = '<div class="alert alert-success"><strong>&#9989; Mobile Register Successfully</strong></div>'
            }
            
            document.getElementById('div_frmverify').style.display = 'none';
            document.getElementById("div_msg").style.display=''; 
            document.getElementById("div_msg").innerHTML=msg;
        })
        .catch((err)=>{
            alert(err)
        });
       event.preventDefault();
    }
        
}

class Login extends Base{
    template=`
       <div id="div_login" name="div_login" style="display:'';">
            <h3 class="card-title text-center">Login</h3>
            <form name="loginfrm" id="loginfrm" method="POST" action="">
                <div class="form-group">
                    <label for="Number">Mobile Number</label>
                    <input type="tel"  class="form-control form-control-sm" id="lgn_mobile" name="lgn_mobile" required="true" maxlength="10" minlength="10">
                </div>                                               
                <button type="submit" id="log_in" class="btn btn-primary btn-block">Login</button>
            </form>
        </div>
    `
    async render(){
        await super.render();
        document.getElementById("log_in").addEventListener('click',(e)=>{this.validMobile()});
    }

    validMobile(){
       let mobile = document.getElementById("lgn_mobile").value;

        const data = {
          method: 'POST',
          body: JSON.stringify({'mobile':mobile}),
          headers: {'Content-Type':'application/json'}
        };

        fetch('/login',data)
        .then((response)=>{
            return response.json();
        })
        .then((jsondata)=>{
            var msg = `<div class="alert alert-danger"><strong>&#10060 Yout Mobile is not registerd</strong></br>
                <button type="button" class="btn btn-primary btn-block w-50" id="reload">REGISTER</div>`
            if(jsondata['is_registerd']){
                msg = '<div class="alert alert-success"><strong>&#10024 Login Successfully</strong></div>'
            }
            document.getElementById("div_login").style.display='none';
            document.getElementById("div_msg").style.display='';
            document.getElementById("div_msg").innerHTML=msg;
            if(! jsondata['is_registerd']){
                document.getElementById("reload").onclick=function(){
                    location.reload();
                }
            }
        })
        .catch((err)=>{
            console.log(err)
        });
        event.preventDefault()
    }
}

window.onload=function(){
    let reg_obj = new Register()
    reg_obj.render();
}