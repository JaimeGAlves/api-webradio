from django.db import transaction
from .models import Sponsor

def reorganize_sponsor_ids():
    with transaction.atomic():
        sponsors = Sponsor.objects.all().order_by('id')
        current_id = 1
        for sponsor in sponsors:
            if sponsor.id != current_id:
                sponsor.id = current_id
                sponsor.save(update_fields=['id'])
            current_id += 1
        return current_id