+++
id = "lemma-finite-morphisms-cohomology--2"
kind = "lemma"
title = "Base change for finite direct image"
name_showing = false
order = 1594002
aliases = ["bp-r497-2"]
lean = ["AlgebraicGeometry.Etale.isIso_baseChangeMap_of_isFinite"]
uses = ["definition-underived-base-change-map"]
+++
Let $h:Y\to C$ be a finite morphism of schemes and let $a:C'\to C$
be any morphism. Write $Y'=Y\times_C C'$, with projections $b:Y'\to Y$
and $h':Y'\to C'$. For every abelian sheaf $G$ on $Y_{\acute{e}t}$,
the canonical base change map of [definition-underived-base-change-map]

$$
a^*h_*G\longrightarrow h'_*b^*G
$$

is an isomorphism, naturally in $G$.

The same holds for sheaves with values in a Grothendieck abelian
category $\mathcal A$ admitting small-site sheafification and a faithful
forgetful functor to sets which reflects isomorphisms, preserves
filtered colimits, and takes $\mathcal A$-valued sheaves on
$C'_{\acute{e}t}$ to sheaves of sets. In particular, it holds for
sheaves of modules over any ring.
