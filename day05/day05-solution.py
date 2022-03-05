import my_discount
import typer

def main():
    price = float(typer.prompt("What's the price?"))
    discount_percentage = float(typer.prompt("What's the discount %?"))

    md = my_discount.MyDiscount()
    result = md.my_discount(price, discount_percentage)

    typer.echo(f"Final price {result}")


if __name__ == "__main__":
    typer.run(main)