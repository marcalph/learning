-- +--------------+---------+
-- | Column Name  | Type    |
-- +--------------+---------+
-- | player_id    | int     |
-- | device_id    | int     |
-- | event_date   | date    |
-- | games_played | int     |
-- +--------------+---------+
-- (player_id, event_date) is the primary key of this table.
-- This table shows the activity of players of some games.
-- Each row is a record of a player who logged in and played a number of games (possibly 0) before logging out on someday using some device.


-- Write an SQL query to report the fraction of players that logged in again on
-- the day after the day they first logged in, rounded to 2 decimal places. In
-- other words, you need to count the number of players that logged in for at
-- least two consecutive days starting from their first login date, then divide
-- that number by the total number of players.



SELECT sum(CASE WHEN temp.min_date + 1 = a.event_date THEN 1 ELSE 0 END)/count(distinct temp.player_id)
FROM (
    SELECT plqyer_id, min(event_date) as min_date
    FROM activty
    GROUP BY player_id as temp
    JOIN
    activity ON temp.player_id = a.player_id
)
