+++
id = "lem-kun-open-immersion-restriction"
kind = "lemma"
title = "Inverse image along an open immersion is a left inverse of direct image"
order = 6060
lean = ["AlgebraicGeometry.Etale.openImmersion_pullback_pushforward_eq_id"]
uses = ["lem-kun-leray-bdd"]
+++
Let $j:U\to X$ be an open immersion. Then $j^{-1}j_*=\mathrm{id}$ on
$\Ab(U_{\Et})$, and for every $F\in D(U_{\Et})$ the canonical morphism
$R\Gamma(X_{\Et},Rj_*F)\to R\Gamma(U_{\Et},F)$ of [lem-kun-leray-bdd] is an
isomorphism (Leray for $j$).

## Proof

For an étale $V\to U$, the direct image gives
$(j_*F)(V)=F(V\times_XU)=F(V)$, because $V\times_XU=V$ since $V\to X$
factors through the open $U$; this is $j^{-1}j_*=\mathrm{id}$. The second
assertion is [lem-kun-leray-bdd] applied to $j$.

Unresolved dependencies: def:weil-pbc-scheme-conventions, def:weil-pbc-direct-image
