from django.contrib.admin import ModelAdmin


class NoDeleteActionModelAdmin(ModelAdmin):
    """
    Custom ModelAdmin class preventing the delete action from appearing in the admin actions.

    This class overrides the default behavior of the ModelAdmin to eliminate the
    "delete_selected" action from the list of available admin actions, ensuring
    that users cannot delete multiple objects at once using the admin interface.
    """

    def get_actions(self, request):
        actions = super().get_actions(request)
        if "delete_selected" in actions:
            del actions["delete_selected"]
        return actions
