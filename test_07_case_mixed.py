from ds_test_utils import (
    run_program, assert_prompts,
    extract_age, extract_foods_list, extract_foods_count, extract_unique_foods,
    extract_profile_dict, extract_summary_tuple
)

def test_07_case_mixed():
    out = run_program('Yann', 'Beni', 1960, 2026, 'Chicken, fish, Chicken')
    assert_prompts(out)

    assert extract_age(out) == 66

    assert extract_foods_list(out) == ['Chicken', 'fish', 'Chicken']
    assert extract_foods_count(out) == 3
    assert extract_unique_foods(out) == 2

    assert extract_profile_dict(out) == {'name': 'Yann', 'city': 'Beni', 'age': 66, 'foods': ['Chicken', 'fish', 'Chicken']}
    assert extract_summary_tuple(out) == ('Yann', 66, 'Beni')
