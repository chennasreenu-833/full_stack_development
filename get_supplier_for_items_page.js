
xhttp_request=new XMLHttpRequest();
url='http://localhost:8000/hunger/get_supplier_for_items_list?id='+id;
xhttp_request.open('GET',url);
function clicked_plus(e){
	var target = e.target || e.srcElement;
	var j=target.getAttribute("index_plus");
	parent = target.parentElement;
	all_childs = parent.childNodes;
	for(i=0;i<all_childs.length;i++)
	{
		if (all_childs[i].className == "value")
		{
			my_child = all_childs[i];
			break;
		}
	}
	value = parseInt(my_child.textContent);

	value++;
	qty[j]=value;
	my_child.textContent = value;
}
function clicked_minus(e){
	var target = e.target || e.srcElement;
	var j=target.getAttribute("index_minus");
	parent = target.parentElement;
	all_childs = parent.childNodes;
	for(i=0;i<all_childs.length;i++)
	{
		if (all_childs[i].className == "value")
		{
			my_child = all_childs[i];
			break;
		}
	}
	value = parseInt(my_child.textContent);
	if(value>0){
		value--;
		qty[j]=value;
	}
	my_child.textContent = value;
}
function checkout_clicked(e){
	total=0;
	items=0;
	for(i=0;i<val.length;i++){
		total+=(qty[i]*val[i]);
		items+=qty[i];
	}
	alert("You have Ordered: \nitems: "+items+
		"\nTotal Price :"+total);

}
document.getElementById("checkout").addEventListener("click",checkout_clicked);

xhttp_request.onload=function(){
	var responseData=JSON.parse(xhttp_request.responseText);
	list=Object.keys(responseData);
	data=responseData[list[0]];
	if(data.length>0){
			for(i=0;i<data.length;i++){
		var item_name=data[i]["item_name"];
		var item_price=data[i]["price"];
		var supplier_name=data[i]["supplier_name"];
		var supplier_id=data[i]["supplier_id"];
		var time_to_deliver=data[i]["time_to_deliver"];
		val.push(item_price);
		qty.push(0);
		var list_box=document.createElement("div");
		list_box.setAttribute('class','anchor_class');
		var item_div=document.createElement("div");
		item_div.setAttribute('class','item_class');
		var title_top_div=document.createElement("div");
		title_top_div.setAttribute('class','item_top');
		var title_div=document.createElement("div");
		title_div.setAttribute('class','item_title');
		title_div.appendChild(document.createTextNode(supplier_name+" "+item_name+"   Price: "+item_price+"  Delivery Time: "+time_to_deliver));
		var plus_div=document.createElement("div");
		plus_div.setAttribute('class','plus_class');
		plus_div.setAttribute('index_plus',i);
		plus_div.addEventListener("click",clicked_plus);
		
		var value_div=document.createElement("div");
		value_div.setAttribute('class','value');
		value_div.appendChild(document.createTextNode(0));
		var minus_div=document.createElement("div");
		minus_div.setAttribute('class','minus_class');
		minus_div.setAttribute('index_minus',i);
		minus_div.addEventListener("click",clicked_minus);
		title_top_div.appendChild(title_div);
		list_box.appendChild(item_div);
		list_box.appendChild(title_top_div);
		list_box.appendChild(plus_div);
		list_box.appendChild(value_div);
		list_box.appendChild(minus_div);
		document.getElementById('list').appendChild(list_box);
	}

	}
	else{
		alert("Sorry no restaurants available!!!");
	}

}
xhttp_request.send();
var val=[];
var qty=[];
document.getElementById("title").appendChild(document.createTextNode("Hungry App"));
