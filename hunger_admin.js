var responseData;
window.onload=function(){
    
    xhttp=new XMLHttpRequest();
    url='http://localhost:8000/hunger/get_supplier_status';
    var state_list=[];
    xhttp.open('GET',url);
   
    xhttp.onload=function(){
        responseData=JSON.parse(xhttp.responseText);
        list=Object.keys(responseData);
        for(i=0;i<list.length;i++){
            supplier_name=responseData[list[i]]["supplier_name"];
            supplier_state=responseData[list[i]]["supplier_state"];
            var anchor_div=document.createElement("div");
            anchor_div.setAttribute('class','anchor_class');
            var icon_div=document.createElement("div");
            icon_div.setAttribute('class','icon_class');
            var title_top_div=document.createElement("div");
            title_top_div.setAttribute('class','title_top_class');
            var title_div=document.createElement("div");
            title_div.setAttribute('class','title_class');
            title_div.innerHTML=supplier_name;
            var checkbox_top_div=document.createElement('div');
            checkbox_top_div.setAttribute('class','check_box_top');
            var check_box_div=document.createElement("input");
            check_box_div.setAttribute('type','checkbox');
            check_box_div.setAttribute('class','check_box');
            check_box_div.setAttribute('index',i);
            check_box_div.onchange=function(){
                if(this.checked){
                    index = this.getAttribute('index');
                    responseData[list[index]]['supplier_state'] = 1;
                }
                else{
                    index = this.getAttribute('index');
                    responseData[list[index]]['supplier_state'] = 0;
                }
            }
            if(supplier_state==1){
                check_box_div.checked=true;
            }
            title_top_div.appendChild(title_div);
            checkbox_top_div.appendChild(check_box_div);
            anchor_div.appendChild(icon_div);
            anchor_div.appendChild(title_top_div);
            anchor_div.appendChild(checkbox_top_div);

            document.getElementById("list_box").appendChild(anchor_div);

        }
    }
    xhttp.send();
    function save_clicked(){
        // save responseData
        console.log("button clicked");
        list = Object.keys(responseData);
        console.log("list lenght is "+String(list.length));
        s="";
        for(i=0;i<list.length;i++)
        {
            id  = list[i];
            status = responseData[list[i]]["supplier_state"];
            s=s+String(id)+":"+String(status)+"_";
        }
        console.log("the string need to send is "+String(s));
        xhttp_save=new XMLHttpRequest();
        url_save='http://localhost:8000/hunger/save_state';
        xhttp_save.open('POST',url_save);
        params="id_state="+s;
        xhttp_save.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
        xhttp_save.onload=function(){
            response_data=JSON.parse(xhttp_save.responseText);
            console.log(response_data);
            if(response_data["response"]=="true"){
                alert("Details saved successfully");
            }
            else{
                alert("Failed to save Details");
            }
        }
        xhttp_save.send(params);
    }
    document.getElementById("save_changes").addEventListener('click', save_clicked);


}