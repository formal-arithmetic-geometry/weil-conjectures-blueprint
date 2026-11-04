+++
id = "prose-13-01"
kind = "hidden"
title = "Weights"
order = 1046
+++
For the elliptic curve $y^2=x^3-x$ over $\mathbf F_3$ of the introduction,
Frobenius acts on $H^1$ with eigenvalues $\pm i\sqrt3$. The Riemann
hypothesis for this curve is the statement $|\pm i\sqrt3|=3^{1/2}$. But the
eigenvalues live in $\overline{\mathbf Q}_\ell$, and an $\ell$-adic number has no complex
absolute value until we choose a field embedding
$\iota:\overline{\mathbf Q}_\ell\hookrightarrow\mathbf C$. No choice is preferred. We fix one
$\iota$ throughout, and the final theorems hold for every choice.

An eigenvalue $\alpha$ of Frobenius at a closed point of degree $n$ has weight $w$
if $|\iota(\alpha)|=q^{nw/2}$. The factor $n$ makes the weight independent of
the field over which we look at the point: over $\mathbf F_{q^{mn}}$ the
eigenvalue becomes $\alpha^m$ and $q^n$ becomes $q^{mn}$. For example, on $\mathbf P^1$
Frobenius acts on $H^0$ by $1$, of weight $0$, and on $H^2=\overline{\mathbf Q}_\ell(-1)$ by $q$,
of weight $2$. The eigenvalues on $H^1$ of our elliptic curve have weight $1$.
Weil's purity axiom says that this pattern persists: $H^i$ of a smooth proper
variety is pure of weight $i$. The name comes from Hodge theory, where $H^i$
of a compact Kähler manifold carries a Hodge structure of weight $i$.

The proof cannot stay with smooth proper varieties. It fibres them in
curves, and the cohomology of the fibres forms sheaves on the base. So we
need weights for sheaves, and for cohomology that is not pure. Without
smoothness and properness only an upper bound survives. For example, let
$\mathbf G_m=\mathbf P^1\setminus\{0,\infty\}$. The localization sequence gives
$H^1_c(\mathbf G_m,\overline{\mathbf Q}_\ell)=\overline{\mathbf Q}_\ell$ with trivial Frobenius and
$H^2_c(\mathbf G_m,\overline{\mathbf Q}_\ell)=\overline{\mathbf Q}_\ell(-1)$. This agrees with the trace formula
$q-1=\#\mathbf G_m(\mathbf F_q)$. Thus $H^1_c$ has weight $0$, strictly less
than $1$.

A sheaf is pure of weight $w$ if all its eigenvalues at all closed
points have weight $w$. It is mixed if it has a finite filtration whose
quotients are pure. A bounded complex $K$ has weights at most $w$ if each
$\mathcal H^i(K)$ is mixed with all weights at most $w+i$
(Definition [definition-weights]). The shift by $i$ puts the constant
sheaf and its cohomology into one statement: $R\Gamma_c(X,\overline{\mathbf Q}_\ell)$ has weights
at most $0$ exactly when $H^i_c$ has weights at most $i$, as on
$\mathbf G_m$. In these terms Deligne's theorem
(Theorem [theorem-weights-rf-shriek]) says that $Rf_!$ does not increase
weights.

Two warnings will matter later. The first is that weights depend on $\iota$.
Consider the rank-one Weil sheaf on $\operatorname{Spec}\mathbf F_q$ on which
Frobenius acts by $1+\sqrt2\in\overline{\mathbf Q}_\ell$. It has weight $2\log_q(1+\sqrt2)>0$ for
an embedding with $\iota(\sqrt2)=\sqrt2$, and weight
$2\log_q(\sqrt2-1)=-2\log_q(1+\sqrt2)$ for the other one. We learn that the
reciprocal roots of $P_i$ have absolute value $q^{i/2}$ under every complex
embedding (Theorem [theorem-weil-conjectures-smooth-proper-schemes]) only
because Deligne's theorem holds for every $\iota$.

The second warning is that being mixed is not a pointwise condition. Mixedness
asks for a filtration with pure quotients, and we must construct one. Most of Section [chap-Delignes-theorem-in-general] is spent
constructing such a filtration for direct images.

We define weights on Weil sheaves, sheaves on $X$ with a Frobenius
structure, rather than on sheaves on $X_0$. The reason is that normalizing weights
requires twisting by the geometrically constant rank-one Weil sheaves $\mathcal B_b$,
on which a degree-one Frobenius acts by a scalar $b\in\overline{\mathbf Q}_\ell^\times$. These do not come from
$X_0$ when $b$ is not an $\ell$-adic unit.
