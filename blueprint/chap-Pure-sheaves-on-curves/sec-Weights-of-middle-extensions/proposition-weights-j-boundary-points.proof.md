+++
kind = "proof"
of = "proposition-weights-j-boundary-points"
order = 1184
uses = ["proposition-etale-implications", "proposition-topos-functoriality", "proposition-splitting-ind-etale-covers", "theorem-existence-contractible-covers", "theorem-pro-etale-refinements-weakly-etale", "proposition-pro-etale-affines-form-basis", "lemma-w-contractible-affines-projective", "proposition-comparison-morphism-inverse-image", "lemma-acyclicity-pulled-back-injectives", "theorem-comparison-direct-images", "lemma-comparison-direct-images-compatibilities", "proposition-locally-constant-sheaves-finite-presentation", "theorem-comparison-constructible-sheaves", "proposition-pro-etale-site-separably-closed", "definition-derived-adic-completeness", "definition-constructible-sheaves", "definition-lisse-sheaves", "lemma-integral-models", "proposition-inverting-ell", "lemma-cohomology-modules-underlying-abelian", "definition-derived-base-change-map", "lemma-acyclic-resolutions", "proposition-cohomology-p-1-over-henselian", "proposition-proper-base-change-projective-line", "lemma-finite-cover-projective-space", "theorem-proper-base-change-classical-pro", "lemma-smooth-morphisms-locally-constant-sheaves", "lemma-extension-across-finite-subset", "lemma-generic-smooth-open", "definition-change-of-coefficients-maps", "proposition-six-operations-change-coefficients", "proposition-dctf-x-qbar-2-colimit", "lemma-change-coefficients", "lemma-additivity-open-subscheme-complement", "theorem-grothendieck-lefschetz-trace-formula", "definition-trace-function", "proposition-function-sheaf-dictionary", "lemma-finite-quasi-finite-direct-images", "lemma-schematic-closure-uniqueness", "lemma-passing-schematic-closure", "remark-non-noetherian-compactifications", "remark-base-change-compactification", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection", "theorem-theorem-cube", "lemma-symmetric-ample-sheaf", "proposition-multiplication-n", "definition-relative-picard-functor", "corollary-degree-jacobian"]
+++
Comparing the $L$-functions of $\mathcal F$ and of $j_*\mathcal F$
gives the weaker bound $a+2$ at the boundary, and tensor powers
remove the extra $2$.

The assertion is local at a point of $X_0-U_0$, so we may replace $X_0$ by an
affine neighbourhood of that point. The complement of $U_0$ is an effective
Cartier divisor, so after shrinking this neighbourhood it is cut out by one
equation $f$, and then $U_0=D(f)$ is affine as well. Write
$i:Z_0=X_0-U_0\hookrightarrow X_0$. The hypotheses are preserved by this
replacement. Indeed, forming $j_*$ commutes with restriction to open
subschemes, and the restriction of $\mathcal F$ is still punctually of weights
$\le a$. Moreover, a nonempty open of $X_0$ is still geometrically connected.

The boundary Euler factors of $j_*\mathcal F$ are the ratio
$L_X/L_U$ of the two $L$-functions defined below. We show that $L_U$
has no zero and $L_X$ no pole on the disc $|t|<q^{-a/2-1}$, so that the
boundary factors have no pole there, and this bounds their eigenvalues.

*The $L$-function on $U_0$.* Put $L_U(t)=L(U_0,\mathcal F,t)$.
We show that $\iota L_U$ is holomorphic and nonvanishing on the disc,
by bounding the coefficients of its logarithm.
The logarithm of the Euler product has coefficients

$$
\log\iota L_U(t)=\sum_{n\ge1}\frac{c_n}{n}t^n,
\qquad
c_n=\sum_{d\mid n}d\sum_{\deg(x)=d}
\iota\operatorname{Tr}(\operatorname{Frob}_x^{n/d}\mid\mathcal F_{\bar x}).
$$

Let $r=\operatorname{rank}\mathcal F$. For a closed point $x$ of
degree $d\mid n$, the bound on the weights gives
$|\iota\operatorname{Tr}(\operatorname{Frob}_x^{n/d}\mid\mathcal F_{\bar x})|
\le rq_x^{(n/d)a/2}=rq^{na/2}$. Since
$\sum_{d\mid n}d\cdot\#\{x\in|U_0|:\deg(x)=d\}=\#U_0(k_n)$,
Lemma [lemma-point-count-bound] gives $|c_n|\le rDq^{n(a/2+1)}$. Hence the
logarithm converges on the disc $|t|<R=q^{-a/2-1}$, and its exponential
is a nonvanishing holomorphic function there. By the trace formula,
its Taylor series is that of the rational function $\iota L_U(t)$, so
the two agree on the whole disc.

*The $L$-function on $X_0$.* Let $L_X(t)=L(X_0,j_*\mathcal F,t)$.
We show that $\iota L_X$ is holomorphic on the same disc. By the trace
formula its poles come from $H^0_c$ and $H^2_c$ of $j_*\mathcal F$, and
we compute both groups.

The group $H^0_c$ vanishes. Indeed, the support of a compactly supported
section of $j_*\mathcal F$ on $X$ is closed and proper over $k$, and since $X$ is
an affine curve, the support is finite. So the section vanishes on a dense
open subset of $U$, and as $\mathcal F$ is lisse and $U$ is connected, it vanishes
on all of $U$. Since a section of $j_*\mathcal F$ is determined by its restriction
to $U$, the section is zero.
For $H^2_c$, note that the quotient sheaf in

$$
0\longrightarrow j_!\mathcal F\longrightarrow j_*\mathcal F
\longrightarrow i_*i^*j_*\mathcal F\longrightarrow0
$$

is supported on the finite boundary, whose cohomology is concentrated
in degree zero.  From the long exact sequence we obtain
$H_c^2(X,j_*\mathcal F)=H_c^2(U,\mathcal F)$, and by
Lemma [lemma-degree-zero-top-cohomology] its eigenvalues have absolute value at most
$q^{a/2+1}$.  By the trace formula, every pole of $\iota L_X$ is the
inverse of a Frobenius eigenvalue on $H^0_c$ or $H^2_c$. Since
$H^0_c=0$, the poles have absolute value at least $q^{-a/2-1}=R$. Hence
$\iota L_X$ is holomorphic on $|t|<R$.

*The boundary factors.* On $U_0$ the sheaves $\mathcal F$ and
$j_*\mathcal F$ have the same stalks, so the two Euler products differ
only by the factors at the points of $Z_0$, and we get

$$
L_X(t)=L_U(t)\prod_{z\in Z_0}
\det(1-\operatorname{Frob}_z t^{\deg(z)}\mid(j_*\mathcal F)_{\bar z})^{-1}.
$$

Since $L_U$ has no zero on the disc, the finite product on the right
is holomorphic there. As it is the reciprocal of a product of
polynomials with constant term one, none of these polynomials has
a zero on the disc.  Now, for an eigenvalue $\alpha$ at $z$, the roots of
$1-\iota(\alpha)t^{\deg(z)}$ have absolute value
$|\iota(\alpha)|^{-1/\deg(z)}$. This number is therefore at least $R$, which
is the preliminary bound

$$
|\iota(\alpha)|^2\le q_z^{a+2}.
$$

*Tensor powers.* The error $2$ in the exponent comes from the
twist $(-1)$ on $H^2_c$. Since it does not grow with the weight, it
becomes negligible for high tensor powers. We therefore apply the
preliminary bound to $\mathcal F^{\otimes m}$ for every $m\ge1$, a sheaf
punctually of weights $\le ma$.  Let $V$ be the local generic fibre of
$\mathcal F$ at $z$. By Lemma [lemma-boundary-stalk], the eigenvalue
$\alpha$ of $\operatorname{Frob}_z$ on $(j_*\mathcal F)_{\bar z}$ has an
eigenvector $v\in V^{I_z}$, and then $v^{\otimes m}$ is a nonzero
invariant eigenvector in $V^{\otimes m}$ with eigenvalue $\alpha^m$.
By the same lemma, $\alpha^m$ is therefore an eigenvalue on the stalk of
$j_*(\mathcal F^{\otimes m})$ at $\bar z$, and the preliminary bound for
$\mathcal F^{\otimes m}$ gives $|\iota(\alpha)|^{2m}\le q_z^{ma+2}$.  Taking
$m$th roots and letting $m$ tend to infinity, we obtain
$|\iota(\alpha)|^2\le q_z^a$ at every boundary point. On $U_0$, finally, the bound is
the hypothesis.
