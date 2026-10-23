+++
kind  = "proof"
of    = "sk-l-dl-general-quasifinite"
+++
For a finite map, exactness follows from [sk-lem-pbc-finite]
and the comparison of coefficients. The stalk at a closed point $y$ is
the direct sum of the stalks at the points of its geometric fibre, and
Frobenius permutes these summands. For a point $z$ of residue degree
$e=[\kappa(z):\kappa(y)]$, Frobenius cycles through $e$ summands, and
its $e$th power on each of them is conjugate to the local Frobenius at
$z$. Hence each eigenvalue $\beta$ on this cycle satisfies
$\beta^e=\alpha$ for an eigenvalue $\alpha$ at $z$. If the input has
weight $w$, then

$$
 |\iota(\beta)|^e=q_z^{w/2}=q_y^{ew/2}.
$$

This proves that finite direct image preserves purity. A nonreduced
fibre causes no trouble, since nilpotents do not change the category
of sheaves.

By Zariski's main theorem, in the form
[Stacks, Tag 05K0](https://stacks.math.columbia.edu/tag/05K0), which
applies because $Y_0$ is Noetherian and hence quasi-compact and
quasi-separated, $g$ factors as an open immersion
$j:Z_0\hookrightarrow\overline Z_0$ followed by a finite map
$\bar g:\overline Z_0\to Y_0$. By [sk-thm-sf-comp-composition],
$Rg_!=\bar g_*j_!$, and both functors are exact. Extension by zero
preserves purity, since its other stalks are zero. Applying these
exact functors to a finite mixed filtration proves the assertion on
sheaves, and taking the cohomology sheaves of a complex proves the
assertion on $D_{\leq w}$. The factorization and the composition maps
are defined over $k_0$, so the resulting filtrations are
Weil-equivariant.
