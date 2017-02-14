SELECT gene_id, count(rs_id) FROM snps WHERE chromosome='14' AND position BETWEEN 30000000 AND 80000000 GROUP BY gene_id ORDER BY count(rs_id) DESC;
