/** Loads the widget as an iframe in the specified div **/
(function(){

var widget_div = document.getElementById('widget_{{ widget_id }}');

if ( widget_div ) {
	widget_div.innerHTML = '';
	widget_div.style.width = 'auto';
	widget_div.style.height = 'auto';
	
	var f = document.createElement('iframe');
    f.id = "widgetframe_{{ widget_id }}";
    f.style.border = "1px solid silver";
    f.style.overflow = "hidden";
    f.scrolling = "no";
    f.src = "{{ iframe_url }}";
    
    var widget_css = '#widget_{{ widget_id }} * {margin:0;padding:0;border:0;font-size:100%;vertical-align:baseline;display:inline-block}';
    var widget_head = document.getElementsByTagName('head')[0];
    var widget_style = document.createElement('style');
    widget_style.type = 'text/css';
    
    if(widget_style.styleSheet) widget_style.styleSheet.cssText = widget_css;
    else widget_style.appendChild(document.createTextNode(widget_css));
    
    widget_head.appendChild(widget_style);
    widget_div.appendChild(f);
}

}());
