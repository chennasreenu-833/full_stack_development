xhttp_request=new XMLHttpRequest();
url="http://localhost:8000/hunger/get_suppliers";
xhttp_request.open('GET',url);
xhttp_request.onload=function(){
	var responseData=JSON.parse(xhttp_request.responseText);
	list=Object.keys(responseData);
	console.log(list);
	for(i=0;i<list.length;i++){
		var supplier_name=responseData[list[i]]["supplier_name"];
		var supplier_address=responseData[list[i]]["supplier_address"];
		var supplier_phone=responseData[list[i]]["supplier_phone"];
		var anchor=document.createElement("a");
		anchor.setAttribute('href','http://localhost:8000/hunger/get_items_from_supplier?id='+list[i]+'&supplier_name='+supplier_name);
		anchor.setAttribute('class','anchor_class');
		var dinner_div=document.createElement("div");
		dinner_div.setAttribute('class','dinner_class');
		var title_top_div=document.createElement("div");
		title_top_div.setAttribute('class','supplier_top');
		var title_div=document.createElement("div");
		title_div.setAttribute('class','supplier_title');
		title_div.appendChild(document.createTextNode(supplier_name+" "+supplier_address+" "+supplier_phone));
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