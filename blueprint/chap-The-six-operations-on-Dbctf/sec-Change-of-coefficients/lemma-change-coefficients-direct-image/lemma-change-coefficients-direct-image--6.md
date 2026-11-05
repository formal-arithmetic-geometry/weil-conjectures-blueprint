+++
id = "lemma-change-coefficients-direct-image--6"
kind = "lemma"
title = "Composition of flat coefficient changes"
order = 635012
aliases = ["bp-r193-6"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.derivedPushHom_comp_app"]
uses = ["definition-change-of-coefficients-maps"]
+++
Let $a:\Lambda\to\Lambda'$, $b:\Lambda'\to\Lambda''$ and $c=b\circ a$ be maps of commutative condensed rings. Assume that extension of scalars along each of $a_Z,b_Z,c_Z$ is exact for every scheme $Z$. Write $T_a^Z$ for derived extension of scalars, and let
$$
\tau_Z:T_c^Z\xrightarrow{\sim}T_b^Z T_a^Z
$$
be its transitivity isomorphism. For every morphism $f:X\to Y$ and every $K\in D(X_{\mathrm{pro}\acute{e}t},\Lambda)$, write $\gamma_a(K)$ for the direct-image comparison. Then
$$
\gamma_c(K)=
Rf_{*,\Lambda''}(\tau_X(K)^{-1})
\circ\gamma_b(T_a^XK)
\circ T_b^Y(\gamma_a(K))
\circ\tau_Y(Rf_{*,\Lambda}K).
$$
Consequently $\gamma_c(K)$ is an isomorphism whenever $\gamma_a(K)$ and $\gamma_b(T_a^XK)$ are isomorphisms. This composition statement assumes flat coefficient changes; it does not assert the corresponding result for arbitrary composites involving finite reductions.
