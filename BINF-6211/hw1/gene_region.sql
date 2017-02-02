SELECT s.snp_id, s.position, s.gene_symbol, a.measure, a.effect_allele_frequency FROM snps s LEFT OUTER JOIN assocs a ON (s.snp_id = a.snp_id)
WHERE s.chromosome='9' and s.position BETWEEN 4153000 AND 8863000
ORDER BY s.position ASC;
