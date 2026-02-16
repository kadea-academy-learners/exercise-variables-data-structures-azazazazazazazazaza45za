from ds_test_utils import (
    run_program, assert_prompts,
    extract_age, extract_foods_list, extract_foods_count, extract_unique_foods,
    extract_profile_dict, extract_summary_tuple
)

def test_05_case_many():
    out = run_program('Patrick', 'Matadi', 1975, 2026, 'fufu, pondu, saka saka, fufu')
    assert_prompts(out)

    assert extract_age(out) == 51

    assert extract_foods_list(out) == ['fufu', 'pondu', 'saka saka', 'fufu']
    assert extract_foods_count(out) == 4
    assert extract_unique_foods(out) == 3

    assert extract_profile_dict(out) == {'name': 'Patrick', 'city': 'Matadi', 'age': 51, 'foods': ['fufu', 'pondu', 'saka saka', 'fufu']}
    assert extract_summary_tuple(out) == ('Patrick', 51, 'Matadi')
