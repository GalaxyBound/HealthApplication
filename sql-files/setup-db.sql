
-- THE FIRST CREATE DATABASE COMMAND NEEDS TO BE RUN SEPERATELY
CREATE DATABASE elec5622;

CREATE USER elec5622user WITH PASSWORD 'password';

ALTER ROLE elec5622user SET client_encoding TO 'utf8';
ALTER ROLE elec5622user SET default_transaction_isolation TO 'read committed';
ALTER ROLE elec5622user SET timezone TO 'UTC';

GRANT ALL PRIVILEGES ON DATABASE elec5622 TO elec5622user;