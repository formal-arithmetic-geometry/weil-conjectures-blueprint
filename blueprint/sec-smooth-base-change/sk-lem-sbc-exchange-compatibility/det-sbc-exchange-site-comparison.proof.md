+++
kind = "proof"
of = "det-sbc-exchange-site-comparison"
uses = ["det-sbc-exchange-formal", "lem-weil-pbc-comparison-pullback", "prop-weil-pbc-comparison-direct-image"]
+++
Both exchange maps are built in the same way from three ingredients: the composition
isomorphism for inverse images, the counit of $f^*\dashv Rf_*$ and the unit of
$f'^*\dashv Rf'_*$ (the second description of the exchange map as
$\eta_{f'}$ followed by $Rf'_*u^*\epsilon_f$). The comparison isomorphism of
[lem-weil-pbc-comparison-pullback] is compatible with composites and with the cartesian
identification, so it carries the étale composition isomorphism
$f'^{-1}g^{-1}\simeq u^{-1}f^{-1}$ to the pro-étale one. The isomorphism of
[prop-weil-pbc-comparison-direct-image] is the mate of the inverse-image comparison, so it
is compatible with units and counits of the adjunctions $f^{-1}\dashv Rf_{\mathrm{\acute et},*}$
and $f^*\dashv Rf_*$ on the bounded-below categories, and likewise for $f'$. Applying
$\nu_{Y'}^*$ to the étale composite and inserting these identifications term by term gives the
pro-étale composite defining $\operatorname{Ex}_{g,f}(\nu_X^*K)$ in [det-sbc-exchange-formal].
