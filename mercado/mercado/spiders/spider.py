import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.exceptions import CloseSpider
from mercado.items import MercadoItem

class MercadoSpider(CrawlSpider):
    name = 'mercado'
    item_count = 0
    allowed_domain = ['www.computrabajo.com.pe']
    start_urls = ['https://www.computrabajo.com.pe/trabajo-de-sistemas?p=2']

    rules ={
        #primera regla correponde a boton siguiente
        Rule(LinkExtractor(allow=(), restrict_xpaths=('//nav[@class="pag_numeric"]/a[7]'))),
        #la segunda regla correponde a link de cada producto
        Rule(LinkExtractor(allow=(), restrict_xpaths=('//div[@id="p_ofertas"]/article/div/h1/a')),
             callback='parse_item', follow=False)
    }

    def parse_item(self, response):
        ml_item = MercadoItem()
        #DATSO DE OFERTAS LABORALES
        ml_item['titulo'] = response.xpath('normalize-space(//html/body/main/div[1]/h1/text())').extract()
        ml_item['descripcion'] = response.xpath('normalize-space(//div[@class="box_border menu_top dFlex"]/div/div[2]/div/p[1]/text())').extract()
        ml_item['requisitos'] = response.xpath('normalize-space(//div[@class="box_border menu_top dFlex"]/div/div[2]/div/ul)').extract()
        ml_item['key_words'] = response.xpath('normalize-space(//div[@class="box_border menu_top dFlex"]/div/div[2]/div/p[3]/text())').extract()

        #DATOS DE LA EMPRESA
        ml_item['empresa'] = response.xpath('normalize-space(//html/body/main/div[1]/p/text())').extract()
        ml_item['acerca_empresa'] = response.xpath('normalize-space(//html/body/main/div[2]/div/div[2]/div[4]/p[2]/text())').extract()
        ml_item['rating'] = response.xpath('normalize-space(//html/body/main/div[2]/div/div[2]/div[5]/div[1]/div/div[1]/div/div/p[1]/text())').extract()

        self.item_count += 1
        if self.item_count > 5:
            raise CloseSpider('item_exceeded')
        yield ml_item