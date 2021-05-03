"""
This module represents the Producer.

Computer Systems Architecture Course
Assignment 1
March 2021
"""

from threading import Thread
import time

class Producer(Thread):
    """
    Class that represents a producer.
    """

    def __init__(self, products, marketplace, republish_wait_time, **kwargs):
        """
        Constructor.

        @type products: List()
        @param products: a list of products that the producer will produce

        @type marketplace: Marketplace
        @param marketplace: a reference to the marketplace

        @type republish_wait_time: Time
        @param republish_wait_time: the number of seconds that a producer must
        wait until the marketplace becomes available

        @type kwargs:
        @param kwargs: other arguments that are passed to the Thread's __init__()
        """
        Thread.__init__(self, **kwargs)
        self.products = products
        self.marketplace = marketplace
        self.republish_wait_time = republish_wait_time
        self.id_prod = self.marketplace.register_producer()

    def run(self):
        #bucla infinita pentru a produce continuu
        while True:
            #pentru fiecare produs
            for prod, quant, time_to_sleep in self.products:
                #initializez contorul cu 0 la fiecare produs
                prd = 0
                #cat timp nu s-a produs cantitatea dorita de produsul respectiv
                while prd < quant:
                    products_published = self.marketplace.publish(self.id_prod, prod)
                    if products_published:
                        time.sleep(time_to_sleep)
                        prd += 1
                    else:
                        #coada este plina si astept timpul respectiv
                        time.sleep(self.republish_wait_time)
        