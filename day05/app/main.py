from day05.modules.my_discount import MyDiscount
import typer

app = typer.Typer()


@app.command()
def main():
    price = float(typer.prompt("What's the price?"))
    discount_percentage = float(typer.prompt("What's the discount %?"))

    md = MyDiscount()
    result = md.my_discount(price, discount_percentage)

    typer.echo(f"Final price {result}")


if __name__ == "__main__":
    app()
