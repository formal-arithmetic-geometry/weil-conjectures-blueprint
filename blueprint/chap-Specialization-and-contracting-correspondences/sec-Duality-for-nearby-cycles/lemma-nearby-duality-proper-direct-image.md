+++
id = "lemma-nearby-duality-proper-direct-image"
kind = "lemma"
title = "Duality for nearby cycles and proper direct image"
order = 1667
lean = ["CategoryTheory.Verdier.nearbyDualityMap_proper", "CategoryTheory.Verdier.nearbyDualityMap_restrict", "AlgebraicGeometry.ProEtale.CondensedRing.NearbyCyclesModel.isIso_lowerStar_nearbyDualityMap_of_isProper"]
+++
Let $f:X\to Y$ be a proper morphism of separated $S$-schemes of finite
type, and let $M\in D^b_{\mathrm{ctf}}(X_\eta,A)$. Under the
isomorphism $\chi_f$ and the Verdier duality isomorphisms
$Rf_*\mathbb D\simeq\mathbb DRf_*$ of Section [chap-Verdier-and-Poincare-duality] on
both fibres,

$$
Rf_{s*}\delta_{X,M}\quad\text{is identified with}\quad
\delta_{Y,Rf_{\eta*}M}.
\tag{E.14}
$$

For an open immersion $j:U\to X$, the restriction $j_s^*\delta_{X,M}$ is
$\delta_{U,j_\eta^*M}$ under the base change isomorphism $\alpha_j$. If
$X$ is proper over $S$, then under global Verdier duality on both fibres

$$
R\Gamma(X_s,\delta_{X,M})
\quad\text{is identified with the identity of}\quad
R\operatorname{Hom}_A(R\Gamma(X_{\bar\eta},M),A).
\tag{E.15}
$$
