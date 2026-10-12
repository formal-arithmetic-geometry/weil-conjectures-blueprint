+++
id = "lem-sc-riemann-roch"
kind = "lemma"
title = "Riemann–Roch on a proper smooth curve"
order = 712
uses = ["def-sc-curves", "def-sc-function-field", "def-sc-genus", "def-sc-invertible-module", "def-sc-pic0"]
lean = ["AlgebraicGeometry.Scheme.eulerChar_free_eq", "AlgebraicGeometry.Scheme.eulerChar_unit_eq"]
+++
Let $k$ be algebraically closed and $C$ a
proper smooth connected curve of genus $g$ ([def-sc-genus]) over
$k$, with generic point $\eta$ and function field $k(C)$
([def-sc-function-field]). For a coherent $\mathcal O_C$-module
$\mathcal F$ put
$\chi(C,\mathcal F):=\sum_q(-1)^q\dim_kH^q(C,\mathcal F)$, let
$\mathcal T\subseteq\mathcal F$ be its torsion subsheaf (the kernel of
$\mathcal F\to\mathcal F_\eta$), and define the *rank* and the
*degree* of $\mathcal F$ by

$$
\operatorname{rk}\mathcal F:=\dim_{k(C)}\mathcal F_\eta,\qquad
\deg\mathcal F:=\dim_kH^0(C,\mathcal T)+\deg\det(\mathcal F/\mathcal T),
$$

where $\mathcal F/\mathcal T$ is locally free of rank
$\operatorname{rk}\mathcal F$ (see the proof),
$\det$ is its top exterior power (with $\det=\mathcal O_C$ in rank
$0$) and $\deg$ on line bundles is that of [def-sc-pic0]; for a line
bundle $\mathcal L$ this is $\operatorname{rk}\mathcal L=1$ and
$\deg\mathcal L$ as in [def-sc-pic0]. Then:

1. (*Riemann–Roch for line bundles.*) For every line bundle
$\mathcal L$ on $C$,

$$
\chi(C,\mathcal L)=\deg\mathcal L+1-g.
$$

In particular $\chi(C,\mathcal O_C)=1-g$.

2. (*Riemann–Roch for coherent modules.*) For every coherent
$\mathcal O_C$-module $\mathcal F$,

$$
\chi(C,\mathcal F)=\deg\mathcal F+\operatorname{rk}(\mathcal F)\,(1-g).
$$
