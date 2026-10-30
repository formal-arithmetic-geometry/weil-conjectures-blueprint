+++
id = "sk-lem-wft-compact-kunneth"
kind = "lemma"
title = "Künneth formula for compact supports"
order = 718
uses = ["sk-prop-cohsm", "sk-thm-sf-package", "sk-thm-sf-kunneth-relative", "sk-def-sf-weil-complexes", "sk-def-sp-trace", "sk-prop-sp-trace-composition", "sk-prop-sp-purity-bc"]
tags = ["sketch"]
+++
Let $f:X\to S$ and $g:Y\to S$ be separated morphisms of finite type,
let $h:X\times_SY\to S$ be the structure map, and let $K,L$ be bounded
constructible complexes with coefficients in a field. There is a
canonical isomorphism

$$
Rf_!K\otimes Rg_!L
\simeq Rh_!(K\boxtimes_SL).
$$

It respects Weil structures and, for smooth maps, the trace maps for
cohomology with compact support.

*Complement.* The isomorphism is the inverse of the relative Künneth map
$\kappa^{\mathrm{rel}}_{K,L}$ of [sk-thm-sf-kunneth-relative] for $B=S$, and
so has the coherences recorded there (symmetry, triple products, base change).
