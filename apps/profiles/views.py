from django.shortcuts import render, get_object_or_404
from .models import ExpertProfile

def profile_list(request):
    profiles = ExpertProfile.objects.all()
    return render(request, 'profiles/profile_list.html', {'profiles': profiles})

def profile_detail(request, pk):
    profile = get_object_or_404(ExpertProfile, pk=pk)
    return render(request, 'profiles/profile_detail.html', {'profile': profile})

def search_results(request):
    query = request.GET.get('q', '')
    profiles = ExpertProfile.objects.filter(user__first_name__icontains=query)
    return render(request, 'profiles/search_results.html', {'profiles': profiles, 'query': query})
