# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items, max_quality=50, min_quality=0, legendary_quality=80):
        self.items = items
        self.max_quality = max_quality
        self.min_quality = min_quality
        self.legendary_quality = legendary_quality

    def get_items(self):
        return self.items

    def update_quality(self):
        for item in self.items:
            if item.name == "Aged Brie":
                self.update_aged_brie(item)
            elif item.name == "Sulfuras, Hand of Ragnaros":
                self.update_sulfuras(item)
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                self.update_backstage_passes(item)
            elif item.name == "Conjured Mana Cake":
                self.update_conjured(item)
            else:
                self.update_default(item)

    def update_default(self, item):

        if item.quality > self.min_quality:
            item.quality -= 1

            if item.sell_in <= 0:
                item.quality -= 1

        item.sell_in -= 1

    def update_aged_brie(self, item):

        if item.quality < self.max_quality:
            item.quality = item.quality + 1

            if item.sell_in <= 0:
                item.quality += 1

        item.sell_in -= 1

    # actualizar 'Sulfuras' - Legendary item
    def update_sulfuras(self, item):
        pass

    def update_backstage_passes(self, item):

        if 10 >= item.sell_in > 5:
            item.quality += 2
        elif 5 >= item.sell_in > 0:
            item.quality += 3
        elif item.sell_in <= 0:
            item.quality = 0
        else:
            item.quality += 1

        if item.quality > self.max_quality:
            item.quality = self.max_quality

        item.sell_in -= 1

    def update_conjured(self, item):

        if item.quality > self.min_quality:
            item.quality -= 2

            if item.sell_in <= 0:
                item.quality -= 2

        if item.quality < self.min_quality:
            item.quality = self.min_quality

        item.sell_in -= 1

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)