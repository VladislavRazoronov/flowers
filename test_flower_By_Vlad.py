import flower
import unittest

class TestFlowers(unittest.TestCase):
    """ Test flower module functionality"""
    def test_flowers(self):
        """ Test flower class"""
        tulpan = flower.Tulip('red',8,20)
        self.assertEqual(tulpan.petals, 8, 'Отримано кількість пелюсток')
        tulpan.setcolor('yellow')
        self.assertEqual(tulpan.color, 'yellow', 'Присвоєно колір')
        tulpan.setprice(15)
        self.assertEqual(tulpan.price, 15, 'Присвоєно ціну')
        self.assertIsInstance(tulpan, flower.Flower, 'Тюльпан - квітка')
        self.assertNotIsInstance(tulpan, flower.Rose, 'Тюльпан не троянда')
    
    def test_flower_sets(self):
        """ Test flower set class"""
        romashka = flower.Chamomile('white',20,5)
        flowers = flower.FlowerSet(romashka, 21)
        self.assertIsInstance(flowers, flower.FlowerSet, 'Квітки це набір квіток')
        self.assertNotIsInstance(flowers, flower.Flower, 'Квітки не є квіткою')
        self.assertEqual(flowers.price(), 105, 'Пораховано ціну')
        flowers.flower.setprice(10)
        self.assertEqual(flowers.price(), 210, 'Перераховано ціну')
    
    def test_bouquet(self):
        """ Test Bouquet class"""
        troyanda1 = flower.Rose('red', 10, 20)
        troyanda2 = flower.Rose('pink', 10, 20)
        romashka = flower.Chamomile('white', 20, 5)
        tulpan = flower.Tulip('orange', 8, 15)
        flowers1 = flower.FlowerSet(troyanda1, 3)
        flowers2 = flower.FlowerSet(troyanda2, 1)
        flowers3 = flower.FlowerSet(romashka, 15)
        flowers4 = flower.FlowerSet(tulpan, 5)
        bouquet = flower.Bouquet([flowers1, flowers2, flowers3, flowers4])
        self.assertIsInstance(bouquet, flower.Bouquet, "Об'єкт є букетом")
        self.assertNotIsInstance(bouquet, flower.FlowerSet, 'Не набір квіток')
        self.assertEqual(bouquet.price(), 230)
        bouquet.flowers[1].flower.setprice(30)
        self.assertEqual(bouquet.price(), 240)
        self.assertEqual(bouquet.flowers[0].flower.color, 'red', 'Перевірка кольору')

if __name__ == "__main__":
    unittest.main()