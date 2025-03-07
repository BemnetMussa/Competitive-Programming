class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        
        deck.sort()

        revealed = [0] * len(deck)
        cards = deque(range(len(deck)))

        for num in deck:
            i = cards.popleft()

            revealed[i] = num

            if cards:
                cards.append(cards.popleft())

        
        return revealed