from ds_test_utils import (
    run_program, assert_prompts,
    extract_age, extract_foods_list, extract_foods_count, extract_unique_foods,
    extract_profile_dict, extract_summary_tuple
)

def test_01_case_basic():
    out = run_program('John Doe', 'Kinshasa', 2000, 2026, 'pizza, burger, pizza')
    assert_prompts(out)

    assert extract_age(out) == 26

    assert extract_foods_list(out) == ['pizza', 'burger', 'pizza']
    assert extract_foods_count(out) == 3
    assert extract_unique_foods(out) == 2

    assert extract_profile_dict(out) == {'name': 'John Doe', 'city': 'Kinshasa', 'age': 26, 'foods': ['pizza', 'burger', 'pizza']}
    assert extract_summary_tuple(out) == ('John Doe', 26, 'Kinshasa')
