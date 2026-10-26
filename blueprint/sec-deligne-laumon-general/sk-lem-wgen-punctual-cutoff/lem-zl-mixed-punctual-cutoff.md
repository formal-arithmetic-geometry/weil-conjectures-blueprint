+++
id = "lem-zl-mixed-punctual-cutoff"
kind = "lemma"
title = "Punctual cutoff for an already mixed sheaf"
order = 4066
lean = ["AlgebraicGeometry.WeilSheaf.IsMixedOfWeightsAtMost.of_hasWeightsAtMost"]
uses = ["def-weil-pbc-scheme-conventions", "def-weil-punctual-weights", "p-linear-filtration", "sk-lem-coefficient-heart", "sk-d-real-weights"]
+++
Fix the finite field, coefficient field and embedding $\iota$ of
[def-weil-punctual-weights].
Let $\mathcal G$ be a
constructible
$\Qlb$-Weil sheaf ([sk-lem-coefficient-heart], [def-weil-punctual-weights]) on a
separated finite-type
$k_0$-scheme $Y_0$. Assume that for some $u\in\mathbf R$
it is $\iota$-mixed of weights
at most $u$. Let $v\in\mathbf R$, and suppose that at every
closed point $y$ every eigenvalue $\alpha$ of local Frobenius
on $\mathcal G_{\bar y}$ satisfies
$|\iota(\alpha)|\leq q_y^{v/2}$.
Then $\mathcal G$ is $\iota$-mixed of weights at most $v$.
