+++
kind  = "proof"
of    = "lem-weil-pbc-proper-open-comparison-proetale"
+++
Apply the exact functor $\nu^*$ from
[thm-weil-pbc-site-comparison] to the etale isomorphism
[lem-weil-pbc-proper-open-comparison-iso].
The right side is identified with the pro-etale direct image by
[prop-weil-pbc-comparison-direct-image]; properness gives its
quasi-compact and quasi-separated hypothesis.

For the left side, the comparison morphism in
[def-weil-pbc-site-comparison-morphism] satisfies
$j_{\Et}^{-1}\nu_{T,*}G=\nu_{X,*}j_{\Proet}^{-1}G$:
both evaluate a pro-etale sheaf $G$ on the same etale objects over
the open $X$. Taking left adjoints, using the adjunctions in
[def-weil-pbc-extension-by-zero], [def-weil-extension-by-zero], gives

$$
\nu_T^*j_{\Et,!}\simeq j_{\Proet,!}\nu_X^*.
$$

All these functors are exact, so the identity holds on complexes.
It transports the etale comparison map to the displayed map.
The identifications are natural and commute with composition;
thus [lem-weil-pbc-proper-open-comparison-composition] transports
its identity and composition law as well.
