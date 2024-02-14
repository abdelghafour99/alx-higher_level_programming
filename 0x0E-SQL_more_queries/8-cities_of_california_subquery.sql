-- A script that lists all the cities of California that can be found in the database hbtn_0d_usa
Select states.id, states.name FROM states, cities WHERE states.name = "California"order by cities.id
