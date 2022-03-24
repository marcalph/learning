-- +-------------+------+
-- | Column Name | Type |
-- +-------------+------+
-- | num         | int  |
-- | frequency   | int  |
-- +-------------+------+
-- num is the primary key for this table.
-- Each row of this table shows the frequency of a number in the database.


-- The median is the value separating the higher half from the lower half of a data sample.



with a as (
    select num,
           sum(frequency) over (order by num) - frequency as lower_num,
           sum(frequency) over (order by num) as upper_num,
           sum(frequency) over () / 2 as medium_num
    from Numbers
)

SELECT avg(num) as median
FROM a
where medium_num between  lower_num and upper_num
