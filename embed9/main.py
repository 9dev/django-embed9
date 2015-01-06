
class Embeddable:
    
    def get_widget_template(self):
        """ Return name of the template containing iframe contents """
        return self.widget_template
    widget_template = 'embed9/widget.html'
    
    def get_code_template(self):
        """ Return name of the template containing embed code for external websites """
        return self.code_template
    code_template = 'embed9/code.html'
    
    def get_loader_template(self):
        """ Return name of the template containing javascript loader of the widget """
        return self.loader_template
    loader_template = 'embed9/loader.js'
    