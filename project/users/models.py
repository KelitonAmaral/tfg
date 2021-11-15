from __future__ import unicode_literals

from django.apps import apps
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, UserManager
from django.db import models
from django.db.models import Q
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from datetime import timedelta, datetime

from utils.gerador_hash import gerar_hash

class AdministratorActiveManager(UserManager):
    def get_queryset(self):
        return super().get_queryset().filter(type='ADMINISTRATOR', is_active=True)


class AthleteActiveManager(UserManager):
    def get_queryset(self):
        return super().get_queryset().filter(type='ATHLETE', is_active=True)


class CoachActiveManager(UserManager):
    def get_queryset(self):
        return super().get_queryset().filter(type='COACH', is_active=True)


class GuestActiveManager(UserManager):
    def get_queryset(self):
        return super().get_queryset().filter(type='GUEST', is_active=True)
    

class User(AbstractBaseUser):
    #1 campo da tupla fica no banco de dados
    #2 campo da tupla eh mostrado para o usuario
    TYPES_USERS = (
        ('ADMINISTRATOR', 'Administrator'),
        ('ATHLETE', 'Athlete' ),
        ('COACH', 'Coach'),
        ('GUEST', 'Guest' ),
    ) 
    
    TYPE_GENDER = (
        ('FEMALE', 'Female'),
        ('MALE', 'Male'),
    )

    USERNAME_FIELD = 'email'

    type = models.CharField(_('User type *'), max_length=13, choices=TYPES_USERS, default='GUEST', help_text='* Required fields')
    name = models.CharField(_('Name *'), max_length=100)
    email = models.EmailField(_('Email'), unique=True, max_length=100, db_index=True)
    cpf = models.CharField(_('CPF *'),max_length=14,help_text='ATENTION: just numbers')
    phone = models.CharField(_('Cellphone *'),max_length=14, help_text='ATENTION: just numbers') 
    birth_date = models.DateField(_('Date of birth *'), help_text='dd/mm/aaaa')       
    gender = models.CharField(_('Gender *'), max_length=10, choices=TYPE_GENDER) 
    
    is_active = models.BooleanField(_('Active'), default=False, help_text='If active, the user has permission to access the system')
    slug = models.SlugField('Hash', max_length= 200, null=True, blank=True)
       
    weight = models.DecimalField(_('Weight (Kg)'), max_digits=5, decimal_places=2, null=True, blank=True)
    height = models.DecimalField(_('Height (meters)'), max_digits=3, decimal_places=2, null=True, blank=True)     
    
    regulatory_agency_registration = models.CharField(_('Regulatory agency registration '), max_length=100, null=True, blank=True)

    objects = UserManager()
    administrators = AdministratorActiveManager()
    athletes = AthleteActiveManager()
    coaches = CoachActiveManager()
    guests = GuestActiveManager()    

    class Meta:
        ordering            =   ['type', 'name']
        verbose_name        =   _('user')
        verbose_name_plural =   _('users')

    def __str__(self):
        return '%s | %s' % (self.name, self.type)

    def has_module_perms(self, app_label):
        return True

    def has_perm(self, perm, obj=None):
        return True

    @property
    def get_first_name(self):
        nomes = self.nome.split()
        return nomes[0]

    @property
    def get_last_name(self):
        nomes = self.nome.split()
        return nomes[-1]
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = gerar_hash()
        self.name = self.name.upper()
        if not self.id:
            self.set_password(self.password) #criptografa a senha digitada no forms
        super(User, self).save(*args, **kwargs)

    def get_id(self):
        return self.id

    @property
    def is_staff(self):
        if self.tipo == 'ADMINISTRATOR':
            return True
        return False

    @property
    def get_absolute_url(self):
        return reverse('users_update', args=[str(self.id)])

    @property
    def get_delete_url(self):
        return reverse('users_delete', args=[str(self.id)])

    @property
    def get_user_register_activate_url(self):
        return '%s%s' % (settings.DOMINIO_URL, reverse('users_register_activate', kwargs={'slug': self.slug}))
    