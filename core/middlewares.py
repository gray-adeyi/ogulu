from . import models

class SiteDataMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # add website data to every request
        response = self.get_response(request)
        return response

    def process_template_response(self, request, response, *args, **kwargs):
        try:
            response.context_data["site"] = models.Site.objects.first()
            return response
        except models.Site.DoesNotExist:
            return None