window.onload=function(){
	var select_all_existing_items=document.getElementById("all_existing_items");
	xhttp=new XMLHttpRequest();
	url='http://localhost:8000/hunger/get_items';
	xhttp.open('GET',url);
	var item_id_list=[];
	xhttp.onload=function(){
		var responseData=JSON.parse(xhttp.responseText);
		list=Object.keys(responseData);
		items_list=responseData[list[0]];
		console.log(items_list);
		for(i=0;i<items_list.length;i++){
			item_name=items_list[i]["item_name"];
			item_id=items_list[i]["item_id"];
			item_id_list.push(item_id);
			select_all_existing_items.options.add(new Option(item_name));
		}
	}
	xhttp.send();

	function goto_items(){
		index=select_all_existing_items.selectedIndex;
		if(index>0){
			item_id=item_id_list[index-1];
			window.open('http://localhost:8000/hunger/get_supplier_for_items_page?id='+item_id,"_self");

		}
		else{
			alert("Please select item");
		}
	}


	document.getElementById("update_button").addEventListener('click',goto_items);
}