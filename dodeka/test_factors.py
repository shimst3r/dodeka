from dodeka import factors


def test_generate_factors():
    expected = [
        factors.Factor(title=title, short_description=short_description)
        for title, short_description in factors.FACTORS
    ]
    actual = factors.generate_factors()

    assert actual == expected
