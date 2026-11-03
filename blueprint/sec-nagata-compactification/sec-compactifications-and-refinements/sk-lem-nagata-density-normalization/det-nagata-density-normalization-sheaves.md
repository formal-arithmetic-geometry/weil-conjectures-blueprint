+++
id = "det-nagata-density-normalization-sheaves"
kind = "lemma"
title = "Extension by zero through the schematic closure"
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructibleOpenImmersionLowerShriekRefinement", "AlgebraicGeometry.ProEtale.CondensedRing.isIso_boundedConstructibleOpenImmersionLowerShriekRefinement", "AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructibleOpenImmersionLowerShriekRefinementPushforward", "AlgebraicGeometry.ProEtale.CondensedRing.isIso_boundedConstructibleOpenImmersionLowerShriekRefinementPushforward", "AlgebraicGeometry.ProEtale.CondensedRing.isIso_boundedConstructibleOpenImmersionLowerShriekRefinementPushforward_padicAlgCl"]
order = 1352
uses = ["det-nagata-density-normalization-setup", "lem-cbc-proetale-extension-zero", "lem-cbc-proetale-extension-zero-base-change", "lem-exc-proetale-closed-essential-image", "lem-exc-proetale-closed-exact", "lem-weil-extension-by-zero-exact"]
+++
In the situation of [det-nagata-density-normalization-setup], assume that
$X$ and $\overline X$ are separated schemes of finite type over a field $k$
of positive characteristic different from $\ell$, and let $\Lambda$ be the condensed
coefficient ring of a finite extension $E/\Ql$ or of $\Qlb$, with pulled-back
coefficient sheaves $\Lambda_X,\Lambda_Z,\Lambda_{\overline X}$. For every
bounded constructible complex $K\in D^b_c(X,\Lambda)$:

1. the *restriction comparison* $j_{Z,!}K\to i^*j_!K$, the map adjoint under
   $j_{Z,!}\dashv j_Z^*$ to the identification
   $K\cong j^*j_!K\cong j_Z^*i^*j_!K$, is an isomorphism;
1. the *pushforward comparison*
   $$
   j_!K\longrightarrow Ri_*i^*j_!K\cong Ri_*j_{Z,!}K,
   $$
   the unit of $i^*\dashv Ri_*$ followed by the inverse of the restriction
   comparison, is an isomorphism.

Since $i_*$ is exact, $Ri_*j_{Z,!}K=i_*j_{Z,!}K$, so $j_!K\simeq i_*j_{Z,!}K$
in $D^b_c(\overline X,\Lambda)$.
