select

     (case
        when seq.type = 'AMEND' and seq.final_action = 'Fully Executed' then 'Converted Amendment Number:'|| ' ' || seq.amendment_num   
        when seq.type = 'NEWK' and seq.final_action = 'Fully Executed' then 'New Contract'
        when seq.type = 'ORIGK' and seq.final_action = 'Fully Executed' then 'Original Contract' 
        else null
        end )                       as description
    , f.id as file_id
    , f.file_name as file_name
    , f.file_name_orig as file_original_name
    , f.upload_date as file_upload_date
    , cm_contracts.id                                                               as id 
    , substr(replace ( replace ( cm_contracts.title , chr ( 10 ),' ' ) , chr ( 13 ) , ' ' ) , 0, 255) as name
    , peer_person_2.vunetid                                                         as "owner::ID" 
    , null                                                                          as "agreement::id" 
    , peer_person.vunetid as "agreementCreator::ID" 
    , peer_unit.unit_name as "department::ID" 
    , null                as "multipleCounterparties" 
    , null                as "postAwardAdminContact::ID" 
    , case
            -- Outgoing | Research | Federal Grant Subcontract = Outgoing Subaward Agreement
        when cm_contracts.funding_apar = 'AP' and cm_type_category.id = 12 and cm_type_type.id = 37 
            then 'ID00000018'
            -- Incoming | Research | Federal Grant Subcontract = Incoming Subaward Agreement
        when cm_contracts.funding_apar = 'AR' and cm_type_category.id = 12 and cm_type_type.id = 37 
            then 'ID00000015'
            -- BLANK | Abridged Summary | CDA =  Non-Disclosure Agreement
        when cm_contracts.funding_apar = 'BLANK' and cm_type_category.id = 14 and cm_type_type.id = 
            50 then 'ID00000005'
            --Incoming | Research | Foundation/Non-Profit/Inter-Institutional = Sponsored Research 
            -- Agreement
        when cm_contracts.funding_apar = 'AR' and cm_type_category.id = 12 and cm_type_type.id = 38 
            then 'ID00000011'
            -- BLANK | Abridged Summary | Data Use Agreement = Data Use Agreement
        when cm_contracts.funding_apar = 'BLANK' and cm_type_category.id = 14 and cm_type_type.id = 
            8 then 'ID00000013'
            -- Outgoing | Abridged Summary | VU Billing Agreement = Outgoing Sponsored Billing 
            -- Agreement
        when cm_contracts.funding_apar = 'AP' and cm_type_category.id = 14 and cm_type_type.id = 56 
            then 'ID00000012'
            --Incoming | Research | Industry = Sponsored Research Agreement
        when cm_contracts.funding_apar = 'AR' and cm_type_category.id = 12 and cm_type_type.id = 39 
            then 'ID00000011'
            --Incoming | Research | Other Government = Sponsored Research Agreement
        when cm_contracts.funding_apar = 'AR' and cm_type_category.id = 12 and cm_type_type.id = 40 
            then 'ID00000011'
            -- Outgoing | Research | Foundation/Non-Profit/Inter-Institutional = Outgoing Subaward 
            -- Agreement
        when cm_contracts.funding_apar = 'AP' and cm_type_category.id = 12 and cm_type_type.id = 38 
            then 'ID00000018'
            -- Incoming | Abridged Summary | VU Billing Agreement = Incoming Sponsored Billing 
            -- Agreement
        when cm_contracts.funding_apar = 'AR' and cm_type_category.id = 14 and cm_type_type.id = 56 
            then 'ID00000014'
            -- Incoming | Research | Federal Contract - Prime = Sponsored Research Agreement
        when cm_contracts.funding_apar = 'AR' and cm_type_category.id = 12 and cm_type_type.id = 36 
            then 'ID00000011'
            --  Incoming | Research | Federal Contract - Sub = Sponsored Research Agreement
        when cm_contracts.funding_apar = 'AR' and cm_type_category.id = 12 and cm_type_type.id = 54 
            then 'ID00000011'
            -- Incoming | Prof Svcs | Health Promotions = Sponsored Research Agreement
        when cm_contracts.funding_apar = 'AR' and cm_type_category.id = 11 and cm_type_type.id = 23 
            then 'ID00000011'
            --   | Research | Foundation/Non-Profit/Inter-Institutional = Other
        when cm_contracts.funding_apar is null and cm_type_category.id = 12 and cm_type_type.id = 
            38 then 'ID00000019'
            -- BLANK | Research | Industry = Sponsored Research Agreement
        when cm_contracts.funding_apar = 'BLANK' and cm_type_category.id = 12 and cm_type_type.id = 
            39 then 'ID00000011'
            --  | Research | Federal Contract - Prime = Sponsored Research Agreement
        when cm_contracts.funding_apar is null and cm_type_category.id = 12 and cm_type_type.id = 
            36 then 'ID00000011'
            -- BLANK | Memorandum of Understanding | Other = Teaming Agreement
        when cm_contracts.funding_apar = 'BLANK' and cm_type_category.id = 9 and cm_type_type.id = 
            6 then 'ID00000017'
            -- BLANK | Research | Federal Contract - Prime = Sponsored Research Agreement
        when cm_contracts.funding_apar = 'BLANK' and cm_type_category.id = 12 and cm_type_type.id = 
            36 then 'ID00000011'
            -- BLANK | Research | Foundation/Non-Profit/Inter-Institutional = Other
        when cm_contracts.funding_apar = 'BLANK' and cm_type_category.id = 12 and cm_type_type.id = 
            38 then 'ID00000019'
            -- Incoming | Prof Svcs | VA IPA = Other
        when cm_contracts.funding_apar = 'AR' and cm_type_category.id = 11 and cm_type_type.id = 35 
            then 'ID00000019'
            --  | Research | Industry
        when cm_contracts.id = 58538 then 'ID00000011'
        when cm_contracts.id = 58796 then 'ID00000005'
            -- BLANK | Affiliation | Cooperative = Teaming Agreement
        when cm_contracts.funding_apar = 'BLANK' and cm_type_category.id = 1 and cm_type_type.id = 
            1 then 'ID00000017'
            -- BLANK | Confidentiality | BAA = Non-Disclosure Agreement
        when cm_contracts.funding_apar = 'BLANK' and cm_type_category.id = 2 and cm_type_type.id = 
            7 then 'ID00000005'
            -- Outgoing | Research | Federal Contract - Prime = Outgoing Subaward Agreement
        when cm_contracts.funding_apar = 'AP' and cm_type_category.id = 12 and cm_type_type.id = 36 
            then 'ID00000018'
            -- Outgoing | Research | Industry = Outgoing Subaward Agreement
        when cm_contracts.funding_apar = 'AP' and cm_type_category.id = 12 and cm_type_type.id = 39 
            then 'ID00000018'
            --  | Confidentiality | BAA = Non-Disclosure Agreement
        when cm_contracts.funding_apar is null and cm_type_category.id = 2 and cm_type_type.id = 7 
            then 'ID00000005'
            --  | Research | Other Government = Sponsored Research Agreement
        when cm_contracts.funding_apar is null and cm_type_category.id = 12 and cm_type_type.id = 
            40 then 'ID00000011'
            -- BLANK | Research | Other Government = Sponsored Research Agreement
        when cm_contracts.funding_apar = 'BLANK' and cm_type_category.id = 12 and cm_type_type.id = 
            40 then 'ID00000011'
            -- Incoming | Education | Other = Sponsored Research Agreement
        when cm_contracts.funding_apar = 'AR' and cm_type_category.id = 3 and cm_type_type.id = 6 
            then 'ID00000011'
            -- Incoming | Prof Svcs | Nursing = Sponsored Research Agreement
        when cm_contracts.funding_apar = 'AR' and cm_type_category.id = 11 and cm_type_type.id = 30 
            then 'ID00000011'
            -- Outgoing | Research | Other Government = Outgoing Subaward Agreement
        when cm_contracts.funding_apar = 'AP' and cm_type_category.id = 12 and cm_type_type.id = 40 
            then 'ID00000018'
            -- Cores | Other
        when cm_type_category.id = 15 then 'ID00000019'
        else null
    end "agreementType::ID" 
    , cm_contracts.ext_email        as "contractingParty.contactEmail" 
    , cm_contracts.ext_contact_name as "contractingParty.contactName" 
    , cm_contracts.ext_phone        as "contractingParty.contactPhone" 
    , null                          as "contractingPartyName" 
    , cm_contracts.sponsor          as "contractingorganization::ID" 
    , to_char(cm_contracts.date_start, 'YYYY-MM-DD')       as effectivedate 
    , to_char(cm_contracts.date_end_current, 'YYYY-MM-DD') as expirationdate 
    , null                          as officegenerated 
    , peer_person.vunetid           as "piProxies::ID" 
    , peer_person_1.vunetid         as "investigator::ID" 
    , null                          as "studyTeamMembers::ID"



