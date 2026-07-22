from devopslib.randomfruit import fruit, meal


def test_fruit():
    fruit_choice = fruit()
    assert fruit_choice in ["apple", "cherry", "strawberry"]


def test_meal(capsys):
    meal("banana")
    captured = capsys.readouterr()
    assert (
        "Your meal is fruit salad with banana" in captured.out
        or "Your meal is fruit salad with banana and cherry" in captured.out
    )
