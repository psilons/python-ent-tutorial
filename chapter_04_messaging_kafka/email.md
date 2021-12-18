


| Server Type                     | Server Encryption | Authentication | Port    |
|---------------------------------|-------------------|----------------|---------|
| SMTP Server (Outgoing Messages) | Non-Encrypted     | AUTH           | 25, 587 |
| 	                               | Secure (TLS)      | StartTLS       | 587     |
|                                 | Secure (SSL)      | SSL            | 465     |
| POP3 Server (Incoming Messages) | Non-Encrypted     | AUTH           | 110     |
 |                                 | Secure (SSL)      | SSL            | 995     |
| IMAP Server (Incoming Messages) | Non-Encrypted     | AUTH           | 143     |
 |                                 | Secure (TLS)      | StartTLS       | 143     |
 |                                 | Secure (SSL)      | SSL            | 993     |

- https://www.arclab.com/en/kb/email/list-of-smtp-and-pop3-servers-mailserver-list.html
