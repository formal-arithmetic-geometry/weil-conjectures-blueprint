+++
id = "def-sfb-dc-tensor"
kind = "definition"
title = "$\\otimes^{\\mathrm L}$ on $D_{\\mathrm{cons}}$"
order = 1785
uses = ["lem-sfb-dc-tensor-preserves", "sk-def-sfb-derived-tensor-hom"]
+++
Let $X$ be a scheme of the setting, and let $\Lambda$ be a commutative condensed ring such that
the derived tensor product $-\otimes^{\mathrm L}_{\Lambda_X}-$ of [sk-def-sfb-derived-tensor-hom]
carries pairs of bounded constructible complexes to bounded constructible complexes. By
[lem-sfb-dc-tensor-preserves] this holds for $\Lambda=\underline{\cO}_E,\underline E,\underline{\Qlb}$.
The derived tensor product

$$
-\otimes^{\mathrm L}-\colon D_{\mathrm{cons}}(X,\Lambda)\times D_{\mathrm{cons}}(X,\Lambda)\to D_{\mathrm{cons}}(X,\Lambda)
$$

is its restriction in both variables. For fixed $K$, the functor $K\otimes^{\mathrm L}-$ commutes
with the inclusions.
