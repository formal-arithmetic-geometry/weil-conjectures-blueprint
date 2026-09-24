+++
id = "closed-immersions-on-the-ambient-pro-etale-site"
kind = "section"
title = "Closed immersions on the ambient pro-etale site"
order = 1417
uses = ["def-weil-pbc-ind-etale-algebra", "def-weil-pbc-ind-etale-basis", "def-weil-pbc-proetale-modules", "def-weil-pbc-proetale-operations", "def-weil-pbc-proetale-site", "def-weil-pbc-scheme-conventions", "lem-weil-pbc-ind-etale-basis", "lem-weil-pbc-ind-etale-stability"]
+++
In the sheaf and derived statements of this section, coefficients are in a
fixed finite commutative ring $\Lambda$. The algebra constructions use
arbitrary commutative base rings and arbitrary ideals; the finiteness of
$\Lambda$ imposes no finiteness condition on those rings or ideals.

The section builds, by explicit algebra, a left adjoint $v$ to base change
along a closed immersion on the affine ind-etale basis
[def-exc-closed-site-lift]. The input is that an etale finite-presentation
algebra is exactly one with a square Jacobian presentation
[def-exc-jacobian-presentation], [lem-exc-etale-jacobian-presentation], so
that such an algebra lifts across an *arbitrary* quotient — no nilpotence
hypothesis — by lifting the presentation coefficientwise and inverting the
Jacobian [def-exc-etale-algebra-lift], [lem-exc-etale-algebra-lift]. Taking
the filtered colimit [lem-exc-closed-lift-filtered] over all etale
factorizations gives the ind-etale lift $H_A$
[def-exc-ind-etale-closed-lift], whose units [lem-exc-closed-lift-units],
reduction [lem-exc-closed-lift-reduction] and Jacobson-radical property
[lem-exc-closed-lift-jacobson] yield the algebra adjunction
[lem-exc-closed-lift-adjunction]. Its opposite is the site adjunction
[lem-exc-closed-site-adjunction]; it preserves coverings
[lem-exc-closed-site-lift-coverings] and hence computes closed inverse image
as the sheafification of $V\mapsto F(v(V))$
[lem-exc-closed-inverse-image-formula].
