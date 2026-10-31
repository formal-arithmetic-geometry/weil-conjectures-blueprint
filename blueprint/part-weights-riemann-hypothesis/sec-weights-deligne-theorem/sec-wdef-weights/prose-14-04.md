+++
id = "prose-14-04"
kind = "hidden"
title = "Weil sheaves and weights (3)"
order = 632
+++
There are more Weil sheaves than sheaves on $X_0$. For instance, if
$b\in \overline{\mathbf Q}_\ell^\times$ is not an $\ell$-adic unit, the geometrically
constant rank-one Weil sheaf on which a degree-one Frobenius acts by $b$
does not come from $X_0$. We need these sheaves, denoted $\mathcal B_b$
in Proposition [sk-r-real-linear], to normalize weights.

The definition below has to produce a class of complexes that $Rf_!$
preserves, and this decides its form. Purity is too strong, since
$R\Gamma_c(\mathbf G_m,\overline{\mathbf Q}_\ell)$ is not pure although $\overline{\mathbf Q}_\ell$ is. A bound on the eigenvalues at
each closed point, the condition of being punctually of weights $\le w$,
is what the curve case gives on each stalk of a direct image, but it is
too weak to be fed back into the curve case, which applies to pure
lisse sheaves. A sheaf with a finite filtration whose quotients are pure
can be treated one quotient at a time, and so mixedness is defined by
such a filtration. For a sheaf known to be mixed, the bound on weights
is again a pointwise condition (the first remark after the definition),
and Lemma [sk-lem-wgen-punctual-cutoff] uses this to turn the stalkwise
bounds into the bound of Theorem [sk-cor-dl-general-complex]. The
normalization by $q_x^{w/2}$ gives the constant sheaf weight $0$ and
$\overline{\mathbf Q}_\ell(1)$ weight $-2$.
