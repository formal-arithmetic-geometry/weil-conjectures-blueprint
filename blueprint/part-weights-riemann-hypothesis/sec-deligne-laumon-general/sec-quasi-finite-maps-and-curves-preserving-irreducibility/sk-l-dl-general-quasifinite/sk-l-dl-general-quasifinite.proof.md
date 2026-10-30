+++
kind = "proof"
of = "sk-l-dl-general-quasifinite"
+++
We first treat a finite map and then reduce to it by Zariski's main
theorem. For a finite map, exactness follows from
Lemma [sk-lem-pbc-finite] and the comparison of coefficients. By the same
lemma, the stalk at a geometric point $\bar y$ over a closed point $y$
is the direct sum of the stalks at the geometric points of $Z_0$ over
$\bar y$, and the local Frobenius at $y$ permutes these summands. For a point $z$ of residue degree
$e=[\kappa(z):\kappa(y)]$, Frobenius cycles through $e$ summands, and
its $e$th power on each of them is conjugate to the local Frobenius at
$z$. Hence each eigenvalue $\beta$ on this cycle satisfies
$\beta^e=\alpha$ for an eigenvalue $\alpha$ at $z$. If the input has
weight $w$, then

$$
|\iota(\beta)|^e=|\iota(\alpha)|=q_z^{w/2}=q_y^{ew/2},
$$

so $|\iota(\beta)|=q_y^{w/2}$. Hence finite direct image preserves
purity.

In general, $Y_0$ is Noetherian and hence quasi-compact and
quasi-separated, and so Zariski's main theorem in the form
[Stacks, Tag 05K0](https://stacks.math.columbia.edu/tag/05K0) applies. It shows that $g$ factors as an open immersion
$j:Z_0\hookrightarrow\overline Z_0$ followed by a finite map
$\bar g:\overline Z_0\to Y_0$. By
Proposition [sk-thm-sf-comp-composition] we have
$Rg_!=\bar g_*j_!$, and both functors are exact. Extension by zero
preserves purity, since its other stalks are zero. As $j$ and $\bar g$
are defined over $k_0$, these exact functors carry a finite mixed
filtration by Weil subsheaves to one of the same kind, with pure
quotients of the same weights, and we obtain the assertion on sheaves.
Since $Rg_!$ is exact, it commutes with taking cohomology sheaves, and
the assertion on $D_{\leq w}$ follows.
