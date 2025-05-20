The two reaming sub languages are Data Definition Language which deals with creating and altering the database schema (CREATE TABLE, ALTER TABLE) and Data Manipulation Language which deals with the insertion, removal and manipulation of the data within the database (SELECT, INSERT).

### 1. Describe the difference between the `varchar` and `text` data types.

Both store textual data. `varchar(n)` stores up tp `n` characters. Text columns can store an unlimited number of characters.

### 2. Describe the difference between the `integer`, `decimal`, and `real` data types.

Integer is used to store whole numbers. Decimal is used to store arbitrary precision numbers while real is used to store floating-point numbers.

### 3. What is the largest value that can be stored in an `integer` column?

2147483647

### 4. Describe the difference between the `timestamp` and `date` data types.

Timestamp includes the data and time whereas date just includes the date.

### 5.Can a time with a time zone be stored in a column of type `timestamp`?

No. But there is a `timestamp with time zone` data type that will store a timestamp with a timezone.

