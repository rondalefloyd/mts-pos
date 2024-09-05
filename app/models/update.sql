UPDATE "Date"
SET "IsHoliday" = TRUE
WHERE   
    ("Month" = 1 AND "Day" = 1) OR
    ("Month" = 11 AND "Day" BETWEEN 29 AND 30) OR
    ("Month" = 12 AND "Day" BETWEEN 24 AND 31);