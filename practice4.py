from threading import Thread,Lock
import time
class check_cards():
    def __init__(self,card) -> None:
        self._lock=Lock()
        self._cards_on_hands=[]
    
    def turn(self,card):
        self._lock.acquire()
        try:
            self._cards_on_hands.append(card.pop())
            time.sleep(0.01)
        finally:
            self._lock.release()

class draw(Thread):
    def __init__(self,card) :
        super().__init__()
        self._check_cards=check_cards()
        self._card=card
        self._card_on_hands=self._check_cards._cards_on_hands
    
    def run(self) :
        return self._check_cards.turn(self._card)
    



def main():
    cards = [i+j for i in "ABCD" for j in range (1,14)]
    card=check_cards()
    person = []
    for p in range (2):
        t=draw(card.turn(cards))
        person.append(t)
        t.start()
    for t in person :
        t.join()
    print(t._card_on_hands)

