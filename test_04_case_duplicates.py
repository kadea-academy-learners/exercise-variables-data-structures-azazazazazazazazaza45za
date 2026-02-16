from ds_test_utils import (
    run_program, assert_prompts,
    extract_age, extract_foods_list, extract_foods_count, extract_unique_foods,
    extract_profile_dict, extract_summary_tuple
)

def test_04_case_duplicates():
    out = run_program('Sarah', 'Bukavu', 1985, 2026, 'tea, tea, tea')
    assert_prompts(out)

    assert extract_age(out) == 41

    assert extract_foods_list(out) == ['tea', 'tea', 'tea']
    assert extract_foods_count(out) == 3
    assert extract_unique_foods(out) == 1

    assert extract_profile_dict(out) == {'name': 'Sarah', 'city': 'Bukavu', 'age': 41, 'foods': ['tea', 'tea', 'tea']}
    assert extract_summary_tuple(out) == ('Sarah', 41, 'Bukavu')
