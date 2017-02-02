DELETE FROM assocs WHERE effect_allele_frequency is NULL and measure='Self Well-Being' or effect_allele_frequency is NULL and measure='Life Satisfaction';



DELETE FROM assocs WHERE effect_allele_frequency is NULL and (measure='Self Well-Being' or  measure='Life Satisfaction');
