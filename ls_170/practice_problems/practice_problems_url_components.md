# Practice Problems: URL Components

### Question 1

Given the following URL:

```none
https://amazon.com/Double-Stainless-Commercial-Refrigerator/B60HON32?ie=UTF8&qid=142952676&sr=93&keywords=commercial+fridge
```

a) Host is `amazon.com`

b) Query Paramater names: `ie`, `qid`, `sr`, `keywords`

c) Query paramater values: `UTF8` `142952676` `93` `commercial+fridge`

d) Scheme: `https`

e) Path: `/Double-Stainless-Commercial-Refrigerator/B60HON32`

f) Port: not in URL

### Question 2

Add the port `3000` to the following URL:

```none
http://amazon.com/products/B60HON32?qid=142952676&sr=93
```

Answer:

```none
http://amazon.com:3000/products/B60HON32?qid=142952676&sr=93
```

### Question 3

Given the following URL:

```none
http://localhost:4567/todos/15
```

a) Query parameters: N/A

b) Scheme: `http`

c) Path: `/todos/15`

d) Host: `localhost`

e) Port: `4567`

### Question 4

What are two different ways to encode a space in a query parameter? We didn't cover this in the lectures, so feel free to search online for the answer.

**Percent Encoding**: Replace the space with `%20`.

- Example: `https://example.com/some%20page`

**Plus Encoding (only for query parameters)**: Replace the space with `+`.

- Example: `https://example.com/search?q=hello+world`

### Question 5

What character indicates the beginning of a URL's query parameters?

`?`

### Question 6

What character is used between the name and value of a query parameter?

`=`

### Question 7

What character is used between multiple query parameters?

`&`

