from main import calculate_points_for_word, alphabet, assign_seven_tiles_from_alphabet

def test_points_for_word():
    assert calculate_points_for_word('bag') == 6
    assert calculate_points_for_word('GUARDIAN') == 10
    assert calculate_points_for_word('') == 0


def test_assign_seven_tiles():
    assert len(assign_seven_tiles_from_alphabet(alphabet)) == 7
    assert isinstance(assign_seven_tiles_from_alphabet(alphabet), list)
    hand_one = assign_seven_tiles_from_alphabet(alphabet)
    hand_two = assign_seven_tiles_from_alphabet(alphabet)
    assert hand_one != hand_two


