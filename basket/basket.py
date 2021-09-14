
class Basket():
    """
    A base Basket class, providing some default behaviors that 
    can be inherited or overrided, as necessary.
    """
    
    def __init__(self, request):
        self.session = request.session
        basket = self.session.get('skey')
        if 'skey' not in request.session:
            basket = self.session['skey'] = {}
        self.basket = basket

# from django.contrib.sessions.models import Session
# s = Session.objects.get(pk='<get_session_key_form_browser_session>')
# s.get_decoded()
