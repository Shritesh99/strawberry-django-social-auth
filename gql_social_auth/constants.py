from django.utils.translation import gettext_lazy as _


class Messages:
    NO_PROVIDER = [{"message": _("Provider not found"), "code": "no_provider"}]

    @classmethod
    def user_instance_error(cls, user):
        return [{"message": _('`{}` is not a user instance').format(type(user).__name__),
                 "code": "user_model_improper_instance"}]

    @classmethod
    def exception(cls, e):
        return [{"message": _('{}'.format(e)), "code": "exception"}]
