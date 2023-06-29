#story generator
import random

def generate_random_story(character):
    # List of possible time periods for the story
    time_periods = ["ancient times", "medieval era", "renaissance period", "industrial revolution", "modern day", "future"]

    # List of possible locations for the story
    locations = ["forest", "castle", "beach", "mountain", "city", "cave", "island", "space"]

    # List of possible actions for the story
    actions = ["discovered", "explored", "encountered", "solved", "rescued", "defeated"]

    # Select a random time period, location, and action
    time_period = random.choice(time_periods)
    location = random.choice(locations)
    action = random.choice(actions)

    # Generate the story
    story = f"In {time_period}, {character} embarked on a journey to the {location}. There, they {action} a mysterious artifact. The artifact held great power and posed a new challenge for {character}. Through a series of trials and tribulations, {character} navigated the complexities of the {location}, unraveling its secrets and discovering their own inner strength. In the end, {character} emerged victorious, forever changed by their extraordinary adventure."

    return story

# Example usage:
character = input("Enter a character for the story: ")
story = generate_random_story(character)
print("\nStory:")
print(story)
