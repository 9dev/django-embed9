{{ widget_name }} = function (){	
	var divs = [];
	var item, i;
	
	if ( typeof(document.getElementsByClassName) == "function" ) {
		divs = document.getElementsByClassName('{{ widget_name }}');
	}
	else {
		var temp = document.getElementsByTagName("div");
		for (i = 0; i < temp.length; ++i) {
			if (temp[i].className == '{{ widget_name }}') divs.push(temp[i]);
		}
	}
	
	for (i = 0; i < divs.length; ++i) {
		item = divs[i];

		if (item.innerHTML == '') {
			item.innerHTML = '';
			item.style.width = 'auto';
			item.style.height = 'auto';
			
			var f = document.createElement('iframe');
		    f.id = '{{ widget_name }}_frame';
		    f.style.border = "1px solid silver";
		    f.style.overflow = "hidden";
		    f.scrolling = "no";
		    f.src = "//{{ domain }}{{ iframe_url }}";
		    
		    var widget_css = '.{{ widget_name }} * {margin:0;padding:0;border:0;font-size:100%;vertical-align:baseline;display:inline-block}';
		    var widget_head = document.getElementsByTagName('head')[0];
		    var widget_style = document.createElement('style');
		    widget_style.type = 'text/css';
		    
		    if(widget_style.styleSheet) widget_style.styleSheet.cssText = widget_css;
		    else widget_style.appendChild(document.createTextNode(widget_css));
		    
		    widget_head.appendChild(widget_style);
		    item.appendChild(f);
		}
	}
};
