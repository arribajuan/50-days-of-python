from day06.modules.username_generator import UsernameGenerator
import typer

app = typer.Typer()


@app.command()
def main():
    email = str(typer.prompt("What's the email address?"))

    ng = UsernameGenerator()

    if ng.is_email(email):
        result = ng.user_name(email)
        typer.echo(f"Username {result}")
    else:
        typer.echo(f"{email} is not a valid email ... booo.")


if __name__ == "__main__":
    app()


# john.doe@gmail_com is not a valid email ... booo.

# What's the email address?: john.doe@gmail.com
# Username john.doe