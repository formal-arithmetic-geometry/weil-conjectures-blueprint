+++
kind  = "proof"
of    = "det-lem-integral-models-stacks"
+++
By [sk-prop-integral-criterion], $K\in\Dbc(X,\cO_E)$ iff $K$ is derived complete and
$K\otimes^{\mathbf L}_{\cO_{E,X}}(\cO_E/\pi_E)_X\in\Dbc(X,\cO_E/\pi_E)$. By
[det-prop-integral-criterion-constant-coefficients] (2), (3), $K$ is derived complete iff
$\operatorname{Res}K$ is (completeness is a property of the underlying complex of sheaves of
$\cO_E$-modules, the limit of its reductions), and the reductions of $K$ and of
$\operatorname{Res}K$ modulo $\pi_E$ coincide. Over the field $\cO_E/\pi_E$ every bounded complex
has finite Tor dimension, and conversely a complex of finite Tor dimension with constructible
cohomology in the sense of \stacks{09C1} is bounded (its cohomology is bounded, being the
cohomology of a complex of finite Tor dimension over a field evaluated against
$\cO_E/\pi_E$). The constructibility conditions agree by the pro-étale/étale comparison of
constructible complexes with torsion coefficients ([sk-thm-pe-constructible-comparison]).
Hence the two conditions are equivalent. Since $\operatorname{Res}$ is an equivalence on
derived complete objects ([det-prop-integral-criterion-constant-coefficients] (2)) and the
conditions correspond, it restricts to an equivalence of the full subcategories.
