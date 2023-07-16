import typer
import pyfiglet
from typing import Optional
from scripts.Sockets.Server import Server
from scripts.Sockets.Client import Client
from scripts.Network.Lookup.IP import IP
from scripts.Network.Scanner.PortScanner import PortScanner
from scripts.Network.Proxy.ProxyServer import ProxyServer

app = typer.Typer()

@app.command("server")
def start_server(port: Optional[int]=12345,connections: Optional[int]=5,broadcast: Optional[int]=0):
    server=Server(port=port,connections=connections,broadcast=broadcast)
    server.start_server()

@app.command("client")
def start_client(host: Optional[str]='127.0.0.1', port: Optional[int]=12345):
    client=Client(host=host, port=port)
    client.establish_connection()

@app.command("myIP")
def get_client_info():
    ip=IP()
    print(f'IP: {ip.get_ip_address()}\t Host: {ip.get_hostname()}')

@app.command('port-scan')
def scan_target(target:Optional[str]='127.0.0.1',ports:Optional[str]='1-65536'):
    port_scanner=PortScanner(target=target,ports=ports)
    port_scanner.port_scanner()

@app.command('start-proxy-server')
def start_proxy_server(port:Optional[int]=12345):
    proxy_server=ProxyServer(port=port)
    proxy_server.start()

if __name__ == "__main__":
    ascii_banner=pyfiglet.figlet_format("PORTS")
    print(ascii_banner)
    app()    