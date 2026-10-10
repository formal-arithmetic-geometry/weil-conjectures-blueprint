+++
kind  = "proof"
of    = "lem-fd-as-cover-affine-line"
+++
By [lem-fd-as-cover] for $f=x$, the covering ring of the Artin–Schreier
sheaf family [def-fd-artin-schreier-sheaf] is
$k_0[T]/(T^p-T-x)$; the $k_0[x]$-algebra map $k_0[T]/(T^p-T-x)\to k_0[y]$, $T\mapsto y$, is well defined because $y^p-y=x$, and it is surjective. Both sides are free of rank $p$ over $k_0[x]$: the source is free by definition; for the target, the relation $y^p=x+y$ expresses every element as $\sum_{i<p}c_i(x)y^i$ with $c_i\in k_0[x]$, and such a sum vanishes only if all $c_i=0$, since the terms have leading degrees $p\deg c_i+i$, which are pairwise distinct modulo $p$ and hence cannot cancel (the map $k_0[x]\to k_0[y]$, $x\mapsto y^p-y$, is injective). A surjective $k_0[x]$-linear map between free modules of the same finite rank is injective, so the map is an isomorphism. The formulas for $\pi$ and for the action $T\mapsto T+a$ read off as $x=y^p-y$ and $y\mapsto y+a$.
