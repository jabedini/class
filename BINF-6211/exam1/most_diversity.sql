SELECT t2.rs_id, t2.pop, (t2.maf-t1.maf) AS sub FROM snp_freqs  t1 cross join snp_freqs  t2 WHERE t1.pop<>'EUR' AND t2.pop='global' ORDER BY sub DESC limit 5; 
