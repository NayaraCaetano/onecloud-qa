# -*- coding: utf-8 -*-

import re

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


@step(u'.*[^não] devo ver na linha da tabela os conte[úu]dos: (.+)$')
@step(u'.* eu devo ver na linha da tabela os contéudos: (.+)$')
@step(u'.*[^não] devo ver na linha da tabela o conte[úu]do: (.+)$')
@step(u'.*[^não] devo ver na linha da tabela o conte[úu]do (.+)$')
def entao_eu_devo_ver_na_linha_da_tabela_os_conteudos(step, group1):
    assert encontrar_elemento_por_x_conteudos('tr', processa_group(group1), '')


@step(u'.*[^não] devo ver na primeira linha do corpo da tabela os conte[úu]dos: (.+)$')
def entao_eu_devo_ver_na_primeira_linha_do_corpo_da_tabela_os_conteudos(step, group1):
    assert encontrar_elemento_por_x_conteudos('tr:nth(1)', processa_group(group1), '')


@step(u'.* a tabela deve ter "([^"]*)" linhas')
def entao_a_tabela_deve_ter_group1_linhas(step, group1):
    resultado = world.browser.evaluate_script('$("tr")')
    assert len(resultado) == int(group1), 'resultado: "%s" / esperado: "%s"' % (len(resultado), int(group1))


@step(u'.* clicar no link "([^"]*)"$')
@step(u'.* clico no link "([^"]*)"$')
def e_clico_no_link_group1(step, group1):
    hrefs = encontrar_link_por_texto(group1)
    hrefs[0].click()


@step(u'.*[^não] tenho cadastro do serviço "([^"]*)", "([^"]*)", cpu "([^"]*)", memória "([^"]*)", disco "([^"]*)" e preço "([^"]*)"')
def e_tenho_cadastro_do_servico_group1_group2_cpu_group3_memoria_group4_disco_group5_e_preco_group6(step, group1, group2, group3, group4, group5, group6):
    from onecloud.models import Provider, Service
    provedor, _ = Provider.objects.get_or_create(name=group2)
    Service.objects.get_or_create(
        name=group1,
        provider=provedor,
        cpu=group3,
        memory=group4,
        disk=group5,
        price=group6
    )


def encontrar_elemento_por_x_conteudos(parent_seletor, conteudos, descendant_seletor):
    seletor_inicio = u'$("' + parent_seletor + ''
    seletor_final = u':visible' + descendant_seletor + '")'
    seletor_meio = u''

    for conteudo in conteudos:
        seletor_meio = seletor_meio + u':contains(\'' + conteudo + '\')'

    seletor = seletor_inicio + seletor_meio + seletor_final

    return world.browser.evaluate_script(seletor)


def processa_group(super_group):
    r_get_aspas = re.compile('"([^"]*)"')
    groups = r_get_aspas.findall(super_group)
    groups = [group.replace("''", '"') for group in groups]
    group_final = []
    for group in groups:
        group_final.append(group)
    return group_final


def encontrar_link_por_texto(texto):
    hrefs = [href for href in encontrar_elemento_por_x_conteudos('[href]', [texto], '') if (href.text.lower().split("\n")[0] == texto.lower())]
    if hrefs:
        return hrefs
