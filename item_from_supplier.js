xhttp_request=new XMLHttpRequest();
url='http://localhost:8000/hunger/get_supplier_items?id='+id;
xhttp_request.open('GET',url);
xhttp_request.onload=function(){
	var responseData=JSON.parse(xhttp_request.responseText);
	list=Object.keys(responseData);
	console.log(list);
	for(i=0;i<list.length;i++){
		var item_name=responseData[list[i]]["item_name"];
		var item_price=responseData[list[i]]["item_price"];
		var time_to_deliver=responseData[list[i]]["time_to_deliver"];
		var list_box=document.createElement("div");
		list_box.setAttribute('class','anchor_class');
		var item_div=document.createElement("div");
		item_div.setAttribute('class','item_class');
		var title_top_div=document.createElement("div");
		title_top_div.setAttribute('class','item_top');
		var title_div=document.createElement("div");
		title_div.setAttribute('class','item_title');
		title_div.appendChild(document.createTextNode(item_name+"    "+item_price+"   "+time_to_deliver));
		var plus_div=document.createElement("div");
		plus_div.setAttribute('class','plus_class');
		var value_div=document.createElement("div");
		value_div.setAttribute('class','value');
		var minus_div=document.createElement("div");
		minus_div.setAttribute('class','minus_class');
		title_top_div.appendChild(title_div);
		list_box.appendChild(item_div);
		list_box.appendChild(title_top_div);
		list_box.appendChild(plus_div);
		list_box.appendChild(value_div);
		list_box.appendChild(minus_div);
		document.getElementById('list').appendChild(list_box);
	}
}
xhttp_request.send();