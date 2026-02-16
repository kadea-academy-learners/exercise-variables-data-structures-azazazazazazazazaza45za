from ds_test_utils import (
    run_program, assert_prompts,
    extract_age, extract_foods_list, extract_foods_count, extract_unique_foods,
    extract_profile_dict, extract_summary_tuple
)

def test_03_case_three():
    out = run_program('Marc', 'Goma', 2010, 2026, 'mango,banana,orange')
    assert_prompts(out)

    assert extract_age(out) == 16

    assert extract_foods_list(out) == ['mango', 'banana', 'orange']
    assert extract_foods_count(out) == 3
    assert extract_unique_foods(out) == 3

    assert extract_profile_dict(out) == {'name': 'Marc', 'city': 'Goma', 'age': 16, 'foods': ['mango', 'banana', 'orange']}
    assert extract_summary_tuple(out) == ('Marc', 16, 'Goma')
