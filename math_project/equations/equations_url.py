from django.urls import path

# from rule_engine.views_engine import check_rule
# from rule_engine.views_engine import needed_features
from . import views

urlpatterns = [
    path('ess/', views.get_essential),
    # path('flow_id/<int:flow_id>/check_rule/', check_rule, name='check_rule'),
    # path('flow_id/<int:flow_id>/needed_features', needed_features, name='needed_features'),
]
