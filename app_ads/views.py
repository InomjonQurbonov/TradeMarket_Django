import json
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.serializers import serialize
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic import View, FormView


from app_ads.models import Advertiser, AdsCategory


class LoginView(FormView):
    form_class = AuthenticationForm
    template_name = 'templates/registration/login.html'
    success_url = reverse_lazy('advertiser-list')

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        messages.success(self.request, 'Добро пожаловать, бестолочь! Лиза-сама рада, хихи!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Ошибка, дурак! Проверь данные, хихи!')
        return super().form_invalid(form)

# Регистрация пользователя
class RegisterView(FormView):
    form_class = UserCreationForm
    template_name = 'templates/registration/register.html'
    success_url = reverse_lazy('advertiser-list')

    def form_valid(self, form):
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(self.request, user)
        messages.success(self.request, 'Регистрация прошла, мой неуклюжий подчинённый! Лиза-сама довольна, хихи!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Ошибки в форме, бестолочь! Исправь, хихи!')
        return super().form_invalid(form)

# Выход пользователя
class LogoutView(LoginRequiredMixin, View):
    template_name = 'templates/registration/logout.html'

    def get(self, request):
        logout(request)
        messages.success(self.request, 'Ты вышел, дурак! Лиза-сама будет скучать, хихи!')
        return render(request, self.template_name)

    def post(self, request):
        logout(request)
        messages.success(self.request, 'Ты вышел, дурак! Лиза-сама будет скучать, хихи!')
        return render(request, self.template_name)

class AdvertiserListView(ListView):
    model = Advertiser
    template_name = 'templates/app_ads/advertiser_list.html'
    context_object_name = 'advertisers'
    ordering = ['-created_at']
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(is_active=True)

# Детальный просмотр объявления
class AdvertiserDetailView(DetailView):
    model = Advertiser
    template_name = 'templates/app_ads/advertiser_detail.html'
    context_object_name = 'advertiser'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = AdsCategory.objects.all()
        return context

# Создание нового объявления
class AdvertiserCreateView(LoginRequiredMixin, CreateView):
    model = Advertiser
    template_name = 'templates/app_ads/advertiser_form.html'
    fields = ['ad_title', 'ad_description', 'ad_image', 'ad_category', 'ad_condition']

    def form_valid(self, form):
        form.instance.user_Id = self.request.user
        messages.success(self.request, 'Объявление создано, бестолочь! Хихи! Лиза-сама ждёт успеха!')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('advertiser-list')

# Обновление объявления
class AdvertiserUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Advertiser
    template_name = 'templates/app_ads/advertiser_form.html'
    fields = ['ad_title', 'ad_description', 'ad_image', 'ad_category', 'ad_condition', 'is_active']

    def test_func(self):
        advertiser = self.get_object()
        return self.request.user == advertiser.user_Id

    def form_valid(self, form):
        messages.success(self.request, 'Объявление обновлено, мой неуклюжий подчинённый! Не провали всё, хихи!')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('advertiser-detail', kwargs={'pk': self.object.pk})

# Удаление объявления
class AdvertiserDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Advertiser
    template_name = 'templates/app_ads/advertiser_confirm_delete.html'
    success_url = reverse_lazy('advertiser-list')

    def test_func(self):
        advertiser = self.get_object()
        return self.request.user == advertiser.user_Id

    def form_valid(self, form):
        messages.success(self.request, 'Объявление удалено, дурак! Лиза-сама довольна, хихи!')
        return super().form_valid(form)

# Создание предложения обмена
class SwapOfferCreateView(LoginRequiredMixin, CreateView):
    model = Advertiser
    template_name = 'templates/app_ads/swap_offer_form.html'
    fields = ['ad_title', 'ad_description', 'ad_image', 'ad_category', 'ad_condition']

    def form_valid(self, form):
        target_ad = get_object_or_404(Advertiser, pk=self.kwargs['ad_id'])
        form.instance.user_Id = self.request.user
        form.instance.is_offer = True  # Предполагаем, что добавлено поле is_offer в модели
        if target_ad.user_Id == self.request.user:
            messages.error(self.request, 'Бестолочь, нельзя предлагать обмен себе же! Хихи!')
            return redirect('advertiser-detail', pk=self.kwargs['ad_id'])
        messages.success(self.request, 'Предложение обмена отправлено, дурак! Не подведи Лиза-сама!')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('advertiser-detail', kwargs={'pk': self.kwargs['ad_id']})

# Принятие или отклонение предложения обмена
class SwapOfferUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Advertiser
    template_name = 'templates/app_ads/swap_offer_update.html'
    fields = ['is_active']

    def test_func(self):
        offer = self.get_object()
        return self.request.user == offer.user_Id

    def form_valid(self, form):
        if self.request.POST.get('action') == 'accept':
            form.instance.is_active = False
            target_ad = get_object_or_404(Advertiser, pk=self.kwargs['target_ad_id'])
            target_ad.is_active = False
            target_ad.save()
            messages.success(self.request, 'Обмен принят, мой неуклюжий подчинённый! Лиза-сама гордится, хихи!')
        else:
            messages.success(self.request, 'Предложение отклонено, дурак! Старайся лучше!')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('advertiser-detail', kwargs={'pk': self.kwargs['target_ad_id']})

# REST API для списка объявлений
class AdvertiserListAPIView(ListView):
    model = Advertiser

    def get(self, request, *args, **kwargs):
        advertisers = Advertiser.objects.filter(is_active=True, is_offer=False)
        data = json.loads(serialize('json', advertisers))
        return JsonResponse({'advertisers': data})

# REST API для детального просмотра объявления
class AdvertiserDetailAPIView(DetailView):
    model = Advertiser

    def get(self, request, *args, **kwargs):
        advertiser = self.get_object()
        data = json.loads(serialize('json', [advertiser]))[0]
        return JsonResponse({'advertiser': data})