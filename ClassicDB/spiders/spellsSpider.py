import scrapy
from selenium import webdriver

class SpellsSpider(scrapy.Spider):
    name = 'spells-spider'
    start_urls = ['https://classicdb.ch/?spells=7.11']
    #carrega a pagina no phantomjs
    def __init__(self, *args, **kwargs):
        self.driver = webdriver.PhantomJS()
        super(SpellsSpider, self).__init__(*args, **kwargs)

    def parse(self, response):
        #pega a pagina ja carregada pelo phantomjs
        self.driver.get(response.url)
        sel = scrapy.Selector(text = self.driver.page_source)
        #faz o scraping utilizando a classe do elemento já criado (para verificar a classe do elemento é só inspecionar a pagina no navegador)
        for spell in sel.css('.listview-mode-default'):
            yield {
                'id' : spell.css('a::attr(href)').extract()
            }