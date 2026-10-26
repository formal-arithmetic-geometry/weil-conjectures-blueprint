+++
id = "lem-weil-pbc-connected-torsor-subgroup-quotient"
kind = "lemma"
title = "Connected subgroup quotients of a finite etale torsor with geometric fibre cardinality"
uses = ["def-sbc-normal-dominant-galois", "def-weil-pbc-etale-site", "def-weil-pbc-geometric-fibre", "def-weil-pbc-scheme-conventions"]
lean = ["AlgebraicGeometry.Scheme.GaloisCover.exists_connected_subgroup_quotient"]
order = 1681
+++
Let $U$ be a nonempty connected scheme, [def-weil-pbc-scheme-conventions], $Q$ a finite group in its universe, $c:Y\to U$ a connected finite etale $\operatorname{ULift}(Q)$-torsor [def-sbc-normal-dominant-galois], and $H\le Q$ any subgroup. There exist a connected finite etale $v:V\to U$, a connected finite etale $\operatorname{ULift}(H)$-torsor $c_H:Y_H\to V$, and an isomorphism $e:Y_H\simeq Y$ such that $c\circ e=v\circ c_H$. For every separably closed field $\Omega$ in the universe of $U$ and every $s:\operatorname{Spec}\Omega\to U$, the geometric fibre of $v$ [def-weil-pbc-geometric-fibre] has cardinality $[Q:H]$. This statement involves no prime, module sheaf, representation, or associated-sheaf functor.
