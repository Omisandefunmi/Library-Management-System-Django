from django.contrib import admin


class DjangoProjectAdminSite(admin.AdminSite):
    site_title = "Good Reads Admin Site"
    site_header = "Welcome to the Good Reads Admin Interface"
    index_title = "Good Reads index"
