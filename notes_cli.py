import os
import sys
import click
from models import Note, init_db

@click.group()
def cli():
    pass

@cli.command()
@click.argument('title')
@click.argument('content', required=False)
def create(title, content=''):
    """Create a new note with the given title and
content."""
    session = init_db()
    note = Note(title=title, content=content)
    session.add(note)
    session.commit()
    click.echo(f"Note '{title}' created.")

@cli.command()
@click.argument('title')
@click.argument('content', required=False)
def update(title, content=''):
    """Update the content of a note with the given
title."""
    session = init_db()
    note = session.query(Note).filter_by(title=title).first()
    if not note:
        click.echo(f"No note found with title '{title}'.")
        return
    note.content = content
    session.commit()
    click.echo(f"Note '{title}' updated.")

@cli.command()
@click.argument('title')
def delete(title):
    """Delete a note with the given title."""
    session = init_db()
    note = session.query(Note).filter_by(title=title).first()
    if not note:
        click.echo(f"No note found with title
'{title}'.")
        return
    session.delete(note)
    session.commit()
    click.echo(f"Note '{title}' deleted.")

@cli.command()
@click.argument('title')
def share(title):
    """Share a note with the given title as markdown."""
    session = init_db()
    note = session.query(Note).filter_by(title=title).first()
    if not note:
        click.echo(f"No note found with title
'{title}'.")
        return
    markdown_note = f'# {note.title}\n\n{note.content}'
    with open(f'{title}.md', 'w') as f:
        f.write(markdown_note)
    click.echo(f"Note '{title}' shared as '{title}.md'.")

if __name__ == '__main__':
    cli()
