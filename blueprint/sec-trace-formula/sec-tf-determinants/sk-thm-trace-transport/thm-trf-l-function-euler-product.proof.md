+++
kind  = "proof"
of    = "thm-trf-l-function-euler-product"
+++
*Step 0: the determinant–trace identity.* For an endomorphism $G$ of a
finite-dimensional $\Lambda$-vector space $V$,

$$
\det(1-TG\mid V)^{-1}
=\exp\Bigl(\sum_{r\geq1}\operatorname{Tr}(G^r\mid V)\frac{T^r}{r}\Bigr),
$$

by [lem-zl-euler-product-identity] (after extending scalars to
$\overline{\mathbf Q}_\ell\supseteq\Lambda$, which changes neither side; $\exp$ and
$\log$ are mutually inverse bijections $T\Lambda[[T]]\leftrightarrows1+T\Lambda[[T]]$
carrying sums, including $T$-adically convergent infinite sums, to products). Substituting $T^e$ for
$T$ gives the same identity with $T^{er}$ in place of $T^r$. For a
graded endomorphism of a bounded complex with finite-dimensional
cohomology, taking the alternating product over the degrees gives

$$
\prod_j\det\bigl(1-TG\mid H^j\bigr)^{(-1)^{j+1}}
=\exp\Bigl(\sum_{r\geq1}\Bigl(\sum_j(-1)^j
\operatorname{Tr}(G^r\mid H^j)\Bigr)\frac{T^r}{r}\Bigr).
\tag{$*$}
$$

*Step 1: powers and finiteness.* We argue directly over $\Lambda$, in
$\Dbc(X,\Lambda)\subset D(X_{\mathrm{pro\acute et}},\Lambda)$.

*Global powers.* By (2) of [det-thm-tf-uniform-formula-weil], the operator
of the $m$-th iterate $\theta^{[m]}$ on $H_c^i(X,K)$ is $F^m$.

*Local powers.* Consider the proofs of the conjugacy lemma
[lem-trf-local-frobenius-conjugacy] and the degree formula
[lem-trf-frobenius-degree-formula]. They use only four inputs:
(a) the cocycle identity of [lem-trf-iterated-weil-cocycle];
(b) the canonical stalk identifications
$(f^*M)_{\bar z}\cong M_{f\bar z}$ and the fixed-point identifications
entering $\tau$, natural in $M$ and compatible with composition;
(c) invertibility of the Weil map, for the inverse transports $T_i^{-1}$;
(d) conjugacy invariance of traces.

All four hold over $\Lambda$:
(a) the proof of the cocycle identity uses only associativity of
composition and naturality of the pullback identifications, which hold for
the exact pullback functors on $D(X_{\mathrm{pro\acute et}},\Lambda)$;
(b) these identifications are the composition isomorphisms of inverse
images of $\Lambda_X$-modules, natural in $M$;
(c) $\theta$ is an isomorphism because $(K,\theta)$ is a Weil complex;
(d) is [prop-trf-trace-formal-laws], item (1), over $\Lambda$.

So those proofs apply verbatim to $(K,\theta)$. The one-circuit local
Frobenius $F_x=F_{x_{e_x},e_x}$ is well defined up to conjugation by
$\Lambda$-linear isomorphisms of stalk complexes. Moreover, for every
$y\in X_0(\mathbf F_{q^m})$ above $x$ ($e_x\mid m$), the operator $F_{y,m}$
on $K_{\bar y}$ is conjugate to $F_x^{\,m/e_x}$ on $K_{\bar x}$ by such an
isomorphism.

*Finiteness.* By (1) of [det-thm-tf-uniform-formula-weil], the spaces
$H_c^i(X,K)$ and $H^j(K_{\bar x})$ are finite-dimensional over $\Lambda$ and
nonzero for only finitely many $i$, $j$. Hence each local factor lies in
$1+T^{e_x}\Lambda[[T]]$, its determinant being invariant under
conjugation of $F_x$, and the product in (2) is finite.

