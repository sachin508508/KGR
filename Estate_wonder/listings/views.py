# from django.shortcuts import render, get_object_or_404,redirect
# from .models import Listing
# from .forms import ListingForm
# from django.urls import reverse

# """def listing_detail(request, listing_id):
#     listing = Listing.objects.get(pk=listing_id)
#    # photo_main_base64 = base64.b64encode(listing.photo_main).decode('utf-8')
#     with open(listing.photo_main.path, 'rb') as f:
#         photo_main_data = f.read()
    
#     photo_main_base64 = base64.b64encode(photo_main_data).decode('utf-8')
#   #  return render(request, 'listings/listing_detail.html', {'listing': listing})
#     return render(request, 'listings/listing_detail.html', {'listing': listing, 'photo_main_base64': photo_main_base64})
# """

# def listing_detail(request, listing_id):
#     listing = get_object_or_404(Listing, pk=listing_id)
#     return render(request, 'listings/listing_detail.html', {'listing': listing})
# def listing_list(request):
#     listings = Listing.objects.filter(is_published=True)
#     return render(request, 'listings/listing_list.html', {'listings': listings})

# def listing_search_results(request):
#     # Implement your search logic here
#     query = request.GET.get('q')
#     if query:
#         listings = Listing.objects.filter(title__icontains=query, is_published=True)
#     else:
#         listings = []
#     return render(request, 'listings/listing_search_results.html', {'listings': listings, 'query': query})


# def listing_form(request):
#     if request.method == 'POST':
#         form = ListingForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect()  # Replace 'success_url' with the URL name for the success page
#     else:
#         form = ListingForm()
#     return render(request, 'listings/listing_form.html', {'form': form})
# def listing_delete_confirm(request, listing_id):
#     listing = get_object_or_404(Listing, pk=listing_id)
#     return render(request, 'listings/listing_delete_confirm.html', {'listing': listing})

# def listing_success(request):
#     # This view can handle successful operations (e.g., listing creation, editing, deletion)
#     # You may want to provide a success message or redirect to another page
#     return render(request, 'listings/listing_success.html')

# def listing_error(request):
#     # This view can handle errors (e.g., form validation errors)
#     # You may want to provide error messages to the user or redirect to another page
#     return render(request, 'listings/listing_error.html')
from django.shortcuts import render, get_object_or_404, redirect
from .models import Listing
from .forms import ListingForm

def listing_detail(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    return render(request, 'listings/listing_detail.html', {'listing': listing})

def listing_list(request):
    listings = Listing.objects.filter(is_published=True)
    return render(request, 'listings/listing_list.html', {'listings': listings})

def listing_search_results(request):
    query = request.GET.get('q')
    if query:
        listings = Listing.objects.filter(title__icontains=query, is_published=True)
    else:
        listings = []
    return render(request, 'listings/listing_search_results.html', {'listings': listings, 'query': query})

def listing_form(request):
    if request.method == 'POST':
        form = ListingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/listings/success')  # Redirect to the success page
    else:
        form = ListingForm()
    return render(request, 'listings/listing_form.html', {'form': form})

def listing_delete_confirm(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    return render(request, 'listings/listing_delete_confirm.html', {'listing': listing})

def listing_success(request):
    return render(request, 'listings/listing_success.html')

def listing_error(request):
    return render(request, 'listings/listing_error.html')
