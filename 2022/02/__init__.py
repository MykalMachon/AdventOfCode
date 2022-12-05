def get_move_points(move):
    if move == "rock":
        return 1
    if move == "paper":
        return 2
    if move == "scissors":
        return 3


def get_move(input):
    move_map = {
        "A": "rock",
        "B": "paper",
        "C": "scissors",
        "X": "rock",
        "Y": "paper",
        "Z": "scissors"
    }
    return move_map.get(input)


def get_results(row):
    results = {"comp": 0, "you": 0}

    # get players moves
    comp_move = get_move(row[0])
    your_move = get_move(row[2])

    # add baseline move points
    results.update({"comp": results.get('comp') + get_move_points(comp_move)})
    results.update({"you": results.get('you') + get_move_points(your_move)})

    # figure out who won and who should get points
    # I intentionally used update here: wanted to see how the syntax worked
    # I know you can just use [] accessors.

    if comp_move == your_move:
        # draw results
        results.update({"comp": results.get('comp') + 3})
        results.update({"you": results.get('you') + 3})
    elif comp_move == "rock":
        if your_move == "scissors":
            results.update({"comp": results.get('comp') + 6})
        if your_move == "paper":
            results.update({"you": results.get('you') + 6})
    elif comp_move == "paper":
        if your_move == "scissors":
            results.update({"you": results.get('you') + 6})
        if your_move == "rock":
            results.update({"comp": results.get('comp') + 6})
    elif comp_move == "scissors":
        if your_move == "paper":
            results.update({"comp": results.get('comp') + 6})
        if your_move == "rock":
            results.update({"you": results.get('you') + 6})
    return results


def get_outcome(input):
    outcome_map = {
        "X": "lose",
        "Y": "draw",
        "Z": "win",
    }
    return outcome_map.get(input)


def get_results_part_two(row):
    results = {"comp": 0, "you": 0}

    # get comp move and outcome
    comp_move = get_move(row[0])
    outcome = get_outcome(row[2])

    # baseline move points for the computer
    results["comp"] += get_move_points(comp_move)

    if comp_move == "rock":
        if outcome == "win":
            results["comp"] += 0
            results["you"] += 6 + get_move_points('paper')
        if outcome == "draw":
            results["comp"] += 3
            results["you"] += 3 + get_move_points('rock')
        if outcome == "lose":
            results["comp"] += 6
            results["you"] += get_move_points('scissors')
    elif comp_move == "paper":
        if outcome == "win":
            results["comp"] += 0
            results["you"] += 6 + get_move_points('scissors')
        if outcome == "draw":
            results["comp"] += 3
            results["you"] += 3 + get_move_points('paper')
        if outcome == "lose":
            results["comp"] += 6
            results["you"] += get_move_points('rock')
    elif comp_move == "scissors":
        if outcome == "win":
            results["comp"] += 0
            results["you"] += 6 + get_move_points('rock')
        if outcome == "draw":
            results["comp"] += 3
            results["you"] += 3 + get_move_points('scissors')
        if outcome == "lose":
            results["comp"] += 6
            results["you"] += get_move_points('paper')
    return results


def load_data():
    with open('./input.txt', 'r') as file:
        raw_data = file.readlines()
        data = [line.strip('\n') for line in raw_data]
        return data


if __name__ == "__main__":
    data = load_data()

    # part one: get your total score given the strategy guide
    total_scores_p1 = {"comp": 0, "you": 0}
    for rps in data:
        rps_results = get_results(rps)
        total_scores_p1["comp"] += rps_results["comp"]
        total_scores_p1["you"] += rps_results["you"]

    print(f"part 1: Your total points are: {total_scores_p1['you']}")

    # part two: get your total score given the new interpretation
    total_scores_p2 = {"comp": 0, "you": 0}
    for rps in data:
        rps_results = get_results_part_two(rps)
        total_scores_p2["comp"] += rps_results["comp"]
        total_scores_p2["you"] += rps_results["you"]

    print(f"part 1: Your total points are: {total_scores_p2['you']}")