+++
id = "prop-nagata-rees-localization"
kind = "theorem"
title = "Graded localization of the Rees algebra"
order = 85
lean = ["AlgebraicGeometry.AffineBlowup.isLocalization_away_map"]
tags = ["latex:proposition"]
uses = ["def-nagata-homogeneous-localization-degree-zero", "def-nagata-rees-algebra", "def-nagata-rees-localization-map", "def-nagata-rees-piece", "lemma-nagata-localization-rees-piece", "lemma-nagata-rees-degree-one-element", "lemma-nagata-rees-degree-zero", "lemma-nagata-rees-piece-mul", "prop-nagata-rees-graded"]
+++
Let $s\in A$, let $\varphi\colon A\to B$ be a localization of $A$ away from
$s$, let $J=IB$, and let $a\in I$. Then the ring homomorphism

$$
\mathcal R_A(I)_{(at),0}\longrightarrow\mathcal R_B(J)_{(\varphi(a)t),0}
$$

induced by $\rho_\varphi\colon\mathcal R_A(I)\to\mathcal R_B(J)$ of
[def-nagata-rees-localization-map] makes the target a localization of the
source away from the image of $s$.
