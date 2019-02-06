import scrapy

class QuotesSpider(scrapy.Spider):
    name = "spider_"
    start_urls = [
            'https://www.plusvalia.com/casas-en-venta-en-quito.html',
            'https://www.plusvalia.com/casas-en-venta-en-quito-pagina-2.html',
            'https://www.plusvalia.com/casas-en-venta-en-quito-pagina-3.html',
            'https://www.plusvalia.com/casas-en-venta-en-quito-pagina-4.html',
            'https://www.plusvalia.com/casas-en-venta-en-quito-pagina-5.html',
            'https://www.plusvalia.com/casas-en-venta-en-quito-pagina-6.html',
            'https://www.plusvalia.com/casas-en-venta-en-quito-pagina-7.html',
            'https://www.plusvalia.com/casas-en-venta-en-quito-pagina-8.html',
            'https://www.plusvalia.com/casas-en-venta-en-quito-pagina-9.html',
            'https://www.plusvalia.com/casas-en-venta-en-quito-pagina-10.html',

    ]

    def parse(self, response):
        resultado = response.xpath('//*[@id="avisos-content"]')


        for i, casas in enumerate(resultado):
            lugares = casas.xpath('//div/div/div/div/span/span/text()').extract()
            disponibles = casas.css(
                'div.aviso-data.aviso-data--right > div > ul > li:nth-child(1) > b::text').extract()
            precio = casas.css('.aviso-data-price-value::text').extract()

            yield {'index': i, 'title': precio}