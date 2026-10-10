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

*Step 1: powers and finiteness.* We argue at the stage $E$, for the
$E$-representative $(K_E,\varphi_E)$ and its operators of
[prop-trf-rational-frobenius-integral-model]. The $\Qlb$-operators are
their scalar extensions ([thm-trf-grothendieck-lefschetz-qbar]), and scalar
extension preserves composition and conjugacy. No integrality of
$\varphi_E$ is used in this step.

*Global powers.* By definition
$\varphi_E^{[m]}=\varphi_E\circ Lg_\gamma^*\varphi_E^{[m-1]}$ after the
composition isomorphisms of the rationalized pullbacks. This is the
cocycle identity of [lem-trf-iterated-weil-cocycle], whose proof uses only
associativity of composition and naturality of the pullback
identifications, so it holds in $D^b_c(X,E)$. The base-change
isomorphisms at the stage $E$ are rationalizations of the integral ones
([prop-weil-pbc-rational-transport]). They are therefore natural,
$g^{*}_{\gamma,c}\circ R\Gamma_c(X,f)=R\Gamma_c(X,Lg_\gamma^*f)\circ g^{*}_{\gamma,c}$,
and compatible with composition,
$g^{*}_{\gamma,c}\circ g^{m-1,*}_{\gamma,c}=g^{m,*}_{\gamma,c}$. Hence

$$
F^1_{c,K_E}\circ F^{\,m-1}_{c,K_E}
=R\Gamma_c(X,\varphi_E)\circ R\Gamma_c(X,Lg_\gamma^*\varphi_E^{[m-1]})\circ
g^{*}_{\gamma,c}\circ g^{m-1,*}_{\gamma,c}
=R\Gamma_c(X,\varphi_E^{[m]})\circ g^{m,*}_{\gamma,c}=F^{\,m}_{c,K_E},
$$

and by induction $F^m_{c,K}=(F^1_{c,K})^m$.

*Local powers.* Consider the proofs of the conjugacy lemma
[lem-trf-local-frobenius-conjugacy] and the degree formula
[lem-trf-frobenius-degree-formula]. They use only four inputs:
(a) the cocycle identity;
(b) the canonical stalk identifications
$(Lf^*M)_{\bar z}\cong M_{f\bar z}$ and the fixed-point identifications
entering $\tau$, natural in $M$ and compatible with composition;
(c) invertibility of the Weil map, for the inverse transports $T_i^{-1}$;
(d) conjugacy invariance of traces.

All four hold at the stage $E$:
(a) as just shown;
(b) the $E$-stage identifications are rationalizations of the integral
ones ([prop-weil-pbc-rational-transport]), hence natural and compatible;
(c) $\varphi_E$ is an isomorphism of $D^b_c(X,E)$ because $K$ is a Weil
complex;
(d) is [prop-trf-trace-formal-laws], item (1), over $E$.

So those proofs apply verbatim to $(K_E,\varphi_E)$. The one-circuit local
Frobenius $F_x=F_{x_{e_x},e_x}$ is well defined up to conjugation by
$E$-linear isomorphisms of stalk complexes. Moreover, for every
$y\in X_0(\mathbf F_{q^m})$ above $x$ ($e_x\mid m$), the operator $F_{y,m}$
on $K_{\bar y}$ is conjugate to $F_x^{\,m/e_x}$ on $K_{\bar x}$ by such an
isomorphism.

*Finiteness.* By the finiteness clause of [thm-trf-trace-formula-e] (and,
for $\Lambda=\Qlb$, scalar extension), the spaces $H_c^i(X,K)$ and
$H^j(K_{\bar x})$ are finite-dimensional over $\Lambda$ and nonzero for only
finitely many $i$, $j$. Hence each local factor lies in
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
formula of
[thm-trf-trace-formula-e] (for $\Lambda=E$) or
[thm-trf-grothendieck-lefschetz-qbar] (for $\Lambda=\Qlb$) is

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

*Step 5: curves.* Let $\dim X_0\leq1$ and $K$ a sheaf in degree zero;
the groups $H_c^i(X,K)$ depend only on $K$, so for $\Lambda=\Qlb$ we
may compute them from the $E$-representative, and we may take
$\Lambda=E$. Let $K_{\mathcal O_E}$ be a lattice of $K$ (one exists by
[thm-trf-trace-formula-e]). In
the rational category [def-weil-pbc-rational-category] a morphism
whose cone has cohomology sheaves killed by a power of $\varpi$ is an
isomorphism (on a bounded cone with cohomology killed by $\varpi^N$ in
$b-a+1$ degrees, $\varpi^{N(b-a+1)}$ kills the identity, by the
truncation triangles). The cohomology sheaves $\mathcal H^j$ of
$K_{\mathcal O_E}$ for $j\neq0$ and the $\varpi$-power torsion of
$\mathcal H^0$ vanish after inverting $\varpi$ and, being
constructible, are killed by a power of $\varpi$; so
$K\cong M[1/\varpi]$ for the $\varpi$-torsion-free constructible
$\mathcal O_E$-sheaf $M=\mathcal H^0(K_{\mathcal O_E})/(\text{torsion})$,
and $H_c^i(X,K)=H^i(R\Gamma_c(X,M))\otimes_{\mathcal O_E}E$. The
levels $M\otimes^L_{\mathcal O_E}A_n=M/\varpi^nM$ of the reduction tower of
$M$ are constructible sheaves in degree zero, since $M$ is torsion-free. By
the argument of Step 0 of [thm-trf-trace-formula-e] they lie in
$D^b_{ctf}(X,A_n)$ and form a normalized $A_\bullet$-system. Items (1) and
(2) of [prop-trf-adic-coefficient-morphism-systems] need no Weil
structure, and they give that $P=R\Gamma_c(X,M)$ is represented by a
bounded complex of finite free $\mathcal O_E$-modules with
$P\otimes^L_{\mathcal O_E}A_1\cong R\Gamma_c(X,M/\varpi M)$. For a perfect
complex over the discrete valuation ring $\mathcal O_E$, the universal
coefficient sequence gives
$\dim_E H^i(P)\otimes E=\operatorname{rank}H^i(P)
\leq\dim_{A_1}H^i(P\otimes^LA_1)$. Finally choose a compactification
$j:X\hookrightarrow\bar X$ over $k_0$ by [thm-nagata-compactification];
then $\dim\bar X\leq1$ after replacing $\bar X$ by the closure of $X$,
and $R\Gamma_c(X,M/\varpi M)\cong R\Gamma(\bar X,j_!(M/\varpi M))$ by
[lem-trf-compactification-cohomology]. The cohomology of the sheaf
$j_!(M/\varpi M)$ vanishes in negative degrees, and in degrees $>2$ by
[thm-sc-finite-type-torsion-cd] applied over the algebraically closed
field $k$, whose torsion cohomological dimension is $0$ by
[lem-sf-separably-closed-torsion-cd]. Hence $H_c^i(X,K)=0$ for
$i\notin\{0,1,2\}$, which is (3).

*Step 6: the embedding.* A field embedding $\iota$ is a ring
homomorphism; applied coefficientwise it is a ring homomorphism
$\Qlb[[T]]\to\mathbf C[[T]]$, continuous for the $T$-adic topologies,
so it carries the finite product in (2), each determinant (a
polynomial in the matrix entries) and the convergent product
$L(X_0,K,T)$ to the corresponding expressions for the matrices
$\iota(F)$, $\iota(F_x)$. This is (4).
