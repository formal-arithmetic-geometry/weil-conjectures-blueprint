+++
kind = "proof"
of = "lemma-triviality-fibres--1"
order = 1475004
uses = ["theorem-chow-s-lemma-projective-form"]
+++
The fibre $X_t$ is integral and proper over $\kappa(t)$, so its ring
of global functions is a field. Properness also makes the cohomology
of an invertible sheaf on $X_t$ finite-dimensional. Lean obtains this
finiteness from the coherent-cohomology theorem, whose proof uses
Chow's lemma [theorem-chow-s-lemma-projective-form]. Thus
$h^0(X_t,\mathcal A_t)>0$ is equivalent to the existence of a nonzero
section of $\mathcal A_t$, and likewise for $\mathcal B_t$.

Pull back $\mathcal A\otimes\mathcal B\simeq\mathcal O_X$ to $X_t$.
If $\mathcal A_t$ is trivial, this isomorphism also trivializes
$\mathcal B_t$, and both sheaves have the nonzero section $1$.
Conversely, let $s$ and $s'$ be nonzero sections of the two sheaves.
Their tensor product is nonzero because $X_t$ is integral. Under the
chosen isomorphism it is therefore a unit in $H^0(X_t,\mathcal O_{X_t})$.
Locally write $s=ae$ and $s'=be'$ in free generators. The product
$ab$ is a unit, so $a$ is a unit. Hence $s$ is a global free generator
and trivializes $\mathcal A_t$.
