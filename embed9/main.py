from embed9.forms import DummyForm


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
    
    def get_form_class(self):
        """ Return form class representing additional widget options such as color or size """
        return self.form_class
    form_class = DummyForm
    
    def get_form_template(self):
        """ Return form template """
        return self.form_template
    form_template = 'embed9/form.html'
