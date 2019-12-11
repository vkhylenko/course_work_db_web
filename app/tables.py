from flask_table import Table, Col, LinkCol
 
class ResultsE(Table):
    id = Col('Id', show=False)
    #name = Col('Ski Resort')
    name = LinkCol("Name Location", endpoint="europe", url_kwargs=dict(id_='id'), attr='name')
    country = Col('Country')
    altitude = Col('Altitude')


class ResultsN(Table):
    id = Col('Id', show=False)
    #name = Col('Ski Resort')
    name = LinkCol("Name Location", endpoint="namerica", url_kwargs=dict(id_='id'), attr='name')
    country = Col('Country')
    altitude = Col('Altitude')

class ResultsS(Table):
    id = Col('Id', show=False)
    #name = Col('Ski Resort')
    name = LinkCol("Name Location", endpoint="samerica", url_kwargs=dict(id_='id'), attr='name')
    country = Col('Country')
    altitude = Col('Altitude')

class ResultsO(Table):
    id = Col('Id', show=False)
    #name = Col('Ski Resort')
    name = LinkCol("Name Location", endpoint="othworld", url_kwargs=dict(id_='id'), attr='name')
    country = Col('Country')
    altitude = Col('Altitude')

class Finder(Table):
    id = Col('Id', show=False)
    #name = Col('Ski Resort')
    name = LinkCol("Name Location", endpoint="finder_res", url_kwargs=dict(id_='id'), attr='name')
    country = Col('Country')
    altitude = Col('Altitude')
