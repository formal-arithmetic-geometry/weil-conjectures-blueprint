+++
id = "lem-sc-kummer-exact"
kind = "lemma"
title = "Exactness of the Kummer sequence"
order = 876
uses = ["def-sc-curves", "def-sc-kummer-sequence"]
lean = ["AlgebraicGeometry.Scheme.kummerSequence_shortExact"]
+++
Let $X$ be a scheme (for instance a curve $C$ over algebraically
closed $k$, [def-sc-curves]) and let $n$ be a natural number which is
invertible in $\Gamma(X,\mathcal O_X)$ (for a curve over $k$: $n$ prime
to $\operatorname{char}k$). The Kummer sequence of
[def-sc-kummer-sequence] is a short exact sequence of sheaves on
$X_{\Et}$.

## Proof

The first map is the inclusion of $\mu_n$, which is the kernel of
$t\mapsto t^n$ by definition, so it is a monomorphism and the
sequence is exact at the first $\mathbf G_m$. It remains to show
that $t\mapsto t^n$ is an epimorphism of etale sheaves, i.e. that
every section of $\mathbf G_m$ is etale locally an $n$-th power.

Let $u:U\to X$ be etale and $t\in\mathcal O_U(U)^*$. The image of
$n$ under the ring map $\Gamma(X,\mathcal O_X)\to\mathcal O_U(U)$ is
again a unit, so $n\in\mathcal O_U(U)^*$. If $n=0$, then $0$ is a
unit of $\mathcal O_U(U)$, so $\mathcal O_U(U)=0$, $U$ is empty and
there is nothing to prove; assume $n\geq1$. Put
$V:=\underline{\operatorname{Spec}}_U\,\mathcal O_U[x]/(x^n-t)\to U$.
Then $V\to U$ is finite and flat, $\mathcal O_V$ being locally free
of rank $n$ over $\mathcal O_U$ because the polynomial is monic. It
is surjective: the fibre over a point $p\in U$ is
$\operatorname{Spec}\kappa(p)[x]/(x^n-t(p))$, a $\kappa(p)$-algebra
of dimension $n\geq1$, hence nonempty. It is unramified: locally
over an affine open $\operatorname{Spec}A\subseteq U$ we have
$V=\operatorname{Spec}A[x]/(f)$ with $f=x^n-t$, and for such a
relative complete intersection
$\Omega_{V/U}=A[x]/(f,f')$ with $f'=nx^{n-1}$. In
$B:=A[x]/(x^n-t)$ the element $x$ is a unit (as $x\cdot x^{n-1}=t$ is
a unit) and $n$ is a unit, so $nx^{n-1}$ is a unit, and

$$
\Omega_{V/U}=A[x]/(x^n-t,\,nx^{n-1})=0 .
$$

A morphism is etale if and only if it is locally of finite
presentation, flat and unramified, so $V\to U$ is finite etale and
surjective, i.e. an etale covering of $U$. On $V$ the pullback of
$t$ is $x^n$, the $n$-th power of the unit $x\in\mathcal O_V(V)^*$.
Hence $t\mapsto t^n$ is locally surjective, so it is an epimorphism
of sheaves on $X_{\Et}$, and the Kummer sequence
([def-sc-kummer-sequence]) is short exact.
