+++
id = "def-weil-pbc-finite-etale-trace-splitting-data"
kind = "definition"
title = "Explicit splitting data, splitting presieve, and local sum"
uses = ["def-weil-pbc-etale-site", "def-weil-pbc-scheme-conventions"]
lean = ["AlgebraicGeometry.Etale.FiniteEtaleTraceSplitting", "AlgebraicGeometry.Etale.finiteEtaleTraceSplitPresieve", "AlgebraicGeometry.Etale.FiniteEtaleTraceSplitting.sectionMap", "AlgebraicGeometry.Etale.FiniteEtaleTraceSplitting.sum"]
order = 1526
+++
Let $f:Y\to X$ be a morphism of schemes [def-weil-pbc-scheme-conventions] and
$T\to X$ an object of the small etale site [def-weil-pbc-etale-site], with
projection $p:T\times_XY\to T$. A *splitting* of $T$ for $f$ consists of a
finite index type $J$ (possibly empty), schemes $V_j$ ($j\in J$), morphisms
$i_j:V_j\to T\times_XY$ which are both open and closed immersions and exhibit
$T\times_XY$ as the coproduct $\coprod_jV_j$, and morphisms $t_j:T\to V_j$
inverse to $p\circ i_j$, i.e. $p\,i_j\,t_j=\mathrm{id}_T$ and
$t_j\,p\,i_j=\mathrm{id}_{V_j}$. All these data are part of the structure.

The *split presieve* on an object $W$ of the site consists of all arrows
$T\to W$ such that $T$ admits a splitting for $f$.

If $f$ is etale, then $T\times_XY$, with the composite
$T\times_XY\to Y\xrightarrow{f}X$, is an object of the small etale site of
$X$, and each sheet gives a section $i_j\circ t_j:T\to T\times_XY$ over $X$.
For an abelian sheaf $F$ on $X_{\mathrm{et}}$, the *local sum* of a splitting
is the map

$$
F(T\times_XY)\longrightarrow F(T),\qquad
s\longmapsto\sum_{j\in J}F(i_j\circ t_j)(s).
$$
