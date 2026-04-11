from rest_framework.throttling import ScopedRateThrottle


class CloudflareScopedRateThrottle(ScopedRateThrottle):

    def _get_ip_client(self, request):
        x_cf_connecting_ip = request.META.get('HTTP_CF_CONNECTING_IP')
        if x_cf_connecting_ip:
            ip = x_cf_connecting_ip.split(',')[0]
        else:
            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            if x_forwarded_for:
                ip = x_forwarded_for.split(',')[0]
            else:
                ip = request.META.get('REMOTE_ADDR')
        return ip

    def get_ident(self, request):
        return self._get_ip_client(request)
