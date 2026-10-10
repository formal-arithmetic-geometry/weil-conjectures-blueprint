+++
kind  = "proof"
of    = "lem-sc-cd-ground-field"
+++
For the structure map $f:X\to\operatorname{Spec}K$, the stalk
formula [prop-weil-pbc-strict-henselization-stalk-formula]
identifies the unique geometric stalk of $R^qf_*F$ with
$H^q(X_{K^{\rm sep}},F|)$. Passing from $K^{\rm sep}$ to
$\overline K$ is a purely inseparable algebraic extension,
whose base change is a universal homeomorphism.
Thus [thm-weil-pbc-universal-homeomorphism-invariance]
makes this group zero for $q>e$.
For $F$ killed by $n$, every $R^qf_*F$ is also killed by
$n$. The spectral sequence of [thm-sp-grothendieck]
has terms $H^p(K,R^qf_*F)$, zero unless $p\leq c$ and
$q\leq e$; its total degrees are at most $c+e$.
For arbitrary torsion $F$, pass to the union of the $F[n]$
using [lemma-weil-pbc-torsion-filtered-union], [lem-weil-pbc-cohomology-filtered-colimit].
