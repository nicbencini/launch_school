SELECT customers.id, customers.email, COUNT(events.id)
FROM customers
LEFT OUTER JOIN tickets
ON tickets.customer_id = customers.id
LEFT OUTER JOIN events
ON tickets.event_id = events.id
GROUP BY DISTINCT(customers.id)
HAVING COUNT(events.id) = 3
;

SELECT events.name, events.starts_at, sections.name, seats.row , seats.number
FROM events
INNER JOIN tickets
ON tickets.event_id = events.id
LEFT JOIN seats
ON seats.id = tickets.seat_id
LEFT JOIN sections
ON seats.section_id = sections.id
LEFT JOIN customers
ON tickets.customer_id = customers.id
GROUP BY customers.email, events.name, events.starts_at, sections.name, seats.row, seats.number
HAVING customers.email = 'gennaro.rath@mcdermott.co'
ORDER BY  events.starts_at ASC
;
