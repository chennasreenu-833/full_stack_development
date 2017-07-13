xhttp_request=new XMLHttpRequest();
url="http://localhost:8000/hunger/get_items";
xhttp_request.open('GET',url);
xhttp_request.onload=function(){
	var responseData=JSON.parse(xhttp_request.responseText);
	list=Object.keys(responseData);
	items_list=responseData[list[0]];
	for(i=0;i<items_list.length;i++){
		item_name=items_list[i]["item_name"];
		item_id=items_list[i]["item_id"];
		var anchor=document.createElement("a");
		anchor.setAttribute('href','http://localhost:8000/hunger/get_supplier_for_items_page?id='+item_id);
		anchor.setAttribute('class','anchor_class');
		var dinner_div=document.createElement("div");
		dinner_div.setAttribute('class','dinner_class');
		var title_top_div=document.createElement("div");
		title_top_div.setAttribute('class','supplier_top');
		var title_div=document.createElement("div");
		title_div.setAttribute('class','supplier_title');
		title_div.appendChild(document.createTextNode(item_name));
		var arrow_div=document.createElement("div");
		arrow_div.setAttribute('class','arrow');
		title_top_div.appendChild(title_div);
		anchor.appendChild(dinner_div);
		anchor.appendChild(title_top_div);
		anchor.appendChild(arrow_div);
		document.getElementById('list').appendChild(anchor);
	}

}
xhttp_request.send();