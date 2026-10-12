+++
id = "def-weil-pbc-intrinsic-completion"
kind = "definition"
title = "Intrinsic derived completion"
order = 1314
uses = ["def-weil-pbc-adic-coefficient-datum", "def-weil-pbc-derived-inverse-limit"]
+++
For $m\geq1$, let

$$
 Q_m=K(A_T;a_1^m,\dots,a_r^m)
   =\bigotimes_{j=1}^r[A_T\xrightarrow{a_j^m}A_T]
$$

in cohomological degrees $[-r,0]$. For each factor define a chain map

$$
 [A_T\xrightarrow{a_j^{m+1}}A_T]
 \longrightarrow[A_T\xrightarrow{a_j^m}A_T]
$$

whose degree $-1$ component is multiplication by $a_j$ and whose degree $0$
component is the identity. Their tensor product is a chain map
$q_{m+1,m}:Q_{m+1}\to Q_m$; the composites $q_{m+2,m}=q_{m+1,m}q_{m+2,m+1}$
make $(Q_m)_m$ a strict tower.

For a functorial K-flat representative $QK$, the complexes
$QK\otimes_{A_T}Q_m$ form an object of $D(\operatorname{Tow}_{A}(T))$. Define

$$
 K^{\wedge}_{\mathrm{Kos}}
   =\Rlim_m(QK\otimes_{A_T}Q_m).
$$

The compatible degree-zero maps $A_T\to Q_m$ define $K\to
K^{\wedge}_{\mathrm{Kos}}$. The object $K$ is derived $I$-complete if this
map is an isomorphism.
