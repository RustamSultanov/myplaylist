from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Track
from .forms import LoginForm, EditTrackForm, UploadTrackForm, ProfileForm
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.forms.models import model_to_dict
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

User = get_user_model()

# # Create your views here.


@login_required
def upload_track_view(request):
    form_user = UploadTrackForm(request.POST or None, request.FILES or None)
    if form_user.is_valid():
        new_track = form_user.save(commit=False)
        new_track.name = form_user.cleaned_data['name']
        new_track.artist = form_user.cleaned_data['artist']
        new_track.rating = form_user.cleaned_data['rating']
        new_track.image = form_user.cleaned_data['image']
        new_track.audio_file = form_user.cleaned_data['audio_file']
        new_track.user = request.user
        new_track.save()
        return HttpResponseRedirect(reverse('base'))
    context = {'form_user': form_user}
    return render(request, 'upload_track.html', context)


@login_required
def edit_track_view(request, track_id):
    track = get_object_or_404(Track, id=track_id, user=request.user)
    form = EditTrackForm(
        request.POST or None,
        request.FILES or None,
        initial=model_to_dict(track),
        instance=track)
    if form.is_valid():
        new_user = form.save()
        new_user.save()
        return HttpResponseRedirect(reverse('base'))
    context = {'form_user': form,'track':track}
    return render(request, 'edit_track.html', context)


@login_required
def edit_profile_view(request, user_id):
    user = get_object_or_404(User, id=user_id)
    form_user = ProfileForm(
        request.POST or None,
        request.FILES or None,
        initial=model_to_dict(user),
        instance=user)
    if form_user.is_valid():
        new_user = form_user.save()
        new_user.save()
        return HttpResponseRedirect(reverse('base'))
    context = {'form_user': form_user, 'user': user}
    return render(request, 'edit-profile.html', context)


@login_required
def track_list(request):
    track_list = Track.objects.filter(user=request.user.id)
    track_count = track_list.count()
    context = {'track_list': track_list, 'track_count': track_count}
    return render(request, 'tracks-table.html', context)


@login_required
def delete_track(request, track_id):
    author_id = request.user
    track = get_object_or_404(Track, user=author_id, id=track_id)
    track.delete()
    return HttpResponseRedirect(reverse('base'))
