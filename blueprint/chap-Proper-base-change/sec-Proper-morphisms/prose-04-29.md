+++
id = "prose-04-29"
kind = "hidden"
title = "Proper morphisms (1)"
order = 383
+++
Proper base change for an arbitrary proper morphism follows from the
case of the projective line
(Proposition [proposition-proper-base-change-projective-line]) by
formal steps. Finite morphisms satisfy proper base change
directly, and Lemma [lemma-composition-cancellation] shows that the
property is stable under composition and descends along proper
surjections. Descent along a proper surjection $u:X\to Y$ works because
every injective sheaf on $Y$ is a direct summand of $u_*J$ for an
injective sheaf $J$ on $X$, and the hypotheses on $u$ and on the
composite keep $u_*J$ acyclic after base change.

The steps are then as follows. First, composition gives the projection of
$(\mathbf P^1)^n$. Then descent along the finite surjection
$(\mathbf P^1)^n\to\mathbf P^n$ gives the projection of $\mathbf P^n$,
and with it every projective morphism. Finally, by Chow's lemma every proper
morphism is dominated by a projective one through a proper surjection,
so a last descent covers all proper morphisms.
