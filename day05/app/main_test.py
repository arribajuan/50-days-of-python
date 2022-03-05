from .main import app
from typer.testing import CliRunner

runner = CliRunner()


def test_app():
    result = runner.invoke(app, input="150\n15\n")
    assert result.exit_code == 0
    assert "Final price 127.5" in result.stdout
