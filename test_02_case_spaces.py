from ds_test_utils import (
    run_program, assert_prompts,
    extract_age, extract_foods_list, extract_foods_count, extract_unique_foods,
    extract_profile_dict, extract_summary_tuple
)

def test_02_case_spaces():
    out = run_program('Aline K.', 'Lubumbashi', 1998, 2026, '  rice , beans,  fish ')
    assert_prompts(out)

    assert extract_age(out) == 28

    assert extract_foods_list(out) == ['rice', 'beans', 'fish']
    assert extract_foods_count(out) == 3
    assert extract_unique_foods(out) == 3

    assert extract_profile_dict(out) == {'name': 'Aline K.', 'city': 'Lubumbashi', 'age': 28, 'foods': ['rice', 'beans', 'fish']}
    assert extract_summary_tuple(out) == ('Aline K.', 28, 'Lubumbashi')