from peeradm.cm_contracts cm_contracts

Left Outer Join peeradm.cm_type_type cm_type_type On cm_type_type.id = cm_contracts.type_id
Left Outer Join peeradm.cm_type_category cm_type_category On cm_type_category.id = cm_contracts.category_id
Left Outer Join peeradm.peer_person On peer_person.personindex = cm_contracts.primary_contact_id
Left Outer Join peeradm.peer_unit On peer_unit.unitindex = cm_contracts.unit_id
Left Outer Join peeradm.peer_person  peer_person_1  On peer_person_1.personindex = cm_contracts.pi_resp_party_id
Left Outer Join peeradm.peer_person  peer_person_2 On peer_person_2.personindex = cm_contracts.analyst_id
Left Outer Join peeradm.peer_person  peer_person_3 On peer_person_3.personindex = cm_contracts.secondary_contact_id
left Outer Join peeradm.cm_sequences seq on (seq.cmc_id = cm_contracts.id 
and seq.id =
(
    select
        max ( id )
    from
        cm_sequences seq2
    where seq.cmc_id = seq2.cmc_id
)
)
-- null files ids indicate that the fully executed doc is not the one with the highest sequence number
left outer join cm_files f on (f.cmc_id = seq.cmc_id and f.seq_id = seq.id and f.type = 'afullex') and cmc_id =61404 OR
cmc_id =61734 OR
cmc_id =62322 OR
cmc_id =62276 OR
cmc_id =61290 OR
cmc_id =62404 OR
cmc_id =62435 OR
cmc_id =62446 OR
cmc_id =62113 OR
cmc_id =62403 OR
cmc_id =62096 OR
cmc_id =62153 OR
cmc_id =62412 OR
cmc_id =62398 OR
cmc_id =62414 OR
cmc_id =62384 OR
cmc_id =62365 OR
cmc_id =62353 OR
cmc_id =62430 OR
cmc_id =62380 OR
cmc_id =61958 OR
cmc_id =61556 OR
cmc_id =62421 OR
cmc_id =62349 OR
cmc_id =62332 OR
cmc_id =62308 OR
cmc_id =62447 OR
cmc_id =62416 OR
cmc_id =62314 OR
cmc_id =61850 OR
cmc_id =62429 OR
cmc_id =61315 OR
cmc_id =62400 OR
cmc_id =62370 OR
cmc_id =62440 OR
cmc_id =62433 OR
cmc_id =60204 OR
cmc_id =62306 OR
cmc_id =61978 OR
cmc_id =61199 OR
cmc_id =62448 OR
cmc_id =62428 OR
cmc_id =62410 OR
cmc_id =62437 OR
cmc_id =60975 OR
cmc_id =61939 OR
cmc_id =62434 OR
cmc_id =60834 OR
cmc_id =62190 OR
cmc_id =62243 OR
cmc_id =62442 OR
cmc_id =62426 OR
cmc_id =62359 OR
cmc_id =62438 OR
cmc_id =62372 OR
cmc_id =59439 OR
cmc_id =62391 OR
cmc_id =62362 OR
cmc_id =62343 OR
cmc_id =62319 OR
cmc_id =62283 OR
cmc_id =62378 OR
cmc_id =61767 OR
cmc_id =62406 OR
cmc_id =62207 OR
cmc_id =62076 OR
cmc_id =62352 OR
cmc_id =62320 OR
cmc_id =62169 OR
cmc_id =62357 OR
cmc_id =62444 OR
cmc_id =62371 OR
cmc_id =62413 OR
cmc_id =62179 OR
cmc_id =62201 OR
cmc_id =62355 OR
cmc_id =62368 OR
cmc_id =62408 OR
cmc_id =62399 OR
cmc_id =61818 OR
cmc_id =62409 OR
cmc_id =62397 OR
cmc_id =62415 OR
cmc_id =62335 OR
cmc_id =61600 OR
cmc_id =62436 OR
cmc_id =62360 OR
cmc_id =62423 OR
cmc_id =62402 OR
cmc_id =62405 OR
cmc_id =62198 OR
cmc_id =59727 OR
cmc_id =60720 OR
cmc_id =62189 OR
cmc_id =62407 OR
cmc_id =62389 OR
cmc_id =62143 OR
cmc_id =62348 OR
cmc_id =59322 OR
cmc_id =61434 OR
cmc_id =62364 OR
cmc_id =62351 OR
cmc_id =60352 OR
cmc_id =62326 OR
cmc_id =62256 OR
cmc_id =62432 OR
cmc_id =62441 OR
cmc_id =62388 OR
cmc_id =62394 OR
cmc_id =59008 OR
cmc_id =62443 OR
cmc_id =61173 OR
cmc_id =61748

