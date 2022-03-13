Arhitectura sistemelor de calcul - Multithreading in Python



Producer:
In producer fac o bucla infinita pentru a produce continuu elemente si iterez prin lista de produse. Public prin metoda publish produsul respectiv de un numar de ori egal cu cantitatea ceruta daca este loc liber, iar daca nu, astept un numar de secunde.

Consumer:
In consumer iterez prin fiecare cos de cumparaturi si le dau cate un id cu metoda new_cart apoi iterez prin fiecare produs din cosul de cumparaturi si 
verific ce operatie trebuie sa fac si de cate ori. Dupa ce am trecut prin fiecare produs/operatie din cosul de cumparaturi, plasez comanda.

Marketplace:
Mi-am declarat doua dictionare. Unul de forma id_producator cu lista de produse si celalalt -> id_cart cu lista de produse. In register_producer si
in new_cart incrementez un contor si intorc valoarea lui. In publish
verific daca lungimea listei de produse pentru producatorul respectiv este
mai mare decat limita maxima si returnez false, daca este mai mare si daca nu adaug produsul in dictionar la producatorul respectiv. In add_cart iterez prin fiecare producator si verific daca produsul care se doreste a fi cumparat este in lista vreunui producator sau nu. Daca da, adaug produsul in dictionarul de cosuri si il scot din lista producatorului 
respectiv. Altfel intorc False. In remove cart, daca produsul se afla in cos, il scot si il adaug inapoi in lista producatorului respectiv din dictionar.
