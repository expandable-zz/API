from tastypie.authentication import Authentication
from tastypie.http import HttpUnauthorized
from system.models import Application, Session
from django.utils.datetime_safe import datetime

class ApiAuthentication(Authentication):

    def _unauthorized(self):
        return HttpUnauthorized()

    def is_authenticated(self, request, **kwargs):

        api_key = request.META.get('HTTP_API_KEY')

        if api_key == None:
            return self._unauthorized()

        try:
            app = Application.objects.get(api_key=api_key)
        except (Application.DoesNotExist, Application.MultipleObjectsReturned):
            return self._unauthorized()

        request.app = app

        token = request.META.get('HTTP_TOKEN')

        if token:
            try:
                session = Session.objects.get(token=token)
            except Session.DoesNotExist:
                return self._unauthorized()

            if session.time_end < datetime.now():
                # Session expired
                return self._unauthorized()

            if session.app != app:
                # Wrong Session
                return self._unauthorized()

            request.user=session.user
        return True

    def get_identifier(self, request):
        return request.META.get('HTTP_API_KEY', 'nokey')