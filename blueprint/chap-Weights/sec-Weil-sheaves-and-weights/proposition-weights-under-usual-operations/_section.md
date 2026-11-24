+++
id = "proposition-weights-under-usual-operations"
kind = "proposition"
title = "Weights under the usual operations"
order = 1073
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability", "definition-small-pro-etale-site", "proposition-pro-etale-coverings", "proposition-topos-functoriality", "example-locally-constant-functions-w-local", "proposition-sp-unique-adjoint", "lemma-perfect-complexes-geometric-point", "definition-weights"]
+++
Extensions of [mixed](@definition-weights) sheaves are [mixed](@definition-weights), and an extension of two sheaves with a common upper bound has the same
bound.  Tensor products of [pure](@definition-weights) sheaves of weights $a$ and $b$ are [pure](@definition-weights)
of weight $a+b$, and the dual of a [pure](@definition-weights) [lisse sheaf](@definition-lisse-sheaves) of weight $a$ is
[pure](@definition-weights) of weight $-a$. A tensor product of [mixed](@definition-weights) sheaves of weights at
most $a$ and at most $b$ is [mixed](@definition-weights) of weights at most $a+b$. The dual of
a [mixed](@definition-weights) [lisse sheaf](@definition-lisse-sheaves) is [mixed](@definition-weights), of the negated weights; when its filtration
has [lisse](@definition-lisse-sheaves) graded pieces, their duals are the graded pieces of the
annihilator filtration of the dual.  Inverse image preserves [purity](@definition-weights),
[mixedness](@definition-weights) and their upper bounds.  If a complex $K$ has [weights at most](@definition-weights)
$w$, then $K[r]$ has [weights at most](@definition-weights) $w+r$.

For $b\in\overline{\mathbf Q}_\ell^\times$, let $\mathcal B_b$ be the geometrically constant
rank-one [Weil sheaf](@definition-weil-structure) on which a degree-one Frobenius acts by $b$.
Tensoring by $\mathcal B_b$ adds
$\lambda_\iota(b)=2\log_q|\iota(b)|$ to every weight.  The [Tate sheaf](@definition-tate-twists)
[$\overline{\mathbf Q}_\ell(1)$](@definition-tate-twists) has geometric Frobenius $q^{-1}$, so twisting by [$(r)$](@definition-tate-twists)
subtracts $2r$ from every weight.
