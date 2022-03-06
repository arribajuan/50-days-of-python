from day06.app.main import app
from typer.testing import CliRunner

runner = CliRunner()


def test_app_1():
    result = runner.invoke(app, input="john.doe@gmail.com\n")
    assert result.exit_code == 0
    assert "Username john.doe" in result.stdout

def test_app_2():
    result = runner.invoke(app, input="john.doe@gmail_com\n")
    assert result.exit_code == 0
    assert "john.doe@gmail_com is not a valid email ... booo." in result.stdout