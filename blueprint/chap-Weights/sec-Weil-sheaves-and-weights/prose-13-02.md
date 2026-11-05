+++
id = "prose-13-02"
kind = "hidden"
title = "Weil sheaves and weights (1)"
order = 1055
+++
Weights are defined by the absolute values of the Frobenius
eigenvalues on stalks at closed points, so we first fix how Frobenius
acts on sheaves.

On a smooth curve $U_0$ we want to treat lisse Weil sheaves as
representations, just as a lisse sheaf on $U_0$ is a continuous
representation of $\pi_1(U_0)$. However, the profinite group $\pi_1(U_0)$ is an extension of $\widehat{\mathbf Z}$ by $\pi_1(U)$, and it has too few
representations for this. Indeed, a continuous representation of a profinite group preserves a lattice, so a lift $s$ of Frobenius acts with
eigenvalues that are $\ell$-adic units. Hence the rank-one Weil sheaf
$\mathcal B_\ell$, on which $s$ acts by $\ell$ and $\pi_1(U)$ acts trivially,
is not a representation of $\pi_1(U_0)$. Concretely,
$n\mapsto\ell^n$ does not extend continuously to $\widehat{\mathbf Z}$: the
integers $m!$ tend to $0$ in $\widehat{\mathbf Z}$, whereas $\ell^{m!}$ tends
to $0$ in $\mathbf Z_\ell$ and not to $1$.

The Weil group keeps $\pi_1(U)$ with its topology and replaces
$\widehat{\mathbf Z}$ by the discrete group $\mathbf Z$ of integer powers
of Frobenius. Continuity then constrains only the geometric part. These representations of the Weil group are the language of Theorem [theorem-rank-one-sheaves-have-finite] and of the monodromy groups
of Section [sec-Determinant-weights].
