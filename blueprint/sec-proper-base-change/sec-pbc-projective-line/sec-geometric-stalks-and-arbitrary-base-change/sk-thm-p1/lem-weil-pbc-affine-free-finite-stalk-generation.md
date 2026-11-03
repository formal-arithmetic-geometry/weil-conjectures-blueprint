+++
id = "lem-weil-pbc-affine-free-finite-stalk-generation"
kind = "lemma"
title = "Finite affine free maps generating one module stalk"
uses = ["def-pc-scheme", "def-weil-pbc-etale-sheaves", "def-weil-pbc-etale-site", "def-weil-pbc-geometric-stalks"]
lean = ["AlgebraicGeometry.Scheme.exists_finset_affine_free_stalk_surjective"]
order = 1788
+++
Let $X$ be a scheme [def-pc-scheme], $\Lambda$ a commutative ring, and $F$ a sheaf of $\Lambda$-modules on its small etale site [def-weil-pbc-etale-site], [def-weil-pbc-etale-sheaves]. For $x\in X$, let $\bar x$ be the geometric point given by an algebraic closure of its residue field. Assume $F_{\bar x}$ [def-weil-pbc-geometric-stalks] is finitely generated over $\Lambda$. For an etale object $W$, let $P_W$ be the sheafification of $V\mapsto\Lambda^{(\operatorname{Hom}_X(V,W))}$. Set $I=\{(W,f):W\text{ affine etale over }X, f:P_W\to F\}$. There is a finite subset $S\subset I$ such that the stalk map of $\bigoplus_{(W,f)\in S}P_W\to F$, induced by the maps $f$, is surjective at $\bar x$. No finiteness of the ring, constructibility, or compactness of the scheme is assumed.
