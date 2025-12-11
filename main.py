import json

with open("story.json", "r", encoding="utf-8") as f:
    story = json.load(f)

player = {
    "inventory": [],
    "flags": {}
}

def can_show_choice(choice):
    if "require_item" in choice:
        if choice["require_item"] not in player["inventory"]:
            return False
    if "require_flag" in choice:
        if choice["require_flag"] not in player["flags"]:
            return False
    return True

def apply_actions(actions):
    if not actions:
        return
    if "add_item" in actions:
        item = actions["add_item"]
        if item not in player["inventory"]:
            player["inventory"].append(item)
    if "remove_item" in actions:
        item = actions["remove_item"]
        if item in player["inventory"]:
            player["inventory"].remove(item)
    if "set_flag" in actions:
        flag = actions["set_flag"]
        player["flags"][flag] = True
    if "remove_flag" in actions:
        flag = actions["remove_flag"]
        if flag in player["flags"]:
            del player["flags"][flag]

def play_game():
    current_scene = "bibliotheek"

    while True:
        scene = story[current_scene]
        print("\n" + scene["text"] + "\n")

        apply_actions(scene.get("actions"))

        choices = []

        for label, data in scene["choices"].items():
            if isinstance(data, str):
                choices.append((label, {"to": data}))
            else:
                if can_show_choice(data):
                    choices.append((label, data))

        if not choices:
            print("🎉 Einde avontuur.")
            break

        for i, (label, _) in enumerate(choices, 1):
            print(f"{i}. {label}")

        user_input = input("> ")
        if user_input.isdigit() and 1 <= int(user_input) <= len(choices):
            _, choice_data = choices[int(user_input)-1]
            apply_actions(choice_data)
            current_scene = choice_data["to"]
        else:
            print("Ongeldige keuze.")

play_game()
