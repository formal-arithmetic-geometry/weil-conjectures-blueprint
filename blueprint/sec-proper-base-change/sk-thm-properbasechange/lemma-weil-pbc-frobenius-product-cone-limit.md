+++
id = "lemma-weil-pbc-frobenius-product-cone-limit"
kind = "lemma"
title = "Frobenius structures pass through the product cone"
order = 1377
uses = ["def-weil-pbc-adic-derived-inverse-limit", "lemma-weil-pbc-frobenius-level-rectangle", "lemma-weil-pbc-frobenius-tower-compatibility", "lemma-weil-pbc-level-map-derived-limit"]
+++
For $Z=A,B,C,D$, the product-cone limit carries the Weil structure

$$
\Theta_{Z,\infty}:
\Phi_{Y'}Z_\infty
\xrightarrow{\sim}R\varprojlim_n\Phi_{Y'}Z_n
\xrightarrow{R\varprojlim_n\Theta_{Z,n}}Z_\infty.
$$

The first arrow is the canonical comparison, which is an isomorphism because
$\Phi_{Y'}$ is an equivalence and therefore preserves the two products and
the fibre in the product-cone model. Each of $H,V,H',V'$ is Weil-equivariant.
For the common limit map $W:=V'H=H'V:A_\infty\to D_\infty$, the two typed
composites

$$
\begin{aligned}
\Phi_{Y'}A_\infty&\xrightarrow{\Theta_{A,\infty}}A_\infty
\xrightarrow{W}D_\infty,\\
\Phi_{Y'}A_\infty&\xrightarrow{\Phi_{Y'}(W)}\Phi_{Y'}D_\infty
\xrightarrow{\Theta_{D,\infty}}D_\infty
\end{aligned}
$$

are equal.
