+++
id = "lem-sc-ample-positive-degree"
kind = "lemma"
title = "Ample modules on proper curves have positive degree"
lean = ["AlgebraicGeometry.Scheme.Hom.degree_pos_of_isAmple"]
order = 545
uses = ["def-sc-ample", "def-sc-curves", "def-sc-hilbert-degree", "lem-sc-hilbert-polynomial"]
+++
Let $k$ be algebraically closed, $C$ a proper curve over $k$ of
dimension one (in the sense of [def-sc-curves]; $C$ need not be
connected and may have zero-dimensional connected components), and
$\mathcal L$ an ample invertible $\mathcal O_C$-module
([def-sc-ample]). Then $\deg\mathcal L>0$, where
$\deg\mathcal L:=\deg_{\mathcal L}(C)=\chi(C,\mathcal L)-\chi(C,\mathcal O_C)$
is the degree of [def-sc-hilbert-degree] (with $g=\dim C=1$), i.e. the
coefficient of $m$ in the Hilbert polynomial
$m\mapsto\chi(C,\mathcal L^{\otimes m})$ of [lem-sc-hilbert-polynomial].
In particular $\mathcal L$ is not trivial.

The hypothesis $\dim C=1$ cannot be dropped: on the proper curve
$C=\operatorname{Spec}k$ of dimension zero every invertible module, ample
or not, is trivial and $\chi(C,\mathcal L^{\otimes m})=1$ for all $m$, so
$\chi(C,\mathcal L)-\chi(C,\mathcal O_C)=0$, while the degree
$\deg_{\mathcal L}(C)$ of [def-sc-hilbert-degree] (now with $g=0$) is
$\chi(C,\mathcal O_C)=1$.
