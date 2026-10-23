+++
id = "lem-sf-reduction-compatibility"
kind = "lemma"
title = "Finite reduction commutes with pullback and compact-support direct image"
lean = ["AlgebraicGeometry.Etale.reductionModIdeal", "AlgebraicGeometry.Etale.leftDerivedUpperStarReductionModIdealIso", "AlgebraicGeometry.Etale.nonempty_iso_reductionModIdeal_leftDerivedUpperStar", "AlgebraicGeometry.Etale.rightDerivedLowerShriekReductionModIdealMap", "AlgebraicGeometry.Etale.isIso_rightDerivedLowerShriekReductionModIdealMap", "AlgebraicGeometry.Etale.nonempty_iso_reductionModIdeal_rightDerivedLowerShriek_of_finite"]
order = 2771
uses = ["def-weil-pbc-derived-categories", "def-weil-derived-pullback-tensor-hom", "def-nagata-compactification", "def-amb-etale-compact-support", "lemma-weil-pbc-projection-formula-compactified", "lemma-weil-pbc-projection-formula-open-piece", "lemma-weil-pbc-projection-formula-proper-piece", "lem-amb-proper-coproducts-projection"]
+++
Let $\Lambda$ be a commutative ring and $J\subseteq\Lambda$ an ideal. For a
scheme $W$ let $(\Lambda/J)_W$ be the constant sheaf of $\Lambda$-modules with
value $\Lambda/J$, placed in degree $0$, and let

$$
\rho_W=-\otimes^L_\Lambda(\Lambda/J)_W:\ D(W_{\Et},\Lambda)\longrightarrow D(W_{\Et},\Lambda)
$$

be the *reduction modulo $J$* on the derived category of sheaves of
$\Lambda$-modules on the small étale site [def-weil-pbc-derived-categories],
formed with the derived tensor product [def-weil-derived-pullback-tensor-hom].
The reduction $\rho_WK$ is kept as a complex of $\Lambda$-modules.

1. For every morphism of schemes $f:X\to Y$ there is an isomorphism of functors
$$
Lf^*\circ\rho_Y\cong\rho_X\circ Lf^*:\ D(Y_{\Et},\Lambda)\to D(X_{\Et},\Lambda),
$$
namely the monoidality isomorphism
$Lf^*\bigl(L\otimes^L_\Lambda(\Lambda/J)_Y\bigr)\cong Lf^*L\otimes^L_\Lambda Lf^*(\Lambda/J)_Y$
followed by the identification $Lf^*(\Lambda/J)_Y\cong(\Lambda/J)_X$.
1. Let $f:X\to Y$ be a morphism with a compactification
$c=(X\xrightarrow{j}\overline X\xrightarrow{r}Y)$
[def-nagata-compactification], and let $Rf^c_!=Rr_*\circ j_!$ be the
compact-support direct image computed with $c$ [def-amb-etale-compact-support].
For $K\in D(X_{\Et},\Lambda)$ let
$$
\rho_Y(Rf^c_!K)=Rf^c_!K\otimes^L_\Lambda(\Lambda/J)_Y\longrightarrow
Rf^c_!\bigl(K\otimes^L_\Lambda Lf^*(\Lambda/J)_Y\bigr)\cong Rf^c_!(\rho_XK)
$$
be the projection map of $c$ at $(K,(\Lambda/J)_Y)$
[lemma-weil-pbc-projection-formula-compactified], followed by
$Lf^*(\Lambda/J)_Y\cong(\Lambda/J)_X$; it is natural in $K$. If $\Lambda$ is
finite, this comparison is an isomorphism for every $K$. In particular, for
$\Lambda$ finite and $f$ admitting a compactification,
$\rho_Y\circ Rf_!\cong Rf_!\circ\rho_X$ for the compact-support direct image
$Rf_!$ formed with the chosen compactification of $f$.
