from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from expertclass import settings
import os
from xhtml2pdf import pisa

def fetch_resources(uri, rel):
    path = os.path.join(settings.STATIC_URL, uri.replace(settings.STATIC_URL, ""))
    return path

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result,link_callback=fetch_resources)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None



