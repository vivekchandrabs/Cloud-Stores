count = 0
var cart= [{}];


$( "#item-add" ).click(function() {
	var itemname = $( "#item-list option:selected" ).text();
	var itemid = $( "#item-list option:selected" ).attr("value");
	var itemquant = $( "#item-quant").val();
  	var tablerow = "<tr><td>" + itemid +"</td><td>" + itemname +"</td><td>" +  itemquant +"</td></tr>";
  	item = {};
  	item.name = itemname;
  	item.id = itemid;
  	item.quantity = itemquant;
  	cart[count] = item;
  	count++;
  	$("#table-body").append(tablerow);
});