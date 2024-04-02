from click.testing import CliRunner
import run as run


def test_add():
    runner = CliRunner()
    result = runner.invoke(add)
    assert result.exit_code is 0
    assert "add" in result.output