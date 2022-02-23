# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MercadoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #DATOS DE LA OFERTA
    titulo = scrapy.Field()
    descripcion = scrapy.Field()
    requisitos = scrapy.Field()
    key_words = scrapy.Field()

    #DATOS DE LA EMPRESA
    empresa = scrapy.Field()
    acerca_empresa = scrapy.Field()
    rating = scrapy.Field()

    pass
