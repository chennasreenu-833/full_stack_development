import requests

import json

res = requests.get('http://localhost:8000/hunger/get_items_list')
res = json.loads(res.content)
final_ans = {}
for each_item in res:
	item_name = each_item['item_name']
	supplier_name = each_item['supplier_name']
	item_price = each_item['item_price']
	if supplier_name in final_ans:
		final_ans[supplier_name]["all_items"] += [{"item_name": item_name, "item_price": item_price}]
	else:
		final_ans[supplier_name] = {}
		final_ans[supplier_name]["all_items"] = [{"item_name": item_name, "item_price": item_price}]
f = open('final_ans.json','w')
json.dump(final_ans, f, indent=4)
f.close()
