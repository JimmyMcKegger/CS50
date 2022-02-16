-- Keep a log of any SQL queries you execute as you solve the mystery.

-- Find the crime schene report (295)
SELECT *
FROM crime_scene_reports
WHERE day = 28
AND month = 7
AND year = 2021
AND street = "Humphrey Street"
AND description LIKE "%duck%";

-- find the witnesses interviews
SELECT *
FROM interviews
WHERE day = 28
AND month = 7
AND year = 2021
AND transcript LIKE "%bakery%";

-- Thief withdrew money from the ATM on Leggett Street the day of the robbery
SELECT account_number
FROM atm_transactions
WHERE day = 28
AND month = 7
AND year = 2021
AND atm_location = "Leggett Street"
AND transaction_type = "withdraw";

-- Thief got into a car in the parking lot within 10 minutes of the robbery
SELECT *
FROM bakery_security_logs
WHERE day = 28
AND month = 7
AND year = 2021
AND hour = 10
AND minute BETWEEN 16 AND 25;

-- Thief took the earliest flight from Fiftyville on 29/7/2021
SELECT *
FROM flights
WHERE origin_airport_id = (SELECT id FROM airports WHERE city = "Fiftyville")
AND day = 29
AND month = 7
AND year = 2021
ORDER BY hour
LIMIT 1;

SELECT city FROM airports WHERE id = 4;

SELECT *
FROM passengers
WHERE flight_id = 36;

-- phone call from bakery

SELECT caller
FROM phone_calls
WHERE day = 28
AND month = 7
AND year = 2021
AND duration < 60;

-- suspects
SELECT name
FROM people
WHERE passport_number IN (SELECT passport_number FROM passengers WHERE flight_id = 36)
AND id IN (SELECT person_id
  FROM bank_accounts
  WHERE account_number  IN (SELECT account_number
    FROM atm_transactions
    WHERE day = 28
    AND month = 7
    AND year = 2021
    AND atm_location = "Leggett Street"
    AND transaction_type = "withdraw"))
    AND license_plate IN (SELECT license_plate
  FROM bakery_security_logs
  WHERE day = 28
  AND month = 7
  AND year = 2021
  AND hour = 10
  AND minute BETWEEN 16 AND 25)
AND phone_number IN (SELECT caller
  FROM phone_calls
  WHERE day = 28
  AND month = 7
  AND year = 2021
  AND duration < 60);

  -- accomplice (Robin)
  SELECT name
  FROM people
  WHERE phone_number = '(375) 555-8161';