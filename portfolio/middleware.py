
import hashlib
from datetime import date
from django.utils.deprecation import MiddlewareMixin
from .models import PageVisit

class AnalyticsMiddleware(MiddlewareMixin):
    def process_request(self, request):
        path = request.path
        
        # Don't track static/media/admin/api
        ignored_prefixes = ['/portfolio-admin/', '/media/', '/static/', '/ai/chat/']
        if any(path.startswith(p) for p in ignored_prefixes):
            return
            
        # Ignore file extensions
        if '.' in path.split('/')[-1]:
            return
            
        # Create anonymous day-scoped hash
        ip = request.META.get('REMOTE_ADDR', '127.0.0.1')
        user_agent = request.META.get('HTTP_USER_AGENT', 'unknown')
        today = date.today().isoformat()
        
        raw_id = f"{ip}-{user_agent}-{today}"
        visitor_hash = hashlib.sha256(raw_id.encode('utf-8')).hexdigest()
        
        # Simple non-blocking create
        try:
            PageVisit.objects.create(path=path, visitor_hash=visitor_hash)
        except Exception:
            pass # Failsafe
