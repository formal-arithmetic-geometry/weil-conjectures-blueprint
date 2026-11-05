+++
kind = "proof"
of = "theorem-trace-formula-euler-product"
order = 1037
uses = ["theorem-grothendieck-lefschetz-trace-formula", "definition-trace-function", "lemma-logarithm-determinant", "theorem-trace-formula-euler-product--2", "theorem-trace-formula-euler-product--4", "theorem-trace-formula-euler-product--6"]
+++
Both sides are of the form $\exp$ of a power series, and we compare
the logarithms coefficient by coefficient. The coefficient of $T^m$ on
the cohomological side is the global trace of $\operatorname{Frob}^m$
divided by $m$, and on the side of closed points it is the sum of the local
traces over $X_0(\mathbf F_{q^m})$ divided by $m$. Hence the theorem is
the trace formula for all $m$ at once.

For convergence, note that $X_0$ has only finitely many closed points of
degree at most any given bound $n$, because each of them
lies under a point of the finite set $X_0(\mathbf F_{q^{n!}})$.
The factor at $x$ in (12.6) is $1$ modulo
$T^{\deg(x)}$, so the product converges.

Before comparing logarithms we rewrite the sum over points in
Theorem [theorem-grothendieck-lefschetz-trace-formula] in
terms of closed points. A closed point of degree $d$ has
exactly $d$ points over $\mathbf F_{q^m}$ when $d\mid m$, and none
otherwise. For instance, $\operatorname{Spec}\mathbf F_{q^2}$ has one closed
point, of degree $2$, with no $\mathbf F_q$-points and two
$\mathbf F_{q^2}$-points. These $d$ points form one Frobenius orbit, and the Weil
structure gives isomorphisms between the
stalks at consecutive points of the orbit. The Frobenius on the stalk at a point of the orbit is then the composite of these isomorphisms taken once
around the orbit, starting at that point. Moving the starting point cyclically therefore conjugates this composite by one of these isomorphisms. Hence the
operators at the $\deg(x)$ points are conjugate. In the same way, iterating the Weil
structure shows that for $\deg(x)\mid m$ the operator
$\operatorname{Frob}_{y,m}$ at each of the $\deg(x)$ points $y\in X_0(\mathbf F_{q^m})$ over
$x$ is conjugate to $\operatorname{Frob}_x^{m/\deg(x)}$. Since traces are invariant under conjugation,
(12.3) reads

$$
\operatorname{tr}_{\Lambda}(\operatorname{Frob}_{X,K}^m\mid R\Gamma_c(X_{\mathrm{pro}\acute{e}t},K))
=\sum_{\substack{x\in|X_0|\\\deg(x)\mid m}}\deg(x)\,
\operatorname{tr}_{\Lambda}
(\operatorname{Frob}_x^{m/\deg(x)}\mid K_{\bar x}).
\tag{12.8}
$$

We multiply (12.8) by $T^m/m$ and sum over
$m\geq1$. By Lemma [lemma-logarithm-determinant], the left side becomes
the logarithm of the right side of (12.7). In the
sum over closed points on the right, we substitute $m=r\deg(x)$. Then the multiplicity $\deg(x)$ cancels the factor $\deg(x)$ in $m$, and Lemma [lemma-logarithm-determinant] applied to
$\operatorname{Frob}_x$ on $K_{\bar x}$, with $T^{\deg(x)}$ in place of $T$, shows that

$$
\sum_{x\in|X_0|}\sum_{r\geq1}
\operatorname{tr}_{\Lambda}(\operatorname{Frob}_x^r\mid K_{\bar x})
\frac{T^{r\deg(x)}}{r}
=\log L(X_0,K,T).
$$

Each coefficient of $T$ receives only finitely many contributions, so
we may regroup the sums. Exponentiating proves
(12.7). Rationality holds because the cohomological product has finitely
many factors, each a polynomial or the reciprocal of one, with value
$1$ at zero. If $X_0$ is proper, compact and
ordinary cohomology agree.
