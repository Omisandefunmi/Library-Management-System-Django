from django.contrib.admin.apps import AdminConfig


class DjangoProjectAdminConfig(AdminConfig):
    default_site = 'djangoProject.admin.DjangoProjectAdminSite'
