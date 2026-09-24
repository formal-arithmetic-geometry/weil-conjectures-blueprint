+++
id = "sbc-def-base-change-property"
kind = "definition"
title = "The recorded base-change property $BC(f,n,q_0)$"
order = 2763
uses = ["def-weil-pbc-scheme-conventions", "sbc-def-base-change-map", "sbc-def-base-change-square", "sbc-def-coefficient-conventions"]
+++
Let $f:X\to S$ be a
morphism of schemes,
$n\geq1$, $q_0\geq0$, and put $\Lambda=\mathbf Z/n\mathbf Z$.
We say that *$BC(f,n,q_0)$ holds*, or that *the recorded
base-change property holds for $f$, $n$ and $q_0$*, if for every
base-change square of
[sbc-def-base-change-square] whose horizontal side $g:T\to S$ is
quasi-compact and
quasi-separated, and every abelian sheaf $\mathcal F$ on $T_{\Et}$
annihilated by $n$, the base-change maps
$\operatorname{BC}^q_{f,g}(\mathcal F)$ of
[sbc-def-base-change-map] are isomorphisms for every $q\leq q_0$;
equivalently, the derived base-change map
$\operatorname{BC}_{f,g}(\mathcal F)$ of
[sbc-def-base-change-map] is an isomorphism on $q$-th cohomology
sheaves for all $q\leq q_0$, those cohomology sheaves being the maps
$\operatorname{BC}^q_{f,g}(\mathcal F)$ of degree $q$. The
smooth-base-change theorem of this chapter is the assertion
$BC(f,n,q)$ for every $q$.
