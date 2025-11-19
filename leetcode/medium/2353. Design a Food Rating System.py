# O(log(n+m)) time and O(n+m) space, n = len(foods), m = number of changeRating calls
# link: https://leetcode.com/problems/design-a-food-rating-system/

from heapq import heappop, heappush, heapify

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_to_cuisine = {}
        self.food_to_rating = {}  # to store ratings, and detect outdated ratings
        self.cuisine_heaps = {}

        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.food_to_cuisine[food] = cuisine
            self.food_to_rating[food] = rating
            if cuisine not in self.cuisine_heaps:
                self.cuisine_heaps[cuisine] = []
            self.cuisine_heaps[cuisine].append([-rating, food])

        for cuisine in self.cuisine_heaps.keys():
            heapify(self.cuisine_heaps[cuisine])

    def changeRating(self, food: str, newRating: int) -> None:
        # identify current rating
        cuisine = self.food_to_cuisine[food]
        self.food_to_rating[food] = newRating
        heap = self.cuisine_heaps[cuisine]
        heappush(heap, [-newRating, food])

    def highestRated(self, cuisine: str) -> str:
        heap = self.cuisine_heaps[cuisine]
        while heap:
            rating, food = heap[0]
            if -rating != self.food_to_rating[food]:
                heappop(heap)
                continue
            return food


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
