window.onload = function(){
	var select_all_existing_items=document.getElementById("all_existing_items");
	var div=document.getElementById("header_title");
	div.innerHTML = "Welcome  "+String(username);
	xhttp=new XMLHttpRequest();
	url='http://localhost:8000/hunger/get_items_for_supplierid';
	xhttp.open('POST',url);
	params='id='+userid;
	var item_id_list=[];
	var item_price_list=[];
	xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
	xhttp.onload=function(){
		var responseData=JSON.parse(xhttp.responseText);
		list=Object.keys(responseData);
		
		for(i=0;i<list.length;i++){
			item_name=String(responseData[list[i]]["item_name"]);
			item_id=String(list[i]);
			item_price=responseData[list[i]]["price"];
			item_id_list.push(item_id);
			item_price_list.push(item_price);
			select_all_existing_items.options.add(new Option(item_name));
		}
		
		

	};
	xhttp.send(params);



	function get_price_for_item(){
		index=select_all_existing_items.selectedIndex;
		if(index>0){
				document.getElementById("price_box").value=item_price_list[index-1];
			}
			if(index==0){
				document.getElementById("price_box").value="";
			}
		

	}

	function update_price(){
		index=select_all_existing_items.selectedIndex;
		if(index>0){
			item_id=item_id_list[index-1];
			supplier_id=userid;
			price=document.getElementById("price_box").value;
			xhttp_update=new XMLHttpRequest();
			url='http://localhost:8000/hunger/update_supplier_item_price';
			xhttp_update.open('POST',url);
			params='supplier_id='+supplier_id+'&item_id='+item_id+'&price='+price;
			xhttp_update.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
			xhttp_update.onload=function(){
				responseData=JSON.parse(xhttp_update.responseText);
				if(responseData['response']=='true'){
					alert("update successful");
					item_price_list[index-1]=price;
				}
				else{
					alert("update_failed");
				}

	};
	xhttp_update.send(params);


		}
	}

	select_all_existing_items.addEventListener('change',get_price_for_item);
	document.getElementById("update_button").addEventListener('click',update_price);



};