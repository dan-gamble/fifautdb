# Core imports
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Object types paired up to available Models
OBJECT_TYPES = {
    'Club': 'club',
    'League': 'league',
    'Nation': 'nation'
}


def cbv_pagination(self, context, query, per_page, cbv_context):

    # Create pagination for the players return
    paginator = Paginator(query, per_page)
    # Get the page from the URL
    page = self.request.GET.get('page')

    try:
        # Deliver the requested page
        context[cbv_context] = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        context[cbv_context] = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        context[cbv_context] = paginator.page(paginator.num_pages)


def base_objects(context):
    # Gets the Object Type from the passed model and defines the base filter
    base_object = OBJECT_TYPES[context['object'].__class__.__name__]

    return base_object


def base_objects_add_id(context):
    # Gets the Object Type from the passed model and defines the base filter
    base_object = OBJECT_TYPES[context['object'].__class__.__name__] + '_id'
    return base_object