from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import  AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, render
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic import View, FormView


from app_ads.models import Advertiser, AdsCategory, Notification
from app_ads.forms import CustomUserForm
from config.settings import DEFAULT_FROM_EMAIL


class LoginView(FormView):
    form_class = AuthenticationForm
    template_name = 'templates/registration/login.html'
    success_url = reverse_lazy('advertiser-list')

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        messages.success(self.request, 'Добро пожаловать, Дорогой ползовател !')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Ошибка, дурак! Проверь данные, хихи!')
        return super().form_invalid(form)


class RegisterView(FormView):
    form_class = CustomUserForm
    template_name = 'templates/registration/register.html'
    success_url = reverse_lazy('advertiser-list')

    def form_valid(self, form):
        form.save()
        email = form.cleaned_data.get('email')
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, email=email, password=password)
        login(self.request, user)
        messages.success(self.request, 'Регистрация прошла')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Ошибки в форме!')
        return super().form_invalid(form)


class LogoutView(LoginRequiredMixin, View):
    template_name = 'templates/registration/logout.html'

    def get(self, request):
        logout(request)
        messages.success(self.request, 'Ты вышел из сайта!')
        return render(request, self.template_name)

    def post(self, request):
        logout(request)
        messages.success(self.request, 'Ты вышел из сайта!')
        return render(request, self.template_name)


class AdvertiserListView(ListView):
    model = Advertiser
    template_name = 'templates/app_ads/advertiser_list.html'
    context_object_name = 'advertisers'
    ordering = ['-created_at']
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset().filter(is_active=True)
        search_query = self.request.GET.get('search', '')
        if search_query:
            queryset = queryset.filter(ad_title__icontains=search_query)
        category = self.request.GET.get('category', '')
        if category:
            queryset = queryset.filter(ad_category__id=category)
        condition = self.request.GET.get('condition', '')
        if condition:
            queryset = queryset.filter(ad_condition=condition)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = AdsCategory.objects.all()
        context['conditions'] = Advertiser._meta.get_field('ad_condition').choices
        context['search_query'] = self.request.GET.get('search', '')
        context['selected_category'] = self.request.GET.get('category', '')
        context['selected_condition'] = self.request.GET.get('condition', '')
        return context

class AdvertiserDetailView(DetailView):
    model = Advertiser
    template_name = 'templates/app_ads/advertiser_detail.html'
    context_object_name = 'advertiser'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = AdsCategory.objects.all()
        return context

class AdvertiserCreateView(LoginRequiredMixin, CreateView):
    model = Advertiser
    template_name = 'templates/app_ads/advertiser_form.html'
    fields = ['ad_title', 'ad_description', 'ad_image', 'ad_category', 'ad_condition']

    def form_valid(self, form):
        form.instance.user_Id = self.request.user
        messages.success(self.request, 'Объявление создано')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('advertiser-list')

class AdvertiserUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Advertiser
    template_name = 'templates/app_ads/advertiser_form.html'
    fields = ['ad_title', 'ad_description', 'ad_image', 'ad_category', 'ad_condition', 'is_active']

    def test_func(self):
        advertiser = self.get_object()
        return self.request.user == advertiser.user_Id

    def form_valid(self, form):
        messages.success(self.request, 'Объявление обновлено')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('advertiser-detail', kwargs={'pk': self.object.pk})

class AdvertiserDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Advertiser
    template_name = 'templates/app_ads/advertiser_confirm_delete.html'
    success_url = reverse_lazy('advertiser-list')

    def test_func(self):
        advertiser = self.get_object()
        return self.request.user == advertiser.user_Id

    def form_valid(self, form):
        messages.success(self.request, 'Объявление удалено')
        return super().form_valid(form)


class SwapOfferCreateView(LoginRequiredMixin, CreateView):
    model = Advertiser
    template_name = 'templates/app_ads/swap_offer_form.html'  # Исправлен путь
    fields = ['ad_title', 'ad_description', 'ad_image', 'ad_category', 'ad_condition']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        target_ad = get_object_or_404(Advertiser, pk=self.kwargs['ad_id'])
        context['target_ad'] = target_ad
        context['target_ad_id'] = self.kwargs['ad_id']
        return context

    def form_valid(self, form):
        target_ad = get_object_or_404(Advertiser, pk=self.kwargs['ad_id'])
        form.instance.user_Id = self.request.user
        form.instance.is_offer = True
        form.instance.target_ad = target_ad  # Устанавливаем связь
        if target_ad.user_Id == self.request.user:
            messages.error(self.request, 'Бестолочь, нельзя предлагать обмен себе же!')
            return redirect('advertiser-detail', pk=self.kwargs['ad_id'])

        response = super().form_valid(form)


        Notification.objects.create(
            user=target_ad.user_Id,
            message=f'Пользователь {self.request.user.username} предложил обмен на ваше объявление "{target_ad.ad_title}".',
            offer=form.instance
        )

        subject = f'Новое предложение обмена на "{target_ad.ad_title}"'
        message = (
            f'Здравствуйте, {target_ad.user_Id.username}!\n\n'
            f'Пользователь {self.request.user.username} предложил обмен на ваше объявление "{target_ad.ad_title}".\n'
            f'Название предложения: {form.instance.ad_title}\n'
            f'Посмотреть: http://{self.request.get_host()}/advertiser/{target_ad.pk}/\n\n'
            f'С уважением,\nTradeSite'
        )
        recipient = target_ad.user_Id.email
        if recipient:
            send_mail(
                subject,
                message,
                DEFAULT_FROM_EMAIL,
                [recipient],
                fail_silently=True,
            )
        else:
            print(f"Владелец {target_ad.user_Id.username} не указал email")

        messages.success(self.request, 'Предложение обмена отправлено!')
        return response

    def get_success_url(self):
        return reverse_lazy('advertiser-detail', kwargs={'pk': self.kwargs['ad_id']})


class SwapOfferUpdateView(LoginRequiredMixin, UpdateView):
    model = Advertiser
    template_name = 'templates/app_ads/swap_offer_update.html'
    fields = ['is_active']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['target_ad_id'] = self.kwargs.get('target_ad_id')
        return context

    def form_valid(self, form):
        target_ad = get_object_or_404(Advertiser, pk=self.kwargs['target_ad_id'])
        if self.request.POST.get('action') == 'accept':
            form.instance.is_active = False
            target_ad.is_active = False
            target_ad.save()
            Notification.objects.create(
                user=form.instance.user_id,
                message=f'Ваше предложение на "{target_ad.ad_title}" было принято пользователем {self.request.user.username}!',
                offer=form.instance
            )
            messages.success(self.request, 'Обмен принят!')
        else:
            form.instance.is_active = False
            Notification.objects.create(
                user=form.instance.user_id,
                message=f'Ваше предложение на "{target_ad.ad_title}" было отклонено пользователем {self.request.user.username}.',
                offer=form.instance
            )
            messages.success(self.request, 'Предложение отклонено!')
        return super().form_valid(form)

    def get_success_url(self):
        target_ad_id = self.kwargs.get('target_ad_id')
        if not target_ad_id:
            messages.error(self.request, 'Ошибка: ID целевого объявления не найден!')
            return reverse_lazy('advertiser-list')
        return reverse_lazy('advertiser-detail', kwargs={'pk': target_ad_id})