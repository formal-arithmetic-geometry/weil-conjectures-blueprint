+++
id = "sk-thm-derived-duality"
kind = "section"
title = "Degreewise duality over a field"
order = 2437
lean = ["AlgebraicGeometry.Etale.isPerfectPairing_poincarePairing", "AlgebraicGeometry.Etale.TateOrientation.isPerfectPairing_poincarePairing", "AlgebraicGeometry.Etale.degreewisePoincarePairing", "AlgebraicGeometry.Etale.isPerfPair_degreewisePoincarePairing", "AlgebraicGeometry.Etale.isPerfPair_degreewisePoincarePairing_of_isProper", "AlgebraicGeometry.Etale.untwistedDegreewisePoincarePairing", "AlgebraicGeometry.Etale.exists_untwistedDegreewisePoincarePairing_eq", "AlgebraicGeometry.Etale.bijective_untwistedDegreewisePoincarePairing", "AlgebraicGeometry.Etale.bijective_untwistedDegreewisePoincarePairing_flip"]
uses = ["sk-def-pairing", "sk-lem-finite", "sk-thm-sf-identification"]
+++
*Corollary (sketch).*

In the setting of [sk-def-set] and [sk-def-pairing], let $K$ be perfect over
$\Lambda_X$ and let $\Lambda$ be a field coefficient stage.
The derived pairing of [sk-thm-sf-identification] gives perfect pairings

$$
\langle-,-\rangle_i:H^i_c(X,K)\times H^{2d-i}\bigl(X,K^\vee(d)\bigr)
\longrightarrow\Lambda.
$$

The line-valued form takes values in $\Lambda(-d)$; for proper $X$
the same holds with $H_c$ replaced by $H$.
(Blueprint 15, prop:pod-degree-of-the-pairing,
thm:pod-degreewise-perfectness-over-a-field.)

## Proof

Over a field stage a bounded complex of finite-dimensional spaces
splits as $\bigoplus_jH^j(C)[-j]$, so
$H^{-i}(C^\vee)\cong H^i(C)^\vee$
(lem:pod-cohomology-of-dual-over-field).
Apply this to the perfect point complexes of [sk-lem-finite] and
the derived isomorphism of [sk-thm-sf-identification].
Eliminating the twist through
$\Lambda(d)\otimes_\Lambda\Lambda(-d)\cong\Lambda$ gives the
line-valued form. For proper $X$, $Ra_{X!}\cong Ra_{X*}$, so
$H_c$ may be replaced by $H$.

*Formalisation stage.* The degreewise statements are formalised first
for a *finite* field $\Lambda$ (an $\mathbb F_\ell$-algebra that is a
field), at which the six operations and [sk-lem-finite] are available.
The stages $E$ and $\Qlb$ are not yet covered. They are meant to follow
by the same argument once the six operations are transported to them
([sk-thm-purity-transport]): the derived isomorphism and the
perfectness of the point complexes hold there, and the splitting of a
perfect complex over a field is stage-independent. The line-valued form is
obtained from $\langle-,-\rangle_i$ by composing with linear isomorphisms
$H^j(X,K^\vee)\cong H^j(X,K^\vee(d))$ and $\Lambda\cong\Lambda(-d)$,
which exist since $k$ is separably closed.

Uses: [sk-def-pairing], [sk-lem-finite], [sk-thm-sf-identification]
