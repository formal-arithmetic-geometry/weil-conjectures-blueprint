+++
id = "lem-pc-perfect-locus"
kind = "lemma"
title = "The perfect locus with fixed degree"
order = 764
uses = ["def-pc-base-change", "def-pc-derived-category", "def-pc-derived-pullback", "def-pc-invertible-in-degree-zero", "def-pc-morphism-conventions", "def-pc-perfect-complex"]
lean = ["AlgebraicGeometry.Scheme.Modules.IsFiniteFreeComplex.exists_opens_range_subset_iff"]
+++
Let $X$ be a scheme and let $P$ be a bounded complex of finite free
$\mathcal{O}_X$-modules concentrated in degrees $[0,d]$, representing a
perfect object $E\in D(\mathcal{O}_X)$. Given integers $i,r\ge0$ there is
an open subscheme $U\subseteq X$ characterized by the property: a
morphism $f:Y\to X$ factors through $U$ if and only if
$Lf^*E=f^*P$ is isomorphic to a locally free $\mathcal{O}_Y$-module of
rank $r$ placed in degree $i$, that is, the cohomology sheaves
$H^q(f^*P)$ vanish for $q\neq i$ and $H^i(f^*P)$ is finite locally free
of rank $r$.
