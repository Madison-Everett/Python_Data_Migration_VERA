select cm_contracts.id from cm_contracts
where DATE_START_CURRENT between 
To_date('2021-02-25 00:00:00','YYYY-MM-DD HH24:MI:SS') 
and To_date('2021-03-25 00:00:00','YYYY-MM-DD HH24:MI:SS');