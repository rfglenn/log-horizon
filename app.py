import click

from website import create_app
from database import db

app = create_app()

@app.cli.command()
def initdb():
    click.echo("Creating database tables...")
    db.create_all()
    click.echo("Done")

@app.cli.command()
def dropdb():
    if click.prompt("This will clear all data. Are you sure?"):
        click.echo("Dropping database tables...")
        db.drop_all()
    else:
        click.echo("Aborting")


