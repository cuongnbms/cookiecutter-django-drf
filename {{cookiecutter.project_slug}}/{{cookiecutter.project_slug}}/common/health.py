from django.core.cache import cache
from django.db import connection
from django.http import JsonResponse


def _db_ok():
    try:
        with connection.cursor() as cursor:
            cursor.execute('SELECT 1')
            cursor.fetchone()
        return True
    except Exception:
        return False


def _cache_ok():
    try:
        cache.set('healthz', '1', timeout=1)
        return cache.get('healthz') == '1'
    except Exception:
        return False


def healthz(request):
    ok = _db_ok() and _cache_ok()
    return JsonResponse({'status': 'ok' if ok else 'error'}, status=200 if ok else 503)
