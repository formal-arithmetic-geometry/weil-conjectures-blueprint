+++
id = "lemma-nagata-strict-transform-chart-cocycle"
kind = "lemma"
title = "Cocycle for strict-transform charts"
lean = ["AlgebraicGeometry.Scheme.IdealSheafData.StrictTransformChart.comap_ker_strictι_fst_eq"]
order = 179
+++
Let $f\colon Y\to X$ be a morphism, let $\mathcal I$ be a quasi-coherent
ideal on $X$, and put $X'=\operatorname{Bl}_{\mathcal I}(X)$. Let
$c=(U,V,a)$ and $c'=(U',V',a')$ be two chart data: affine opens
$U=\operatorname{Spec}(A)$ of $X$ and $V=\operatorname{Spec}(B)\subseteq
f^{-1}(U)$ of $Y$ and an element $a\in I=\mathcal I(U)$, and likewise
$A',B',I',a'$. Each gives the open immersion
$\operatorname{Spec}(C_a(A,B,I))=V\times_U\operatorname{Spec}(A[I/a])
\to Y\times_XX'$ of a base-changed blow-up chart. Let
$W=\operatorname{Spec}(C_a(A,B,I))\times_{Y\times_XX'}
\operatorname{Spec}(C_{a'}(A',B',I'))$ be the overlap of the two charts.
Then the closed subschemes $\operatorname{Spec}(C_a^{\mathrm{st}}(A,B,I))$
and $\operatorname{Spec}(C_{a'}^{\mathrm{st}}(A',B',I'))$ have the same
restriction to $W$: the ideals $\Gamma_{(a)}(C_a(A,B,I))$ and
$\Gamma_{(a')}(C_{a'}(A',B',I'))$ pull back to the same ideal of
$\mathcal O_W$.
