+++
id = "sk-prop-sf-existence"
kind = "section"
title = "Existence of the exceptional right adjoint"
order = 1801
lean = ["AlgebraicGeometry.Etale.rightDerivedUpperShriekAdjunction", "AlgebraicGeometry.ProEtale.rightDerivedUpperShriekAdjunction"]
+++
*Proposition (sketch).*

(a) *On the ordinary derived categories of the small étale sites*: if
$f:X\to S$ is compactifiable between Noetherian schemes, the functor
$Rf_!=Rr_*j_!:D(X_{\Et},A)\to D(S_{\Et},A)$ has a right adjoint
$f^{\times}:D(S_{\Et},A)\to D(X_{\Et},A)$; no restriction to a constructible
subcategory is made. (b) *On the small pro-étale sites*:
if $\operatorname{FullCD}(p,A;c)$ holds for the proper part $p$ of a
compactification of a separated finite-type $f$, then
$Rf_{!,n}:D(X_{\Proet},A)\to D(Y_{\Proet},A)$ preserves
coproducts and therefore has a right adjoint
$Rf_n^{\times}:D(Y_{\Proet},A)\to D(X_{\Proet},A)$, and the
adjunction is independent of the compactification.
Chapter 14 (smooth duality on the ordinary derived category):
thm:amb-etale-exceptional-adjoint, by Brown representability (Stacks
`0F5Y`) applied to the exact coproduct-preserving $Rf_!$; Chapter 30
for (b), prop:ambient-exceptional-adjoint.
part (b) is conditional on $\operatorname{FullCD}$, i.e. on clause (1)
of [sk-def-sf-admissible]. On the étale-origin class the bound
$\operatorname{FullCD}(p,A;2\dim\overline X)$ is
[sk-prop-sf-fullcd-etale-origin], a consequence of
[sk-prop-sf-finiteness] and [sk-prop-sf-comparison]. What remains open is
the vanishing for pro-étale module sheaves that are *not* of étale
origin, and with it the coproduct preservation of $Rp_*$ on the whole of
$D(\overline X_{\Proet},A)$, which is what Brown representability needs for
the *ambient* adjoint asserted in (b); see
[sk-rem-sf-fullcd-scope].
*Note: clause (b), the ambient adjoint on all of $D(X_{\Proet},A)$, seems
never to be used later; downstream uses only the adjunction relative to the
class of étale origin (bounded-below $K$ of étale origin), which holds
unconditionally, so (b) has no detailed counterpart in the blueprint.*

Uses: `def-weil-full-cohomological-dimension`, `thm-amb-etale-exceptional-adjoint`, `thm-amb-etale-exceptional-adjoint`
