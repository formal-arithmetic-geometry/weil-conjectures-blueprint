+++
kind  = "proof"
of    = "thm-cbc-finite-level-proetale"
+++
Choose a compactification $c=(j,p)$ of $f$ with base change
$c'$ as in [def-cbc-compact-support-square]. The etale
statement of [thm-cbc-finite-torsion] applies to the etale
representative $L$: the etale exchange map
$\operatorname{Ex}_!(L)$ is an isomorphism. Transporting it to
the pro-etale site: the fully faithful comparison
$\nu_T^*$ of [thm-weil-pbc-site-comparison] (the interface
`OBL-PBC-SITE-COMPARISON` of the proper-base-change chapter) carries the
direct-image parts by
[lem-weil-pbc-transport-identifies-exchange] (and
[prop-weil-pbc-comparison-direct-image]), and the
extension-by-zero factors by the comparisons
[lem-cbc-proetale-extension-zero-comparison] (etale to
pro-etale) and [lem-cbc-proetale-extension-zero-base-change]
(pro-etale base change); the transported composite is the pro-etale
map of [def-cbc-exchange-map] for $K=\nu_X^*L$. Independence
of the witness follows from the functoriality of the transported map and
the notion of an etale-origin witness of
[def-weil-pbc-etale-origin-witness].
