from django.contrib import messages
from django.views.generic.edit import FormView

from .forms import ContactUsForm
from .tasks import proceed_email_us_form


class ShowEmailFormView(FormView):
    form_class = ContactUsForm
    template_name = 'contact_form.html'
    success_url = '/email-us'

    def form_valid(self, form):
        proceed_email_us_form.delay(
            contact_name=form.cleaned_data.get('contact_name'),
            title=form.cleaned_data.get('title'),
            message=form.cleaned_data.get('message'),
            email_from=form.cleaned_data.get('email_from')
        )

        messages.success(self.request, 'An e-mail has been sent!')
        return super().form_valid(form)
