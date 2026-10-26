+++
id = "sk-lem-wft-compact-kunneth"
kind = "lemma"
title = "Compact-support Künneth"
order = 3944
uses = ["sk-prop-sf-cbc", "sk-thm-sf-package", "sk-thm-sf-kunneth-relative", "sk-def-sf-weil-complexes", "sk-def-sp-trace", "sk-prop-sp-trace-composition", "sk-prop-sp-purity-bc"]
tags = ["sketch"]
+++
For separated finite-type maps $a:X\to S$ and $b:Y\to S$,
with $c:X\times_SY\to S$, and bounded constructible field-coefficient
complexes $K,L$, there is a canonical isomorphism

$$
 Ra_!K\otimes Rb_!L
       \simeq Rc_!(K\boxtimes_SL).
$$

Over a point, this is the Künneth isomorphism for cohomology with
compact support. It respects Weil structures and, for smooth maps, the
trace maps for cohomology with compact support.

*Complement.* The isomorphism is the inverse of the relative Künneth map
$\kappa^{\mathrm{rel}}_{K,L}$ of [sk-thm-sf-kunneth-relative] for $B=S$, and
so has the coherences recorded there (symmetry, triple products, base change).
