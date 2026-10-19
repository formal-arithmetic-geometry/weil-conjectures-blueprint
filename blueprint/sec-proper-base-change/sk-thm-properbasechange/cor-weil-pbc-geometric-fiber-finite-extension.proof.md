+++
kind  = "proof"
of    = "cor-weil-pbc-geometric-fiber-finite-extension"
uses = ["sk-cor-pbc-proet-finite", "det-thm-sfb-proper-base-change-integral"]
+++
Apply the proper base change isomorphism of [sk-thm-sfb-proper-base-change],
with $\Lambda=E$, to the cartesian square defined by $\bar y$. The point
$\operatorname{Spec}\Omega$ need not be of finite type over $k$, but the proof
of the $E$-case ([det-thm-sfb-proper-base-change-rational] (3)) uses on the
base only that $\bar y^*$ is exact and commutes with $\otimes^{\mathbf L}$ and
with inverting $\ell$, together with base change for the integral and finite
reductions, which holds for an arbitrary morphism $g:Y'\to Y$
([sk-cor-pbc-proet-finite], [det-thm-sfb-proper-base-change-integral] (3)).
Direct image along the proper morphism $a_{\bar y}$ commutes with inverting
$\ell$ by [det-thm-sfb-proper-base-change-rational] (1), whose proof uses only
that $a_{\bar y}$ is qcqs.
