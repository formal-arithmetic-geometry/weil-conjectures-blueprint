+++
id = "lemma-finite-morphisms--2"
kind = "lemma"
title = "Finite morphisms (2)"
name_showing = false
order = 384002
aliases = ["bp-r116-2"]
lean = ["AlgebraicGeometry.Etale.preservesFiniteColimits_lowerStar_of_isFinite", "AlgebraicGeometry.Etale.isIso_baseChangeMap_of_isFinite"]
uses = ["lemma-finite-morphisms--1", "definition-underived-base-change-map"]
+++
Let $u:V\to W$ and $A$ be as in [lemma-finite-morphisms--1]. Suppose moreover
that $A$ is concrete, with a forgetful functor to sets that reflects
isomorphisms and preserves filtered colimits.

If this forgetful functor carries $A$-valued sheaves on $W_{\acute{e}t}$ to
sheaves of sets, then $u_*$ from $A$-valued sheaves on $V_{\acute{e}t}$ to
$A$-valued sheaves on $W_{\acute{e}t}$ is exact.

For any base change $g:W'\to W$, write $V'=V\times_W W'$ with projections
$g':V'\to V$ and $u':V'\to W'$. If the forgetful functor carries $A$-valued
sheaves on $W'_{\acute{e}t}$ to sheaves of sets, the underived base change map
[definition-underived-base-change-map]

$$
g^*u_*F\longrightarrow u'_*g'^*F
$$

is an isomorphism for every $A$-valued sheaf $F$ on $V_{\acute{e}t}$.
For abelian sheaves and sheaves of modules over a constant coefficient ring,
these conditions hold on every scheme, so $u_*$ is exact and commutes with
arbitrary base change.
