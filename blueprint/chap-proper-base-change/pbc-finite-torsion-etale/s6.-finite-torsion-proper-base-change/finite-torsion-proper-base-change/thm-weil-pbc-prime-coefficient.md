+++
id = "thm-weil-pbc-prime-coefficient"
kind = "theorem"
title = "Prime-coefficient proper base change"
order = 1831
uses = ["def-weil-pbc-property-detailed", "def-weil-pbc-scheme-conventions", "prop-weil-pbc-projective-line-detailed", "prop-weil-pbc-reduction-to-projective-line-detailed"]
+++
For every prime $r$, every proper $f:X\to Y$ that is locally of finite
presentation, every cartesian base change, and every sheaf $F$ of $\mathbf
F_r$-modules on $X_{\Et}$, the specified map

$$
 g^{-1}Rf_*F\xrightarrow{\sim}Rf'_*g'^{-1}F
$$

is an isomorphism.

## Proof

The projective-line proposition [prop-weil-pbc-projective-line-detailed]
supplies the hypothesis of the reduction proposition
[prop-weil-pbc-reduction-to-projective-line-detailed], and that proposition
yields $\mathrm{PBC}(f)$ for every proper $f$ in the sense of
[def-weil-pbc-property-detailed]; the displayed map is exactly the exchange morphism of
that property, hence an isomorphism.
