from ds_test_utils import (
    run_program, assert_prompts,
    extract_age, extract_foods_list, extract_foods_count, extract_unique_foods,
    extract_profile_dict, extract_summary_tuple
)

def test_10_case_multiword():
    out = run_program('Ali', 'Tshikapa', 1950, 2026, 'fried rice, grilled fish, fried rice')
    assert_prompts(out)

    assert extract_age(out) == 76

    assert extract_foods_list(out) == ['fried rice', 'grilled fish', 'fried rice']
    assert extract_foods_count(out) == 3
    assert extract_unique_foods(out) == 2

    assert extract_profile_dict(out) == {'name': 'Ali', 'city': 'Tshikapa', 'age': 76, 'foods': ['fried rice', 'grilled fish', 'fried rice']}
    assert extract_summary_tuple(out) == ('Ali', 76, 'Tshikapa')
