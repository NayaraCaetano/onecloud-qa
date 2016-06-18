# coding: utf-8

import factory

from django.test import TestCase
from django.contrib.auth.models import User
from faker import Faker
from rest_framework.test import APIClient

from onecloud.models import Provider, Service

faker = Faker('pt_BR')


class BaseTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()

    def _cria_usuario(self, **kwargs):
        return UsuarioFactory.create(**kwargs)

    def _cria_provider(self, **kwargs):
        return ProviderFactory.create(**kwargs)

    def _cria_service(self, **kwargs):
        return ServiceFactory.create(**kwargs)


class UsuarioFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = faker.sha1()


class ProviderFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Provider

    name = factory.LazyAttribute(lambda obj: '{0}'.format(faker.word()))


class ServiceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Service

    name = faker.text()
    provider = factory.SubFactory(ProviderFactory)
    cpu = faker.random_number()
    memory = faker.random_number()
    disk = faker.random_number()
    price = faker.random_int()
