+++
id = "lemma-weil-pbc-projection-formula-open-piece"
kind = "lemma"
title = "Open-immersion tensor piece"
order = 1978
lean = ["AlgebraicGeometry.Etale.derivedOpenImmersionLowerShriekProjectionMap", "AlgebraicGeometry.Etale.isIso_derivedOpenImmersionLowerShriekProjectionMap"]
uses = ["def-weil-pbc-projection-compactification"]
+++
Let $j:X\to\overline X$ be the open immersion of a chosen compactification
[def-weil-pbc-projection-compactification]. For every $E$ in the derived
category of sheaves on $X_{\Et}$ and every $F$ in the derived category of
sheaves on $\overline X_{\Et}$, the canonical map

$$
j_!(E\otimes^LLj^*F)
\longrightarrow(j_!E)\otimes^LF,
$$

adjoint under $j_!\dashv j^*$ to
$E\otimes^LLj^*F\to j^*j_!E\otimes^LLj^*F\cong j^*(j_!E\otimes^LF)$ (unit of
the adjunction, then compatibility of $Lj^*$ with $\otimes^L$), is an
isomorphism, natural in $E$ and $F$. Its inverse

$$
\theta_j:(j_!E)\otimes^LF\xrightarrow{\sim}j_!(E\otimes^LLj^*F)
$$

is the *open-piece isomorphism*.
