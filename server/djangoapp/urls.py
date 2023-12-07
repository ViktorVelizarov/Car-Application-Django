from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import about, contact, get_dealerships, registration_request, login_request, logout_request, get_dealer_details, add_review
app_name = 'djangoapp'
urlpatterns = [
    # path('navbar/', navbar_view, name='navbar'),
    # route is a string contains a URL pattern
    # view refers to the view function
    # name the URL

    # path for about view
    path('about/', about, name='about'),
    # path for contact us view
    path('contact/', contact, name='contact'),

    # path for registration
    path('registration/', registration_request, name='registration'),
    # path for login
    path('login/', login_request, name='login'),
    # path for logout
    path('logout/', logout_request, name='logout'),

    path(route='', view=get_dealerships, name='index'),

    # path for dealer reviews view
    path('dealer/<int:dealer_id>/', get_dealer_details, name='dealer_details'),

    # path for add a review view
    path(route='dealer/<int:dealer_id>/add_review', view=add_review, name='add_review')


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)