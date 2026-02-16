from ds_test_utils import (
    run_program, assert_prompts,
    extract_age, extract_foods_list, extract_foods_count, extract_unique_foods,
    extract_profile_dict, extract_summary_tuple
)

def test_08_case_symbols():
    out = run_program('Nadia', 'Mbandaka', 2001, 2026, 'ice-cream, hot dog, ice-cream')
    assert_prompts(out)

    assert extract_age(out) == 25

    assert extract_foods_list(out) == ['ice-cream', 'hot dog', 'ice-cream']
    assert extract_foods_count(out) == 3
    assert extract_unique_foods(out) == 2

    assert extract_profile_dict(out) == {'name': 'Nadia', 'city': 'Mbandaka', 'age': 25, 'foods': ['ice-cream', 'hot dog', 'ice-cream']}
    assert extract_summary_tuple(out) == ('Nadia', 25, 'Mbandaka')
