+++
kind = "proof"
of = "proposition-twisting-weight-zero-adding-dual--5"
order = 1194012
uses = ["proposition-twisting-weight-zero-adding-dual--4", "proposition-weights-under-usual-operations"]
+++
At a closed point $x$, identify the stalk of $\mathcal E$ with the direct
sum of the stalk of $\mathcal F^0$ and its Frobenius-module dual.
By [proposition-twisting-weight-zero-adding-dual--4], the first stalk is
pure of weight zero. Its complex eigenvalues $\beta_j$ have absolute
value one, so the dual eigenvalues are
$\beta_j^{-1}=\overline{\beta_j}$. Thus the product of the two local
polynomials has real coefficients. Lean applies
`FrobeniusModule.IsPureOfWeight.isReal_prod_dual` and transports the
local polynomial along the stalk equivalences for a direct sum and a dual.
