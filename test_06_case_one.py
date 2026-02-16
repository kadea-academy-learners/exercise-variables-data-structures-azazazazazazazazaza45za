from ds_test_utils import (
    run_program, assert_prompts,
    extract_age, extract_foods_list, extract_foods_count, extract_unique_foods,
    extract_profile_dict, extract_summary_tuple
)

def test_06_case_one():
    out = run_program('Ines', 'Kisangani', 2005, 2026, 'water')
    assert_prompts(out)

    assert extract_age(out) == 21

    assert extract_foods_list(out) == ['water']
    assert extract_foods_count(out) == 1
    assert extract_unique_foods(out) == 1

    assert extract_profile_dict(out) == {'name': 'Ines', 'city': 'Kisangani', 'age': 21, 'foods': ['water']}
    assert extract_summary_tuple(out) == ('Ines', 21, 'Kisangani')
