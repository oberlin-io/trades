# Trades

## Server
### Version (AWS)
```
NAME="Ubuntu"
VERSION="20.04.2 LTS (Focal Fossa)"
ID=ubuntu
ID_LIKE=debian
```

### Update and installs
```
sudo apt-get update
```

#### Python3 pip
```
sudo apt install python3-pip
```

#### pip installs
```
pip install pandas
pip install psycopg2-binary
pip install SQLAlchemy
```
For production, ought to use ```pip install psycopg2```,
which has some build requirements, eg a C compiler.

#### PostgreSQL
```
sudo apt install postgresql postgresql-contrib
```

## Database ops
### Start PostgreSQL server and get psql shell
```
sudo service postgresql status | start | stop
sudo -u postgres psql
```

### Make a password
```
\password postgres
```
Used 'postgres' last.

### Create DB
Use to hold stock data gotten from API.
```
create database trades;
```
List DBs: ```\l```

### Create tables
```
create table acct_status(
  acct_status_id serial primary key,
  acct_status_created timestamp,
  acct_status_cap numeric,
  acct_status_cap_risk_pct numeric,
  acct_status_min_rr_pct numeric
  );
create table symbols(
  symbol_id serial primary key,
  symbol varchar(10),
  symbol_created timestamp
  );
create table setups(
  setup_id serial primary key,
  symbol_id int references symbols(symbol_id),
  setup_created timestamp,
  setup_entry numeric,
  setup_sl numeric,
  setup_min_tp numeric,
  setup_min_tp_realistic boolean,
  setup_pos_size numeric,
  setup_cap numeric,
  setup_cap_risk_pct numeric,
  setup_min_rr_pct numeric
  );
create table bots(
  bot_id serial primary key,
  setup_id int references setups(setup_id),
  bot_timestamp timestamp,
  bot numeric,
  bot_pos_size numeric
  );
create table solds(
  sold_id serial primary key,
  bot_id int references bots(bot_id),
  sold_timestamp timestamp,
  sold numeric,
  sold_pos_size numeric
  );
```
