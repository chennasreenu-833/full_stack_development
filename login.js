var btn=document.getElementById("button");
if(btn){
	btn.addEventListener("click", function(){
    username=document.getElementById("username").value;
    password=document.getElementById("password").value;
    if(username.length>0&&password.length>0){
        params="username="+username+"&password="+password;
        xhttp=new XMLHttpRequest();
        url='http://localhost:8000/hunger/check_supplier_login';
        xhttp.open('POST',url);
        xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
        xhttp.onload=function(){
        var responseData=xhttp.responseText;
        if(responseData!="failed"&&responseData!="invalid"){
            alert("login_success");
        }
        else{
            alert("login_failed");
        }

    }
    xhttp.send(params);
    }
    else{
        alert("Please fill in details");
    }
    
});
}

