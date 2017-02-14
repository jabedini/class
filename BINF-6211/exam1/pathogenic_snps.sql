SELECT count(rs_id) FROM snps  NATURAL JOIN snp_freqs WHERE  clin_sig='Pathogenic' AND maf > 0.01 AND pop='global';
