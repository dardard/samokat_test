#SELECT c.login,
#COUNT(o.id)
#FROM "Couriers" AS c
#INNER JOIN  "Orders" AS o
#ON c.id = o."courierId"
#WHERE o."inDelivery" = true
#Group by c.login;

#SELECT id,
#CASE
#WHEN finished = true THEN 2
#WHEN cancelled = true THEN -1
#WHEN "inDelivery" = true THEN 1
#ELSE 0
#END
#FROM "Orders";
