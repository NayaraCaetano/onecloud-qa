# -*- coding: utf-8 -*-

from lettuce import step, world


def pagina_eh_valida(nome):
    assert world.pages.get(nome) is not None, 'A pagina ' + nome + ' nao esta mapeada'


@step(u'Dado que estou na p[áa]gina "([^"]*)"')
@step(u'.* visitar a p[áa]gina "([^"]*)"')
@step(u'.* visito a p[áa]gina "([^"]*)"')
@step(u'.* acesso a p[áa]gina "([^"]*)"')
@step(u'.* acessar a p[áa]gina "([^"]*)"')
def eu_estou_em_alguma_url(step, nome):
    pagina_eh_valida(nome)
    world.browser.visit(world.base_url + world.pages[nome])


@step(u'.* tentar acessar o sistema com as credenciais "([^"]*)" e "([^"]*)"')
@step(u'.* tento acessar o sistema com as credenciais "([^"]*)" e "([^"]*)"')
def tentar_acessar_o_sistema_com_as_credenciais_group1_e_group2(step, group1, group2):
    eu_estou_em_alguma_url(step, 'logout_admin')
    eu_estou_em_alguma_url(step, 'login_admin')
    login(step, group1, group2)


def login(step, group1, group2):
    world.browser.fill('username', group1)
    world.browser.fill('password', group2)
    world.browser.find_by_value('Log in').click()


@step(u'.* devo estar na p[áa]gina "([^"]*)"$')
@step(u'.* devo permanecer na p[áa]gina "([^"]*)"$')
@step(u'.* devo ver a p[áa]gina "([^"]*)"$')
def eu_devo_ver_alguma_pagina(step, nome):
    pagina_eh_valida(nome)
    current_url = (world.browser.url).split('?')[0]
    full_url = (world.base_url + world.pages[nome])
    assert current_url == full_url, 'url atual: "%s" / url esperada: "%s"' % (current_url, full_url)


@step(u'Então devo ver a mensagem de erro "([^"]*)"')
@step(u'.*[^não] devo ver a mensagem de erro "([^"]*)"')
def eu_devo_ver_a_mensagem_de_erro_contendo_group1(step, group1):
    world.browser.is_element_visible_by_css('.errornote', wait_time=5)
    error_elements = world.browser.find_by_css('.errornote')
    for element in error_elements:
        if element.visible:
            if group1 in element.text:
                return True
    assert False
