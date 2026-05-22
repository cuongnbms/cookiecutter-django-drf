from django.conf import settings
from rest_framework.throttling import ScopedRateThrottle


class CloudflareScopedRateThrottle(ScopedRateThrottle):

    def _get_ip_client(self, request):
        if getattr(settings, 'TRUST_CF_HEADERS', False):
            cf_ip = request.META.get('HTTP_CF_CONNECTING_IP')
            if cf_ip:
                return cf_ip.split(',')[0].strip()
        xff = request.META.get('HTTP_X_FORWARDED_FOR')
        if xff:
            return xff.split(',')[0].strip()
        return request.META.get('REMOTE_ADDR')

    def get_ident(self, request):
        return self._get_ip_client(request)
