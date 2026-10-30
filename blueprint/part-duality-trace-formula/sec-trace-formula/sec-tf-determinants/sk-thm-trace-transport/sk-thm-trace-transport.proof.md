+++
kind = "proof"
of = "sk-thm-trace-transport"
uses = ["sk-thm-tf-uniform-formula", "sk-prop-logdet", "sk-thm-sf-ctf-stability", "sk-thm-nagata-compactification", "sk-thm-curveestimate"]
+++
Since $X_0$ is of finite type over a finite field, it has only finitely
many closed points of degree at most any given bound. The factor at
$x$ in (13.6) is $1$ modulo $T^{\deg(x)}$, which proves
convergence.

We compare the logarithms of the two sides, after first
rewriting the sum over points in Theorem [sk-thm-tf-uniform-formula] in
terms of closed points. A closed point of degree $d$ has
exactly $d$ points over $\mathbf F_{q^m}$ when $d\mid m$, and none
otherwise. These points form one Frobenius orbit, and the Weil
structure gives isomorphisms between the
stalks at consecutive points of the orbit. The Frobenius on the stalk at a
point of the orbit is the composite of these isomorphisms taken once
around the orbit, starting at that point. Moving the starting point
cyclically conjugates this composite by one of these isomorphisms, so the
operators at the $\deg(x)$ points are conjugate. Iterating the Weil
structure shows, in the same way, that for $\deg(x)\mid m$ the operator
$\operatorname{Frob}_{y,m}$ at each of the $\deg(x)$ points $y\in X_0(\mathbf F_{q^m})$ over
$x$ is conjugate to $\operatorname{Frob}_x^{m/\deg(x)}$. Since traces are invariant under conjugation,
(13.3) reads

$$
\operatorname{tr}_{\Lambda}(\operatorname{Frob}_{X,K}^m\mid R\Gamma_c(X_{\mathrm{pro}\acute{e}t},K))
=\sum_{\substack{x\in|X_0|\\\deg(x)\mid m}}\deg(x)\,
\operatorname{tr}_{\Lambda}
(\operatorname{Frob}_x^{m/\deg(x)}\mid K_{\bar x}).
\tag{13.8}
$$

We multiply (13.8) by $T^m/m$ and sum over
$m\geq1$. By Lemma [sk-prop-logdet], the left side becomes
the logarithm of the right side of (13.7). In the
sum over closed points on the right, we substitute $m=r\deg(x)$. The multiplicity $\deg(x)$ cancels the
factor $\deg(x)$ in $m$, and Lemma [sk-prop-logdet] applied to
$\operatorname{Frob}_x$ on $K_{\bar x}$, with $T^{\deg(x)}$ in place of $T$, shows that

$$
\sum_{x\in|X_0|}\sum_{r\geq1}
\operatorname{tr}_{\Lambda}(\operatorname{Frob}_x^r\mid K_{\bar x})
\frac{T^{r\deg(x)}}{r}
=\log L(X_0,K,T).
$$

Since each coefficient of $T$ receives only finitely many contributions,
we may regroup the sums, and exponentiating proves
(13.7). Rationality holds because the cohomological product has finitely
many factors, each a polynomial or the reciprocal of one, with value
$1$ at zero. If $X_0$ is proper, compact and
ordinary cohomology agree.
