class RecommendationEngine:
    mood_to_recipe_tags = {
        'happy': ['light', 'sweet'],
        'sad': ['comfort', 'warm'],
        'angry': ['spicy', 'bold'],
        'neutral': ['balanced'],
        'excited': ['fruity', 'fresh']
    }

    def get_recipes_for_mood(self, mood):
        tags = self.mood_to_recipe_tags.get(mood, [])
        # Mocked recipe retrieval logic
        recipes = [
            {'id': 1, 'name': 'Sweet Berry Salad', 'tags': ['light', 'sweet']},
            {'id': 2, 'name': 'Spicy Chili', 'tags': ['spicy', 'bold']},
            {'id': 3, 'name': 'Warm Soup', 'tags': ['comfort', 'warm']}
        ]
        return [recipe for recipe in recipes if any(tag in tags for tag in recipe['tags'])]

# Example usage:
# engine = RecommendationEngine()
# recommended = engine.get_recipes_for_mood('happy')
# print(recommended)
