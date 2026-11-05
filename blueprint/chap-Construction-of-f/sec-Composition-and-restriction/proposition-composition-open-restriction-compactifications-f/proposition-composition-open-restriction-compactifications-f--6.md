+++
id = "proposition-composition-open-restriction-compactifications-f--6"
kind = "proposition"
title = "Construction from a compactification"
order = 530007
aliases = ["bp-r161-6"]
lean = ["AlgebraicGeometry.Etale.rightDerivedUpperShriekOfCompactification", "AlgebraicGeometry.ProEtale.CondensedRing.ContinuousMapRingObj.boundedConstructibleUpperShriekOfCompactification", "AlgebraicGeometry.ProEtale.CondensedRing.PadicIntegersRingObj.boundedConstructibleUpperShriekOfCompactification", "AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructibleUpperShriekOfCompactification"]
uses = ["theorem-existence-exceptional-inverse-image", "definition-compactification-refinement"]
+++
Let $\Lambda$ be a finite commutative ring and let
$c=(X\xrightarrow j\overline X\xrightarrow pY)$ be a compactification of
$f$. Choose the right adjoint $P_p$ of $Rp_*$. The exceptional inverse
image attached to this compactification is defined by
$$
f_c^!=j^*P_p.
$$
The functor $f^!$ is this construction for the chosen compactification of $f$.

For morphisms of separated schemes of finite type over $k$ as in the
shared context, the same construction defines $f_c^!$ on bounded
constructible complexes with coefficients $E$, $\mathcal O_E$, or $\Qbarl$.

Here $P_p$ denotes the chosen right adjoint of $Rp_*$ itself. The
construction does not identify it by definition with the separately
constructed $p^!$, nor does it state uniqueness of a comparison between
$f_c^!$ for different compactifications.
