+++
id = "lemma-bounding-weights-mixed-sheaf--1"
kind = "lemma"
title = "Punctual bounds and mixed filtrations"
order = 1063001
aliases = ["bp-r326-1"]
lean = ["AlgebraicGeometry.WeilSheaf.IsMixedOfWeightsAtMost.hasWeightsAtMost", "AlgebraicGeometry.WeilSheaf.IsMixedOfWeightsAtMost.of_hasWeightsAtMost"]
uses = ["definition-ind-etale-pro-etale-weakly--3", "definition-small-pro-etale-site--1", "proposition-pro-etale-coverings--2", "proposition-topos-functoriality--2", "example-locally-constant-functions-w-local--1", "definition-weil-structure--3", "definition-weights--3", "definition-weights--5"]
+++
Let $X_0$ be locally of finite type over $\Fq$, put
$X=X_0\times_{\Fq}\Fbar$, and let $K$ be a constructible Weil
$\overline{\mathbf Q}_\ell$-sheaf on $X$, where $\ell\nmid q$.
Fix an embedding
$\iota:\overline{\mathbf Q}_\ell\hookrightarrow\mathbf C$ and a real
number $w$. If $K$ is mixed of weights at most $w$, then it is
punctually of weights $\le w$: at every closed point $x$ of $X_0$,
each eigenvalue $\alpha$ of $\operatorname{Frob}_x$ on $K_{\bar x}$
satisfies $|\iota(\alpha)|\le q_x^{w/2}$.

If moreover $X_0$ is separated of finite type, $K$ is mixed of
weights at most some real number $u$, and $K$ is punctually of
weights $\le w$, then $K$ is mixed of weights at most $w$.
Thus, for a mixed sheaf in the setting of this chapter, the two
upper bounds are equivalent.
