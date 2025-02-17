from .auth_urls import urlpatterns as auth_urls
from .user_urls import urlpatterns as user_urls
from .subscription_urls import urlpatterns as subscription_urls

# Combine all urlpatterns
urlpatterns = auth_urls + user_urls + subscription_urls
