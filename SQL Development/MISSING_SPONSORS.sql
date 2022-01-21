select 
       c.id as contract_id,
       TITLE,
       SPONSOR,
       SPONSOR_ID,
       Organization_id,
       ORGANIZATION_NAME,
       ENTITY_ID,
       Status,
       EXT_CONTACT_NAME
       
--    , c.status as contract_status
--    , seq.id as seq_id
--    , seq.type as seq_type
--    , seq.final_action as seq_final_action
--    , f.cmc_id as file_contract_id
    
--    , f.description as file_descr
--    , f.file_name as file_name
--    , f.type as file_type
  --  , f.file_name_orig file_orig_name
  --  , f.upload_date file_upload_date
--    , f.seq_id as file_seq_id
--    , f.checksum
from 
    cm_contracts         c
--left outer join cm_files f 
   -- on  c.id                                   = f.cmc_id 
--left outer join cm_sequences seq on seq.cmc_id = c.id and f.seq_id = seq.id
   
where to_char ( c.DATE_CREATED , 'YYYY-MM-DD' ) > '2021-09-22'
and c.status in ( 'A' , 'R', 'P' )


-- and f.type                                 = 'afullex'
--and seq.type is not null
--order by c.id, f.id