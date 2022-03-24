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

-- Write an SQL query to report the device that is first logged in for each player.


SELECT player_id, device_id
FROM activity
WHERE (player_id, event_date)
IN (
    SELECT player_id, min(event_id)
    FROM activity
    GROUP BY player_id
)
