+++
id = "lem-zl-mixed-punctual-cutoff"
kind = "lemma"
title = "Punctual cutoff for an already mixed sheaf"
order = 3180
lean = ["AlgebraicGeometry.LAdicWeilSheaf.IsMixedOfWeightsAtMost.of_hasWeightsAtMost"]
uses = ["def-weil-pbc-constructible-complexes", "def-weil-pbc-scheme-conventions", "def-weil-punctual-weights", "p-linear-filtration"]
+++
Fix the finite field, coefficient field and embedding $\iota$ of
[def-weil-punctual-weights].
Let $\mathcal G$ be a
constructible
$\Qlb$-Weil sheaf on a
separated finite-type
$k_0$-scheme $Y_0$. Assume that for some $u\in\mathbf R$
it is $\iota$-mixed of weights
at most $u$. Let $v\in\mathbf R$, and suppose that at every
closed point $y$ every eigenvalue $\alpha$ of local Frobenius
on $\mathcal G_{\bar y}$ satisfies
$|\iota(\alpha)|\leq q_y^{v/2}$.
Then $\mathcal G$ is $\iota$-mixed of weights at most $v$.
