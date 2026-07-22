(rr-webserver)=
# Web Server Security

## Summary

This section is explains the basics of setting up a publicly accessible web server.
It touches upon the following basic concepts:

1. Application server: a software that makes an application available to the end users. It can use frameworks like [Node.js](https://nodejs.org/en) (JavaScript), [FastAPI](https://fastapi.tiangolo.com/) or any other framework.
1. Client: a software that makes a request to a server. This can be a web browser that opens a web page that runs on a web server.
1. Reverse proxy: a server that does not host any content itself, but is exposed to the publicly accessible internet with the task to filter and forward incoming requests to an application server.

Note: both 'server' and 'client' are often used in an ambiguous sense, referring to either software or hardware.
The term 'server' hence sometimes means an (application) server software that provides data through a network, or to a computing running that software.
Equivalently, a client can mean a software that communicates with a server, or a computer that runs that software.

### Server Fundamentals

Each server on the internet is assigned a unique *IP address* through which it can be located by other computers.
These IP addresses are shaped in a specific numeric format.
In version 4 of the Internet Protocol (IPv4), they have a form like this: `172.16.254.1`.
In version 6 (IPv6), they look like this: `0123:4567:89ab:cdef:0123:4567:89ab:cdef`.

To make it easier to remember a server's address, the *DNS* (_Domain Name System_) service provides mappings hostnames to IP addresses, for instance `www.example.com` to `93.184.216.34` or `2606:2800:220:1:248:1893:25c8:1946`.
For that purpose, dedicated DNS servers hold a registry of these mappings.
When a client wants to connect to through a server to its name, it performs two separate requests:

1. Connect to the DNS server to retrieve the IP address for `www.example.com` (-> `93.184.216.34`).
2. Connect to the server through that IP address.

Each server application uses a specific *port* through which clients can communicate with it.
Ports are numbered from 0 to 65535.
Although these number don't have intrinsic meaning, some ports are commonly assigned to specific application types, for instance ports 80 and 8080 for (unencrypted) web applications, or port 22 for SSH (Secure Shell).
The port numbers from 0 to 1023 are called _well-known_ ports.
Most operating systems require special privileges to assign an application to any of these ports.

### Network Fundamentals

The internet deserves its name based on the fact that it comprises a set of inter-connected sub-networks that allow computers within these sub-networks to communicate with each other.
With such a sub-network, not all computers might be reachable from outside.
This is typically the case for home networks in which a router creates the connection to the internet.
Devices including laptops, smartphones connect -- as clients -- to any internet server through this router.
However, those internal devices are typically not reachable for computers from outside the same sub-network.

Using the combination of IP address and port, a client can open a connection with a server, if the server is reachable, and the specified port is open.

TODO:
- motivation: why to use a reverse proxy?
- what is reverse proxy?
- how to set up a reverse proxy using Caddy?
