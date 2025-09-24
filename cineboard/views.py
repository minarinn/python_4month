from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from . import models, forms

class CreateFilmView(LoginRequiredMixin, generic.CreateView):
    model = models.Films
    form_class = forms.FilmsForm
    template_name = 'cineboard/create_film.html'
    success_url = '/all_films/'

class UpdateFilmView(LoginRequiredMixin, generic.UpdateView):
    model = models.Films
    form_class = forms.FilmsForm
    template_name = 'cineboard/update_film.html'
    success_url = '/all_films/'

    def get_object(self, *args, **kwargs):
        film_id = self.kwargs.get('id')
        return get_object_or_404(models.Films, id=film_id)

class DeleteFilmView(LoginRequiredMixin, generic.DeleteView):
    template_name = 'cineboard/confirm_delete_film.html'
    success_url = '/all_films/'

    def get_object(self, *args, **kwargs):
        film_id = self.kwargs.get('id')
        return get_object_or_404(models.Films, id=film_id)

class RegisterView(generic.View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, template_name='cineboard/register_cine.html', context={'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('cineboard:all_films')
        return render(request, template_name='cineboard/register_cine.html', context={'form': form})

class AuthLoginView(generic.View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'cineboard/login_cine.html', {'form': form})

    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('cineboard:all_films')
        return render(request, 'cineboard/login_cine.html', {'form': form})
    
class AllFilmsListView(generic.ListView):
    model = models.Films
    template_name = 'cineboard/tv_list.html'
    context_object_name = 'tv_lst'
    ordering = ['-created_at']

    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.GET.get('s', '').strip()
        genre = self.request.GET.get('genre', '').strip()
        tag = self.request.GET.get('tag', '').strip()
        if q:
            qs = qs.filter(title__icontains=q)
        if genre:
            qs = qs.filter(genre=genre)
        if tag:
            qs = qs.filter(tags__name=tag)
        return qs.distinct()

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['s'] = self.request.GET.get('s', '')
        ctx['genre'] = self.request.GET.get('genre', '')
        ctx['tag'] = self.request.GET.get('tag', '')
        ctx['all_tags'] = models.Tag.objects.all()
        ctx['all_genres'] = [g[0] for g in models.Films.GENRE]
        return ctx

class AuthLogoutView(generic.View):
    def get(self, request):
        logout(request)
        return redirect('cineboard:login_cine')