### Python Enterprise Tutorial

Python has so many libraries, e.g.,
https://github.com/vinta/awesome-python
Often, there are more than one way to do something.

We intend to provide a minimal foundation for enterprise applications. No
matter how we try, this is subjective. We provide one tool for each of the
enterprise requirements. Some requirements might need a combination
of several libraries.


#### Office Documents and PDFs
___
- Word: pydocx
- Excel: openpyxl
- Powerpoint: python-ppt
- PDF: reportlab / pdfplumber
- OCR: pytesseract
- Others: pywin32

#### Paralle Computing
___
- Threading and PIL
- Dask
- Others: 
    - PySpark
    - Celery 
    - Airflow 
    - asynio

#### Web
___
- Flask
- Serialization: JSON (json / simplejson), Pickle-Json, 

- Others: Tornado / Django
- Related: HTML, Javascript

#### Database
___
- PyODBC
    - Database Connections
    - Local Transactions and Embedded Transactions
    - Table Row to Object Mapper
    - Pandas
- Others: 
    - SqlAlchemy
- JSON
    - Rest: JSON to Object Mapper
    - Large CSV data
- unique id generating
    
Databases:
https://db-engines.com/en/ranking
- Sql Databases
    - Postgres
    - MariaDB
    - Oracle
    - MS Sqlserver
    - MySQL 
- NoSql Databases
    - ClickHouse time series database
    - Neo4j Graph database
    - InfluxDB time series database
    - Solr / Elastic Search indexer
- Caches
    - Redis
    - Geode / Pivotal GemFire
    - Ignite / Gridgain
    - Hazelcast
    - Oracle Coherence
- Distributed File System:
    - Hadoop
    - Query with Apache Storm

#### Remoting
___
- HTTP: 
    - requests
    - httpx

- Crawler: 
    - BeautifulSoup4, 
    - PyQT5
    - Regular Expression: https://github.com/ziishaned/learn-regex

- FTP: SSL / paramiko
- SSH: fabric
- Email
- Others:
    - xmlrpc
    - lxml
    - suds
    - AWS SMS (phone message)

#### Messaging with Kafka
___
- Producer/Consumer
- Queues and Topics
- Broker Setup
- Others:
    - RabbitMQ / ActiveMQ / ZeroMQ
    - AWS SQS
    - Twisted
- Poison Message

#### Pandas
___
- Pandas: NoOO
- Transforms
- Aggregation
- Modin
- pandas-profiling

#### Application Configuration
___
- IoC
- Networkx & Graphviz & PyDot

#### Application Design 
___  
We will discuss the following topics:
- [Software Design](chapter_09_design/software_engineering.md)
- [Design Principles](chapter_09_design/docs/design_principles.md)
- [Design Patterns](chapter_09_design/docs/design_patterns.md)
- [Design Idioms](chapter_09_design/docs/design_idioms.md)

Software development is complex, we outline a can-be-followed approach with reasonable reasons.


#### Build and Deployment
___
- Python Project Setup
- IntelliJ Setup
- Test Setup
- Build Setup
- Deployment Setup


#### Authentication and Authorization (AA)
___
One topic that we intend to leave out because of the environment setup - 
Authentication and Authorization. However, we want to highlight some
features in this topic:
- HTTP(S) Authentication: HTTP form or headers(such as "Basic Auth"), most of 
  the time you will get a token/cookie which will be used in subsequent calls.
  
- Kerberos based: Use current login information, so it realizes SSO.

- Custom authentication, such oauth2

Because of the unavailable external setup, we leave this out of our scope.
However, they are very common in enterprise applications.
