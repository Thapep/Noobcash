import requests
import click
import addresses
from ip import get_my_ip

@click.group()
def cli():
    pass

@click.command()
def hello():
    click.echo("Hello World!")

@click.command()
def connect():
    click.echo("Connecting to bootstrap...")
    my_ip = get_my_ip()
    url = "http://" + my_ip + ":5000/setup_myself"
    r = requests.get(url)
    click.echo("Returned this:")
    click.echo(r.text)

@click.command()
@click.option('-i', '--id', help='Id of receiving node.')
@click.option('-a', '--amount', help='Amount of CC to send.')
def t(id, amount):
    # Send amount CC another node
    #url = "http://" + addresses[id] + ':5000/send_money'
    print("Sending request")
    my_ip = get_my_ip()
    print(my_ip)
    print(type(my_ip))
    url = "http://" + my_ip + ":5000/send_money"
    r = requests.post(url, data={'ip': addresses.global_addresses[id], 'amount': amount})
    print(r)

@click.command()
def balance():
    r = requests.get("http://" + get_my_ip() + ":5000/get_balance")
    print("Your wallet has " + r.text + " NBCs")

cli.add_command(balance)
cli.add_command(hello)
cli.add_command(connect)
cli.add_command(t)

if __name__ == '__main__':
    cli()
