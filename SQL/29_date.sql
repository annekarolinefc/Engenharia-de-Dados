-- DATE — Operações envolvendo datas


use datawarehouse;

SELECT DataVenda                          as Data
     , day(DataVenda)                     as Dia
     , month(DataVenda)                   as Mes
     , year(DataVenda)                    as Ano
     , hour(DataVenda)                    as Hora
     , minute(DataVenda)                  as Minuto
     , date_format(DataVenda, '%Y%m%d')   as AnoMesDia
     , date_format(DataVenda, '%b %Y')    as Mes_Ano
     , DataVenda - interval '3' hour      as "Data-3hs"
     , DataVenda - interval '3' day       as "Data-3days"
     , localtimestamp()                   as hora_atual
     , localtimestamp - interval '3' hour as "DataAtual-3hs"
  FROM fato_vendas v;