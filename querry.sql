-- A query that will display the table on the test

SELECT 
  circuit_location AS loc,
  grid,
  position,
  fastest_lap,
  points,
  driver_name,
  race_name,
  time,
  year,
  team_name,
  date
FROM races
WHERE year = 2020
ORDER BY points DESC;