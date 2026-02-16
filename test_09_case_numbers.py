from ds_test_utils import (
    run_program, assert_prompts,
    extract_age, extract_foods_list, extract_foods_count, extract_unique_foods,
    extract_profile_dict, extract_summary_tuple
)

def test_09_case_numbers():
    out = run_program('Leo', 'Kananga', 1999, 2026, '7up, coke, 7up')
    assert_prompts(out)

    assert extract_age(out) == 27

    assert extract_foods_list(out) == ['7up', 'coke', '7up']
    assert extract_foods_count(out) == 3
    assert extract_unique_foods(out) == 2

    assert extract_profile_dict(out) == {'name': 'Leo', 'city': 'Kananga', 'age': 27, 'foods': ['7up', 'coke', '7up']}
    assert extract_summary_tuple(out) == ('Leo', 27, 'Kananga')
