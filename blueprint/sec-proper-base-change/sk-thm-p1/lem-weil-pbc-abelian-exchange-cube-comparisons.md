+++
id = "lem-weil-pbc-abelian-exchange-cube-comparisons"
kind = "lemma"
title = "Homology stalk compatibility of exchange in a commuting cube"
uses = ["def-pc-scheme", "def-weil-pbc-derived-exchange", "def-weil-pbc-derived-inverse-image", "def-weil-pbc-direct-image", "def-weil-pbc-geometric-stalks"]
lean = ["AlgebraicGeometry.Etale.exchangeCube_stalk_square"]
order = 1862
+++
Let $S,T,X,X',S_0,T_0,X_0,X_1$ be schemes [def-pc-scheme], and let
$g\colon T\to S$, $f\colon X\to S$, $g'\colon X'\to X$, $f'\colon X'\to T$,
$j_A\colon S_0\to S$, $j_B\colon T_0\to T$, $g_0\colon T_0\to S_0$, $p_0\colon X_0\to X$,
$f_0\colon X_0\to S_0$, $p_1\colon X_1\to X_0$, $f_1\colon X_1\to T_0$ and $b\colon X_1\to X'$
be morphisms such that the four squares

$$
f\circ g'=g\circ f',\qquad f\circ p_0=j_A\circ f_0,\qquad f_0\circ p_1=g_0\circ f_1,\qquad
f'\circ b=j_B\circ f_1
$$

commute, and suppose $g\circ j_B=j_A\circ g_0$ and $g'\circ b=p_0\circ p_1$. For an abelian
étale sheaf $G$ on $X$ put $K=G[0]$, $K_0=(p_0^*G)[0]$ and

$$
M_1=g^*Rf_*K,\qquad M_2=Rf'_*g'^*K,\qquad N_1=g_0^*Rf_{0*}K_0,\qquad N_2=Rf_{1*}p_1^*K_0
$$

([def-weil-pbc-derived-inverse-image], [def-weil-pbc-direct-image]). Let
$u_1\colon j_B^*M_1\to N_1$ be the inverse-image composition isomorphism along
$g\circ j_B=j_A\circ g_0$, followed by $g_0^*$ of the exchange map of the square
$f\circ p_0=j_A\circ f_0$, followed by the comparison of inverse image with single complexes.
Let $u_2\colon j_B^*M_2\to N_2$ be the exchange map of the square $f'\circ b=j_B\circ f_1$,
followed by the inverse-image composition isomorphism along $g'\circ b=p_0\circ p_1$ and the
comparison of inverse image with single complexes. Let $k$ be a separably closed field,
$t\colon\operatorname{Spec}k\to T_0$ and $s\colon\operatorname{Spec}k\to T$ points with
$j_B\circ t=s$, and $q\in\mathbf Z$. Let $r_i\colon(H^qM_i)_s\to(H^qN_i)_t$ be the
inverse-image stalk comparison followed by the map induced by $H^q(u_i)$
[def-weil-pbc-geometric-stalks]. If $e\colon H^qM_1\to H^qM_2$ and
$e_0\colon H^qN_1\to H^qN_2$ are $H^q$ of the exchange maps
[def-weil-pbc-derived-exchange] of the squares $f\circ g'=g\circ f'$ and
$f_0\circ p_1=g_0\circ f_1$, then

$$
(e_0)_t\circ r_1=r_2\circ e_s .
$$

No isomorphism of $r_i$ or $e$ is asserted.
