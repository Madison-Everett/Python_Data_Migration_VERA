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
where cm_contracts.status in ( 'A' , 'R', 'P' )