+++
id = "lem-sf-fullcd-detection-equivalence"
kind = "lemma"
title = "The full cohomological-dimension condition is a bound on the pro-étale cohomology of the source base-changed to weakly contractible objects"
lean = ["AlgebraicGeometry.ProEtale.hasUniformCohomologicalDimensionLE_iff_forall_ext"]
order = 2140
uses = ["cor-sf-fullcd-weakly-contractible-test", "def-weil-derived-cohomology-sheaves", "def-weil-full-cohomological-dimension", "def-weil-pbc-direct-image", "def-weil-pbc-proetale-site", "lem-sf-proetale-vanishing-detection", "thm-sp-grothendieck"]
+++
In the setting of [def-weil-full-cohomological-dimension] the condition
$\operatorname{FullCD}(p,A;c)$ is equivalent to the following statement: for
every object $V\to Y$ of $Y_{\Proet}$
([def-weil-pbc-proetale-site]), every affine weakly contractible object
$W\to V$ of $V_{\Proet}$ and every sheaf $\mathcal F$ of
$A$-modules on $\overline X_{\Proet}$, with $p_V$ and $(p_V)_*$ as in
the derived direct image of [def-weil-pbc-direct-image], one has

$$
H^r\bigl((\overline X\times_YW)_{\Proet},\mathcal F|_{\overline X\times_YW}\bigr)=0
\qquad(r\in\mathbf Z,\ r>c),
$$

the cohomology being that of the small pro-étale site of the source
$\overline X\times_YV$ base-changed along $W\to V$, which is
$\overline X\times_YW$.

*The test objects must be weakly contractible.* The same vanishing over
every object $V\to Y$ of $Y_{\Proet}$, with $\overline X\times_YV$ in
place of $\overline X\times_YW$, is not equivalent to
$\operatorname{FullCD}(p,A;c)$: for $p=\mathrm{id}_Y$ the higher direct
images vanish, so $\operatorname{FullCD}(\mathrm{id}_Y,A;0)$ holds, while
$H^r(V_{\Proet},\mathcal F|_V)\neq0$ for some $r>0$ in general (for
instance $V=Y$ a smooth projective connected curve over $\overline{\mathbf F}_q$
and $\mathcal F$ the constant sheaf $A$, with
$H^2(Y_{\Proet},A)\cong H^2(Y_{\Et},A)\cong A(-1)\neq0$). The Leray argument of
the proof collapses only over weakly contractible bases.
