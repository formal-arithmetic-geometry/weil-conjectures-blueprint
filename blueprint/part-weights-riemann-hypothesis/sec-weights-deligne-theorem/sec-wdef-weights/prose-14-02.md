+++
id = "prose-14-02"
kind = "hidden"
title = "Weil sheaves and weights"
order = 628
+++
Weights are defined by the absolute values of the Frobenius
eigenvalues on stalks at closed points, so we first fix how Frobenius
acts on sheaves.

On a smooth curve $U_0$ we want to treat lisse Weil sheaves as
representations, just as a lisse sheaf on $U_0$ is a continuous
representation of $\pi_1(U_0)$. The profinite group has too few
representations for this. It is an extension of $\widehat{\mathbf Z}$ by $\pi_1(U)$, and a
continuous representation of a profinite group preserves a lattice, so
a lift $s$ of Frobenius acts with eigenvalues that are $\ell$-adic units.
On the Weil sheaf $\mathcal B_b$ with $b=\ell$, the element $s$ would have
to act by $\ell$, and $n\mapsto\ell^n$ does not extend continuously from
$\mathbf Z$ to $\widehat{\mathbf Z}$: the integers $m!$ tend to $0$ in
$\widehat{\mathbf Z}$, whereas $\ell^{m!}$ tends to $0$ and not to $1$.
The Weil group keeps $\pi_1(U)$ with its topology and replaces
$\widehat{\mathbf Z}$ by the discrete group $\mathbf Z$ of integer powers
of Frobenius, so that continuity constrains only the geometric part. Its
representations are exactly the lisse Weil sheaves, and this is the
language of Theorem [sk-p-real-rankone] and of the monodromy groups
of Section [sec-determinant-weights].
