select animal_id, name from animal_ins
where intake_condition not like '%AGED%'
order by animal_id