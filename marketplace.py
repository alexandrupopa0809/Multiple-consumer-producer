"""
This module represents the Marketplace.

Computer Systems Architecture Course
Assignment 1
March 2021
"""
import threading
from threading import Lock

class Marketplace:
    """
    Class that represents the Marketplace. It's the central part of the implementation.
    The producers and consumers use its methods concurrently.
    """
    def __init__(self, queue_size_per_producer):
        """
        Constructor

        :type queue_size_per_producer: Int
        :param queue_size_per_producer: the maximum size of a queue associated with each producer
        """
        self.queue_size_per_producer = queue_size_per_producer
        self.id_prod = 0 #id-ul producatorului
        self.cart_id = 0 #id-ul cosului de cumparaturi
        self.producers_dict = {} #dictionar de forma id -> lista produse
        self.carts_dict = {} #dictionar de forma id -> lista produse
        self.lock_id_prod = Lock() #lock pentru adunarea de la id_prod
        self.lock_id_cart = Lock() #lock pentru adunarea de la id_cart
        self.lock_add = Lock() #lock pentru operatia de remove din add

    def register_producer(self):
        """
        Returns an id for the producer that calls this.
        """
        self.producers_dict[self.id_prod] = []
        with self.lock_id_prod:
            self.id_prod += 1
        return self.id_prod - 1

    def publish(self, producer_id, product):
        """
        Adds the product provided by the producer to the marketplace

        :type producer_id: String
        :param producer_id: producer id

        :type product: Product
        :param product: the Product that will be published in the Marketplace

        :returns True or False. If the caller receives False, it should wait and then try again.
        """
        if len(self.producers_dict[producer_id]) >= self.queue_size_per_producer:
            return False
        self.producers_dict[producer_id].append(product)
        return True

    def new_cart(self):
        """
        Creates a new cart for the consumer

        :returns an int representing the cart_id
        """
        self.carts_dict[self.cart_id] = []
        with self.lock_id_cart:
            self.cart_id += 1
        return self.cart_id - 1

    def add_to_cart(self, cart_id, product):
        """
        Adds a product to the given cart. The method returns

        :type cart_id: Int
        :param cart_id: id cart

        :type product: Product
        :param product: the product to add to cart

        :returns True or False. If the caller receives False, it should wait and then try again
        """
        for i in list(self.producers_dict.keys()):
            if product in self.producers_dict[i]:
                self.carts_dict[cart_id].append(product)
                with self.lock_add:
                    self.producers_dict[i].remove(product)
                return True
        return False

    def remove_from_cart(self, cart_id, product):
        """
        Removes a product from cart.

        :type cart_id: Int
        :param cart_id: id cart

        :type product: Product
        :param product: the product to remove from cart
        """
        for i in list(self.producers_dict.keys()):
            if product in self.carts_dict[cart_id]:
                self.carts_dict[cart_id].remove(product)
                self.producers_dict[i].append(product)
                return

    def place_order(self, cart_id):
        """
        Return a list with all the products in the cart.

        :type cart_id: Int
        :param cart_id: id cart
        """
        for i in self.carts_dict[cart_id][::-1]:
            print(str(threading.currentThread().name) + " bought " + str(i))
            