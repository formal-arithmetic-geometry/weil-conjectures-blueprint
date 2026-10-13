+++
id = "def-sfb-dc-hom"
kind = "definition"
title = "$\\RHom$ on $D_{\\mathrm{cons}}$"
order = 1790
uses = ["lem-sfb-dc-hom-preserves", "sk-def-sfb-derived-tensor-hom"]
+++
Let $X$ be a scheme of the setting, and let $\Lambda$ be a commutative condensed ring such that
the derived internal hom $\RHom_{\Lambda_X}(-,-)$ of [sk-def-sfb-derived-tensor-hom] carries pairs
of bounded constructible complexes to bounded constructible complexes. By
[lem-sfb-dc-hom-preserves] this holds for $\Lambda=\underline{\cO}_E,\underline E,\underline{\Qlb}$.
The derived internal hom

$$
\RHom(-,-)\colon D_{\mathrm{cons}}(X,\Lambda)^{\mathrm{op}}\times D_{\mathrm{cons}}(X,\Lambda)\to D_{\mathrm{cons}}(X,\Lambda)
$$

is its restriction in both variables. For fixed $K$, the functor $\RHom(K,-)$ commutes with the
inclusions.
