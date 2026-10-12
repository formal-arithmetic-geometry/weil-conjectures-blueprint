+++
kind  = "proof"
of    = "lem-wf-additive-characters-h1"
+++
At level $n$, [lem-wf-finite-constant-h1-pi1] gives

$$
H^1(U,A_n)\cong
\operatorname{Hom}_{\mathrm{cont}}(\pi_1(U,\bar u),A_n).
\tag{3.3}
$$

Its naturality shows that the transition map is reduction modulo
$\ell^n$. A compatible family on the right of (3.3) gives, point by
point, a homomorphism to
$\varprojlim_nA_n=\mathbf Z_\ell$. It is continuous because the inverse
image of $\ell^n\mathbf Z_\ell$ is the open kernel of its level-$n$
reduction. Conversely, reducing a continuous $\mathbf Z_\ell$-valued
homomorphism gives such a family. This proves (3.2). The explicit
Weil-descent computation in [lem-wf-finite-constant-h1-pi1], together
with [def-wf-weil-group], gives precomposition by
$g\mapsto s^{-1}gs$, which is the asserted Frobenius action.
