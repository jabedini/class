SELECT b.rs_id , c.sample_id, a.clin_sig FROM
snps a NATURAL JOIN snp_freqs b
NATURAL JOIN snp_calls c
NATURAL JOIN samples d
WHERE b.pop=d.pop AND c.call_type='A' AND b.maf > '0.9'
ORDER BY c.sample_id, b.rs_id ASC;
