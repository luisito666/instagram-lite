# Django
from django.shortcuts import redirect
from django.urls import reverse

class ProfileCompletionMiddleware:
    """Esta clase sirve para que el usuario complete todo el perfil
       para poder interacturar con la plataforma.
    """

    def __init__(self, get_response ):
        """ Metodo
        """
        self.get_response = get_response
    
    def __call__(self, request):
        """
        """
        if not request.user.is_anonymous:
            if not request.user.is_staff:
                profile = request.user.profile
                if not profile.picture or not profile.biography:
                    if request.path not in [reverse('users:update_profile'), reverse('users:logout')]:
                        return redirect('users:update_profile')
        response = self.get_response(request)
        return response
