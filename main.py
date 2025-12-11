import json

# Laad het JSON-bestand
with open("story.json", "r", encoding="utf-8") as f:
    story = json.load(f)

def play_game():
    current_scene = "bibliotheek"
    
    while True:
        scene = story[current_scene]
        print("\n" + scene["text"] + "\n")
        
        if not scene["choices"]:
            print("🎉 Het avontuur is afgelopen. Bedankt voor het spelen!")
            break
        
        print("Wat wil je doen?")
        choices_list = list(scene["choices"].keys())
        for idx, choice in enumerate(choices_list, 1):
            print(f"{idx}. {choice}")
        
        user_input = input("> ")
        if user_input.isdigit() and 1 <= int(user_input) <= len(choices_list):
            current_scene = scene["choices"][choices_list[int(user_input)-1]]
        else:
            print("Ongeldige keuze, probeer opnieuw.")

if __name__ == "__main__":
    play_game()
