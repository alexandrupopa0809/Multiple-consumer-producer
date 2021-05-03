"""
This module represents the Consumer.

Computer Systems Architecture Course
Assignment 1
March 2021
"""

from threading import Thread
import time


class Consumer(Thread):
    """
    Class that represents a consumer.
    """

    def __init__(self, carts, marketplace, retry_wait_time, **kwargs):
        """
        Constructor.

        :type carts: List
        :param carts: a list of add and remove operations

        :type marketplace: Marketplace
        :param marketplace: a reference to the marketplace

        :type retry_wait_time: Time
        :param retry_wait_time: the number of seconds that a producer must wait
        until the Marketplace becomes available

        :type kwargs:
        :param kwargs: other arguments that are passed to the Thread's __init__()
        """
        Thread.__init__(self, **kwargs)
        self.carts = carts
        self.marketplace = marketplace
        self.retry_wait_time = retry_wait_time

    def run(self):
        for cart in self.carts:
            #initializez fiecare cos de cumparaturi cu un id
            cart_id = self.marketplace.new_cart()
            for item in cart:
                qty = 0
                #cat timp nu s-a ajuns la cantitatea ceruta pentru produs
                while qty < item['quantity']:
                    if item['type'] == 'add':
                        products_added = self.marketplace.add_to_cart(cart_id, item['product'])
                        if products_added:
                            #incrementez contorul pentru a adauga cantitatea ceruta
                            qty += 1
                        else:
                            #daca nu s-a gasit produsul respectiv, astept
                            time.sleep(self.retry_wait_time)
                    else:
                        self.marketplace.remove_from_cart(cart_id, item['product'])
                        #incrementez contorul pentru a sterge cantitate ceruta
                        qty += 1
            self.marketplace.place_order(cart_id)
