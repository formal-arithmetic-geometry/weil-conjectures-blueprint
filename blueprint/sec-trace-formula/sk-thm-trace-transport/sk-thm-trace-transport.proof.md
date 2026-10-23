+++
kind = "proof"
of = "sk-thm-trace-transport"
uses = ["sk-thm-tf-uniform-formula", "sk-prop-logdet", "sk-thm-sf-ctf-stability", "sk-thm-nagata-compactification", "sk-thm-curveestimate"]
+++
Since $X_0$ is of finite type over a finite field, it has only finitely
many closed points of degree at most any given bound. The factor at
$x$ in (1) is $1$ modulo $T^{d_x}$, which proves
convergence.

The proof compares the two sides through their logarithms; for this
the point side of [sk-thm-tf-uniform-formula] is rewritten in
terms of closed points. A closed point of degree $d$ has
exactly $d$ points over $\mathbf F_{q^m}$ when $d\mid m$, and none
otherwise. These points form one Frobenius orbit, and the Weil
structure gives isomorphisms $a_0,\ldots,a_{d_x-1}$ between the
stalks at consecutive points of the orbit. The local operator at a
point of the orbit is the composite of these isomorphisms taken once
around the orbit, starting at that point. Moving the starting point
cyclically conjugates this composite by one of the $a_i$; hence the
operators at the $d_x$ points are conjugate. Iterating the Weil
structure shows, in the same way, that for $d_x\mid m$ the operator
$\operatorname{Frob}_{y,m}$ at each of the $d_x$ points $y\in X_0(\mathbf F_{q^m})$ over
$x$ is conjugate to $\operatorname{Frob}_x^{m/d_x}$. Since traces are invariant under conjugation,
the identity (1) of [sk-thm-tf-uniform-formula] reads

$$
 \operatorname{tr}_{\Lambda}(\operatorname{Frob}_{X,K}^m\mid R\Gamma_c(X_{\mathrm{pro\acute et}},K))
  =\sum_{\substack{x\in|X_0|\\d_x\mid m}}d_x\,
      \operatorname{tr}_{\Lambda}
         (\operatorname{Frob}_x^{m/d_x}\mid K_{\bar x}).
 \tag{3}
$$

Multiply (3) by $T^m/m$ and sum over
$m\geq1$. By [sk-prop-logdet], the left side becomes
the logarithm of the right side of (2). On the
point side, substitute $m=rd_x$; the multiplicity $d_x$ cancels the
factor $d_x$ in $m$, and [sk-prop-logdet] applied to
$\operatorname{Frob}_x$ on $K_{\bar x}$, with $T^{d_x}$ in place of $T$, gives

$$
 \sum_{x\in|X_0|}\sum_{r\geq1}
    \operatorname{tr}_{\Lambda}(\operatorname{Frob}_x^r\mid K_{\bar x})
       \frac{T^{rd_x}}{r}
  =\log L(X_0,K,T).
$$

Each coefficient of $T$ receives only finitely many contributions, so
the sums may be regrouped, and exponentiating proves
(2). The cohomological product has finitely
many factors, each a polynomial or the reciprocal of one, with value
$1$ at zero; this proves rationality. If $X_0$ is proper, compact and
ordinary cohomology agree.

*Complement.* (i) The groups $H_c^i(X,K)$ are finite dimensional and vanish
outside a bounded range by [sk-thm-sf-ctf-stability]. For a curve and a
coefficient sheaf in degree zero, compactification by
[sk-thm-nagata-compactification], extension by zero and [lem-sc-arbitrary-curve-cd] give the
range $0\le i\le2$. (ii) A field embedding $\iota$ is a ring homomorphism, so
it carries the identity in $\overline{\mathbf Q}_\ell[[T]]$ coefficientwise to
one in $\mathbf C[[T]]$.

The detailed form of this argument, including the complement, is
[thm-trf-l-function-euler-product].
