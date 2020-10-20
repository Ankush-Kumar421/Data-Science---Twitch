--- Note that the queries were used on the database and resulted in different results when compared to the codecademy platform.
--- The reason for the difference was you can use the database to work on your PC or use the codecademy website. I chose to use my PC.


/* Get familiar with the two tables (stream and chat) */


-- Select all rows and examine the first 20 rows of each table.
SELECT *
FROM stream
LIMIT 20;

SELECT *
FROM chat
LIMIT 20;


-- What are the unique games in the stream table?
SELECT DISTINCT game
FROM stream;

-- What are the unique channels in the stream table?
SELECT DISTINCT channel
FROM stream;


/* Aggregate Functions: Answer a set of questions using the stream table. */

-- What are the most popular games in the stream table?
SELECT game, COUNT(*)
FROM stream
GROUP BY 1
ORDER BY 2 DESC;

-- Where are these League of Legends (LoL) stream viewers located?
SELECT country, COUNT(*)
FROM stream
WHERE game = "League of Legends"
GROUP BY 1
ORDER BY 2 DESC
LIMIT 11;

-- Create a list of players and their number of steamers.
SELECT player, COUNT(*)
FROM stream
GROUP BY 1
ORDER BY 2 DESC;

-- Create a new column named genre for each of the games. Group the games into their genres: Multiplayer Online Battle Arena (MOBA), First Person Shooter (FPS), Survival, and Other.
SELECT game,
  CASE
    WHEN game = "League of Legends" OR game = "Dota 2" 
        OR game = "Heroes of the Storm"    
      THEN "MOBA"
    WHEN game = "Counter-Strike: Global Offensive" THEN "FPS"
    WHEN game = "DayZ" OR game = "Survival Evolved" THEN "Survival"
    ELSE "Other"
  END AS "genre",
  COUNT(*)
FROM stream
GROUP BY 1
ORDER BY 3 DESC;


/* How does view count change in the course of a day? */

-- Lets look at the time column from the stream table. 
SELECT time
FROM stream
LIMIT 10;

-- Use the function strftime(format, column) and see what it does.
SELECT time,
   strftime('%S', time)
FROM stream
GROUP BY 1
LIMIT 20;

-- Use strftime() function and see the view count for each hour. Then fitler with only users in your country. 
SELECT 
   strftime('%H', time),
   COUNT(*)
FROM stream
WHERE country = "US"
GROUP BY 1;


/* Joining the two tables. */

SELECT *
FROM stream
JOIN chat
  ON stream.device_id = chat.device_id;


-- Some insights on viewers and chat room users on my favorite games.
  -- It looks like League of Legends game had total of 92,478 subscribers that were chatting.
  -- It looks Dota 2 game had 145 subscribers that were chatting. 
SELECT stream.game, stream.subscriber, COUNT(stream.subscriber)
FROM stream
JOIN chat
  ON stream.device_id = chat.device_id
WHERE (stream.subscriber = "true") AND
      (stream.game = "League of Legends" OR stream.game = "Dota 2")
GROUP BY 1
ORDER BY 3 DESC;

