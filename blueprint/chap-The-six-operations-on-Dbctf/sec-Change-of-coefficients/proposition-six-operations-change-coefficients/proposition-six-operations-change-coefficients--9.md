+++
id = "proposition-six-operations-change-coefficients--9"
kind = "proposition"
title = "Direct image: transitivity in coefficients"
order = 645018
aliases = ["bp-r197-9"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.derivedPushHom_comp_app"]
uses = ["definition-change-of-coefficients-maps"]
+++
Let $a:\Lambda\to\Lambda'$, $b:\Lambda'\to\Lambda''$ and $c:\Lambda\to\Lambda''$ be morphisms of commutative condensed rings with $c=ba$. Assume that extension of scalars along each of their pullbacks to every scheme is exact. Write $T_a^X,T_b^X,T_c^X$ for the derived scalar extensions, $s_X:T_c^X\simeq T_b^XT_a^X$ for their transitivity isomorphism, and $\gamma_a,\gamma_b,\gamma_c$ for the direct-image comparisons.

For any morphism of schemes $f:X\to Y$ and any unbounded $K\in D(X_{\mathrm{pro}\acute{e}t},\Lambda)$,
$$
\gamma_c(K)=Rf_{*,\Lambda''}(s_X^{-1}(K))\circ
\gamma_b(T_a^XK)\circ T_b^Y(\gamma_a(K))\circ s_Y(Rf_{*,\Lambda}K).
$$
This is an equality of comparison maps; their invertibility is not assumed.