*Step 2: local finiteness.* A closed point of degree $e$ has
exactly $e$ points of $X_0(\mathbf F_{q^e})$ above it, and
$X_0(\mathbf F_{q^e})$ is finite because $X_0$ is of finite type
([def-weil-scheme-morphism-properties]); so for each $N$ only
finitely many $x\in|X_0|$ have $e_x\leq N$. As the factor at $x$ is
$\equiv1\bmod T^{e_x}$, the product $L(X_0,K,T)$ converges
$T$-adically, lies in $1+T\Lambda[[T]]$, and
$\log L(X_0,K,T)=\sum_x\log\det(1-T^{e_x}F_x\mid K_{\bar x})^{-1}$ is
a convergent sum. This is (1).

*Step 3: grouping by closed points.* Let $m\geq1$. The points of
$X_0(\mathbf F_{q^m})$ lie over the closed points $x$ with
$e_x\mid m$, exactly $e_x$ of them over each such $x$. By Step 1,
$F_{y,m}$ on $K_{\bar y}$ is conjugate to $F_x^{\,m/e_x}$ on $K_{\bar x}$
by an isomorphism of complexes of $\Lambda$-vector spaces, for every $y$
above $x$. The induced maps on each $H^j$ are therefore conjugate, and
their ordinary traces agree. Hence the right-hand side of the trace
formula (2) of [det-thm-tf-uniform-formula-weil] is

$$
\sum_{y\in X_0(\mathbf F_{q^m})}\sum_j(-1)^j
\operatorname{Tr}\bigl(F_{y,m}\mid H^j(K_{\bar y})\bigr)
=\sum_{\substack{x\in|X_0|\\e_x\mid m}}e_x
\sum_j(-1)^j\operatorname{Tr}\bigl(F_x^{\,m/e_x}\mid H^j(K_{\bar x})\bigr).
$$

*Step 4: the identity (2).* Multiply the trace formula by $T^m/m$ and
sum over $m\geq1$. On the cohomology side, $(*)$ applied to
$G=F$ on the complex with cohomology $H_c^i(X,K)$ (Step 1:
$F^m_{c,K}=F^m$) gives the logarithm of the right-hand side of (2).
On the point side, writing $m=re_x$,

$$
\sum_{m\geq1}\frac{T^m}{m}\sum_{e_x\mid m}e_x\,t_x(m/e_x)
=\sum_{x\in|X_0|}\sum_{r\geq1}t_x(r)\frac{T^{e_xr}}{r},
\qquad
t_x(r)=\sum_j(-1)^j\operatorname{Tr}\bigl(F_x^{\,r}\mid H^j(K_{\bar x})\bigr),
$$

the rearrangement being legitimate because only finitely many
$x$ contribute to each coefficient (Step 2); by $(*)$ with $T^{e_x}$ in
place of $T$, the inner sum is
$\log\det(1-T^{e_x}F_x\mid K_{\bar x})^{-1}$, so the total is
$\log L(X_0,K,T)$ (Step 2). Applying $\exp$ gives (2).

*Step 5: curves.* Let $\dim X_0\leq1$ and let $K$ be a sheaf placed in
degree zero, so its cohomology sheaves lie in degrees $[0,0]$. By the
complement of [sk-lem-finite], $\RGammac(X,K)$ has cohomology only in
degrees $[0,0+2\dim X]\subseteq[0,2]$. Hence $H_c^i(X,K)=0$ for
$i\notin\{0,1,2\}$, which is (3).

*Step 6: the embedding.* A field embedding $\iota$ is a ring
homomorphism; applied coefficientwise it is a ring homomorphism
$\Qlb[[T]]\to\mathbf C[[T]]$, continuous for the $T$-adic topologies,
so it carries the finite product in (2), each determinant (a
polynomial in the matrix entries) and the convergent product
$L(X_0,K,T)$ to the corresponding expressions for the matrices
$\iota(F)$, $\iota(F_x)$. This is (4).
