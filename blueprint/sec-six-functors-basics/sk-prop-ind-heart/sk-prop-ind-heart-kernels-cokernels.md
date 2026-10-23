+++
id = "det-ind-heart-kernels-cokernels"
kind = "lemma"
title = "Kernels and cokernels of ind-constructible sheaves"
order = 2230
uses = ["det-ind-heart-canonical-presentation", "det-ind-heart-full-faithfulness", "sk-lem-coefficient-heart"]
+++
Let $\Lambda=E$ or $\Qlb$ and $f\colon B\to B'$ a morphism in $\IndCons(X,\Lambda)$. Let $P_f$ be the
category of commutative squares consisting of a map $v\colon C\to D$ in $\Cons(X,\Lambda)$ and maps
$C\to B$, $D\to B'$ compatible with $f$. Then $P_f$ is filtered, the projections $P_f\to J(B)$ and
$P_f\to J(B')$ are cofinal, $f=\varinjlim_{P_f}v$, and

$$
\ker f=\varinjlim_{P_f}\ker v,\qquad\coker f=\varinjlim_{P_f}\coker v
$$

lie in $\IndCons(X,\Lambda)$.
