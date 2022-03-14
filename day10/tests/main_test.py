from day10.app.main import app
from typer.testing import CliRunner

runner = CliRunner()


def test_app_1():
    result = runner.invoke(app, input="hello\n")
    assert result.exit_code == 0
    assert "Your hidden lassword is '*****' and has a length of 5" in result.stdout
