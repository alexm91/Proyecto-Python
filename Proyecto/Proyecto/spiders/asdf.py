import scrapy

nombre_archivo = 'hoteles.txt'

class QuotesSpider(scrapy.Spider):
    name = "spider_participantes"
    start_urls = [
        'file:///C:/Users/alebu/Documents/EPN%20FIS/Workspace/PythonPycharm/Proyecto-Python/WEB/HotelManta1.html',
        'file:///C:/Users/alebu/Documents/EPN%20FIS/Workspace/PythonPycharm/Proyecto-Python/WEB/HotelManta2.html',
        'file:///C:/Users/alebu/Documents/EPN%20FIS/Workspace/PythonPycharm/Proyecto-Python/WEB/HotelManta3.html'

    ]

    def parse(self, response):

        for i in response.css('.item__flex-column'):
            nombres = i.css('.name__copytext::text').extract()
            precios = i.css('.price_min::text').extract()
            rating = i.css('.rating-box__value::text').extract()
            yield {'Nombres': nombres, 'Precios': precios, 'Rating': rating}

