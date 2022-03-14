import typer

app = typer.Typer()


@app.command()
def main():
    password = str(typer.prompt("What's the password to hide?"))
    password_length = len(password)
    hidden_password = "*" * password_length

    typer.echo(f"Your hidden lassword is '{hidden_password}' and has a length of {password_length}")


if __name__ == "__main__":
    app()
