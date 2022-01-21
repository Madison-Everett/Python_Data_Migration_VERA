-- after exporting the insert statements, some of the column name will need to be modified. The Huron db names were too long.
with pool as (

select
    replace ( replace ( cm_contracts.proj_title , chr ( 10 ),' ' ) , chr ( 13 ) , ' ' ) as description 
    , cm_contracts.id                                                               as id 
    , replace ( replace ( cm_contracts.title , chr ( 10 ),' ' ) , chr ( 13 ) , ' ' )     as name 
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
        else null
    end "agreementType::ID" 
    , cm_contracts.ext_email        as "contractingParty.contactEmail" 
    , cm_contracts.ext_contact_name as "contractingParty.contactName" 
    , cm_contracts.ext_phone        as "contractingParty.contactPhone" 
    , null                          as "contractingPartyName" 
    , cm_contracts.sponsor          as "contractingorganization::ID" 
    , cm_contracts.date_start       as effectivedate 
    , cm_contracts.date_end_current as expirationdate 
    , null                          as officegenerated 
    , peer_person.vunetid           as "piProxies::ID" 
    , peer_person_1.vunetid         as "investigator::ID" 
    , null                          as "studyTeamMembers::ID"



from peeradm.cm_contracts cm_contracts

Left Join peeradm.cm_type_type cm_type_type On cm_type_type.id = cm_contracts.type_id
Left Join peeradm.cm_type_category cm_type_category On cm_type_category.id = cm_contracts.category_id
Left Join peeradm.peer_person On peer_person.personindex = cm_contracts.primary_contact_id
Left Join peeradm.peer_unit On peer_unit.unitindex = cm_contracts.unit_id
Left Join peeradm.peer_person  peer_person_1  On peer_person_1.personindex = cm_contracts.pi_resp_party_id
Left Join peeradm.peer_person  peer_person_2 On peer_person_2.personindex = cm_contracts.analyst_id
Left Join peeradm.peer_person  peer_person_3 On peer_person_3.personindex = cm_contracts.secondary_contact_id
--where cm_contracts.status in ( 'P' ) and 
--where cm_contracts.status in ( 'A' , 'R', 'P' )




)
select * from cm_files
where cmc_id in (select id from pool) and type = 'afullex' and cmc_id =61404 OR
type = 'afullex' and cmc_id =61734 OR
type = 'afullex' and cmc_id =62322 OR
type = 'afullex' and cmc_id =62276 OR
type = 'afullex' and cmc_id =61290 OR
type = 'afullex' and cmc_id =62404 OR
type = 'afullex' and cmc_id =62435 OR
type = 'afullex' and cmc_id =62446 OR
type = 'afullex' and cmc_id =62113 OR
type = 'afullex' and cmc_id =62403 OR
type = 'afullex' and cmc_id =62096 OR
type = 'afullex' and cmc_id =62153 OR
type = 'afullex' and cmc_id =62412 OR
type = 'afullex' and cmc_id =62398 OR
type = 'afullex' and cmc_id =62414 OR
type = 'afullex' and cmc_id =62384 OR
type = 'afullex' and cmc_id =62365 OR
type = 'afullex' and cmc_id =62353 OR
type = 'afullex' and cmc_id =62430 OR
type = 'afullex' and cmc_id =62380 OR
type = 'afullex' and cmc_id =61958 OR
type = 'afullex' and cmc_id =61556 OR
type = 'afullex' and cmc_id =62421 OR
type = 'afullex' and cmc_id =62349 OR
type = 'afullex' and cmc_id =62332 OR
type = 'afullex' and cmc_id =62308 OR
type = 'afullex' and cmc_id =62447 OR
type = 'afullex' and cmc_id =62416 OR
type = 'afullex' and cmc_id =62314 OR
type = 'afullex' and cmc_id =61850 OR
type = 'afullex' and cmc_id =62429 OR
type = 'afullex' and cmc_id =61315 OR
type = 'afullex' and cmc_id =62400 OR
type = 'afullex' and cmc_id =62370 OR
type = 'afullex' and cmc_id =62440 OR
type = 'afullex' and cmc_id =62433 OR
type = 'afullex' and cmc_id =60204 OR
type = 'afullex' and cmc_id =62306 OR
type = 'afullex' and cmc_id =61978 OR
type = 'afullex' and cmc_id =61199 OR
type = 'afullex' and cmc_id =62448 OR
type = 'afullex' and cmc_id =62428 OR
type = 'afullex' and cmc_id =62410 OR
type = 'afullex' and cmc_id =62437 OR
type = 'afullex' and cmc_id =60975 OR
type = 'afullex' and cmc_id =61939 OR
type = 'afullex' and cmc_id =62434 OR
type = 'afullex' and cmc_id =60834 OR
type = 'afullex' and cmc_id =62190 OR
type = 'afullex' and cmc_id =62243 OR
type = 'afullex' and cmc_id =62442 OR
type = 'afullex' and cmc_id =62426 OR
type = 'afullex' and cmc_id =62359 OR
type = 'afullex' and cmc_id =62438 OR
type = 'afullex' and cmc_id =62372 OR
type = 'afullex' and cmc_id =59439 OR
type = 'afullex' and cmc_id =62391 OR
type = 'afullex' and cmc_id =62362 OR
type = 'afullex' and cmc_id =62343 OR
type = 'afullex' and cmc_id =62319 OR
type = 'afullex' and cmc_id =62283 OR
type = 'afullex' and cmc_id =62378 OR
type = 'afullex' and cmc_id =61767 OR
type = 'afullex' and cmc_id =62406 OR
type = 'afullex' and cmc_id =62207 OR
type = 'afullex' and cmc_id =62076 OR
type = 'afullex' and cmc_id =62352 OR
type = 'afullex' and cmc_id =62320 OR
type = 'afullex' and cmc_id =62169 OR
type = 'afullex' and cmc_id =62357 OR
type = 'afullex' and cmc_id =62444 OR
type = 'afullex' and cmc_id =62371 OR
type = 'afullex' and cmc_id =62413 OR
type = 'afullex' and cmc_id =62179 OR
type = 'afullex' and cmc_id =62201 OR
type = 'afullex' and cmc_id =62355 OR
type = 'afullex' and cmc_id =62368 OR
type = 'afullex' and cmc_id =62408 OR
type = 'afullex' and cmc_id =62399 OR
type = 'afullex' and cmc_id =61818 OR
type = 'afullex' and cmc_id =62409 OR
type = 'afullex' and cmc_id =62397 OR
type = 'afullex' and cmc_id =62415 OR
type = 'afullex' and cmc_id =62335 OR
type = 'afullex' and cmc_id =61600 OR
type = 'afullex' and cmc_id =62436 OR
type = 'afullex' and cmc_id =62360 OR
type = 'afullex' and cmc_id =62423 OR
type = 'afullex' and cmc_id =62402 OR
type = 'afullex' and cmc_id =62405 OR
type = 'afullex' and cmc_id =62198 OR
type = 'afullex' and cmc_id =59727 OR
type = 'afullex' and cmc_id =60720 OR
type = 'afullex' and cmc_id =62189 OR
type = 'afullex' and cmc_id =62407 OR
type = 'afullex' and cmc_id =62389 OR
type = 'afullex' and cmc_id =62143 OR
type = 'afullex' and cmc_id =62348 OR
type = 'afullex' and cmc_id =59322 OR
type = 'afullex' and cmc_id =61434 OR
type = 'afullex' and cmc_id =62364 OR
type = 'afullex' and cmc_id =62351 OR
type = 'afullex' and cmc_id =60352 OR
type = 'afullex' and cmc_id =62326 OR
type = 'afullex' and cmc_id =62256 OR
type = 'afullex' and cmc_id =62432 OR
type = 'afullex' and cmc_id =62441 OR
type = 'afullex' and cmc_id =62388 OR
type = 'afullex' and cmc_id =62394 OR
type = 'afullex' and cmc_id =59008 OR
type = 'afullex' and cmc_id =62443 OR
type = 'afullex' and cmc_id =61173 OR
type = 'afullex' and cmc_id =61748










