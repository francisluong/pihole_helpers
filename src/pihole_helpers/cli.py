import click


@click.command()
def hello():
    print("Hello from pihole-helpers!")


def main():
    hello()


if __name__ == "__main__":
    main()
