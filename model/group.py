from sys import maxsize


class Group:
    def __init__(self, name=None, header=None, footer=None, id=None):
        self.name = name
        self.header = header
        self.footer = footer
        self.id = id

    def __repr__(self):
        return "%s:%s" % (self.id, self.name)

    def __eq__(self, other): #для сравнения логически, чтобы сравнивались идентификаторы и имена, а не физическое расположение объетов в ячейках памяти. Параметр other - это объект с которым мы должны сравнитьб текущий объект self.
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name #т.е. теперь будет выполняться сравнение по смыслу, а не по физ. расположению

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

