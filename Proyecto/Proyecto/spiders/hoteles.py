import scrapy

nombre_archivo = 'hoteles.txt'

class QuotesSpider(scrapy.Spider):
    name = "spider_hoteles"
    start_urls = [
        'file:///C:/Users/alebu/Documents/EPN%20FIS/Workspace/PythonPycharm/Proyecto-Python/WEB/HotelAtacames1.html',
        'file:///C:/Users/alebu/Documents/EPN%20FIS/Workspace/PythonPycharm/Proyecto-Python/WEB/HotelBallenita1.html',
        'file:///C:/Users/alebu/Documents/EPN%20FIS/Workspace/PythonPycharm/Proyecto-Python/WEB/HotelBallenita2.html',
        'file:///C:/Users/alebu/Documents/EPN%20FIS/Workspace/PythonPycharm/Proyecto-Python/WEB/HotelCanoa.html',
        'file:///C:/Users/alebu/Documents/EPN%20FIS/Workspace/PythonPycharm/Proyecto-Python/WEB/HotelesBahíadeCaráquez.html',
        'file:///C:/Users/alebu/Documents/EPN%20FIS/Workspace/PythonPycharm/Proyecto-Python/WEB/HotelManta1.html',
        'file:///C:/Users/alebu/Documents/EPN%20FIS/Workspace/PythonPycharm/Proyecto-Python/WEB/HotelManta2.html',
        'file:///C:/Users/alebu/Documents/EPN%20FIS/Workspace/PythonPycharm/Proyecto-Python/WEB/HotelMompiche.html',
        'file:///C:/Users/alebu/Documents/EPN%20FIS/Workspace/PythonPycharm/Proyecto-Python/WEB/HotelMontañita1.html',
        'file:///C:/Users/alebu/Documents/EPN%20FIS/Workspace/PythonPycharm/Proyecto-Python/WEB/HotelMontañita2.html',
        'file:///C:/Users/alebu/Documents/EPN%20FIS/Workspace/PythonPycharm/Proyecto-Python/WEB/HotelMontañita3.html',
        'file:///C:/Users/alebu/Documents/EPN%20FIS/Workspace/PythonPycharm/Proyecto-Python/WEB/HotelPlayas1.html',
        'file:///C:/Users/alebu/Documents/EPN%20FIS/Workspace/PythonPycharm/Proyecto-Python/WEB/HotelSalinas1.html',
        'file:///C:/Users/alebu/Documents/EPN%20FIS/Workspace/PythonPycharm/Proyecto-Python/WEB/HotelSalinas2.html',
        'file:///C:/Users/alebu/Documents/EPN%20FIS/Workspace/PythonPycharm/Proyecto-Python/WEB/HotelTonsupa.html',
    ]

    def parse(self, response):

        for i in response.css('.item__flex-column'):
            nombres = i.css('.name__copytext::text').extract()
            precios = i.css('.price_min::text').extract()
            rating = i.css('.rating-box__value::text').extract()
            pagina = i.css('.item__deal-best-ota::text').extract()
            ubicacion = i.css('.location-details::text').extract()
            yield {'Nombres': nombres, 'Precios': precios, 'Rating': rating, 'Ubicacion': ubicacion, 'Pagina': pagina}

