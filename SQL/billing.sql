drop table billing;
create table billing
(
      customer_id               int
    , customer_name             varchar(1)
    , billing_id                varchar(5)
    , billing_creation_date     date
    , billed_amount             int
);

insert into billing values (1, 'A', 'id1', '10-10-2020', 100);
insert into billing values (1, 'A', 'id2', '11-11-2020', 150);
insert into billing values (1, 'A', 'id3', '12-11-2021', 100);
insert into billing values (2, 'B', 'id4', '10-11-2019', 150);
insert into billing values (2, 'B', 'id5', '11-11-2020', 200);
insert into billing values (2, 'B', 'id6', '12-11-2021', 250);
insert into billing values (3, 'C', 'id7', '01-01-2018', 100);
insert into billing values (3, 'C', 'id8', '05-01-2019', 250);
insert into billing values (3, 'C', 'id9', '06-01-2021', 300);

select * from billing;


-- write an SQL query to find average billing amount for each customer 
-- between 2019 to 2021, assume 0 billing amount for customer if no billing 
-- for a particular year

SELECT customer_id, customer_name, AVG(billed_amount) as avg_billed_amount
FROM billing
WHERE YEAR(billing_creation_date) BETWEEN '2019' AND '2021'
GROUP BY customer_id,customer_name;

