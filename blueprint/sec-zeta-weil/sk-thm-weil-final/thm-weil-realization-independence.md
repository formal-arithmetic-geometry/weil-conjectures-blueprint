+++
id = "thm-weil-realization-independence"
kind = "theorem"
title = "Realization-independent integral factors"
lean = ["AlgebraicGeometry.Scheme.realization_independence"]
order = 4382
uses = ["cor-trf-point-counting", "def-weil-algebraic-closure-q", "def-weil-finite-field-fiber", "def-weil-geometric-hypotheses", "def-weil-hankel-matrix", "def-weil-integral-frobenius-factor", "def-weil-normalized-integral-fraction", "def-weil-numbers", "def-weil-ordinary-reciprocal-roots", "def-weil-parity-products", "def-weil-point-counts-zeta", "def-weil-smooth-proper-cohomological-family", "lem-embedding-extension", "lem-zl-log-det-identity", "prop-euler-product", "prop-galois-weight-strata-identification", "prop-galois-weight-strata-integrality", "prop-weight-purity-roots", "prop-weight-separation", "prop-weil-rationality-criterion", "prop-weil-reciprocal-roots-eigenvalues", "prop-weil-zeta-normalized-presentation", "thm-weil-deligne-purity", "thm-zl-lefschetz-weil-identity"]
+++
Fix a prime $p$, an integer $a\in\mathbf Z_{\geq1}$, put
$q=p^a$, $k_0=\Fq$, and let $k=\Fbar$ be the
fixed algebraic closure of $k_0$.
Let
$X_0/k_0$ be smooth, proper,
geometrically connected of pure dimension $d\in\mathbf Z_{\geq0}$, and
put $X=X_0\times_{k_0}k$. Fix an indeterminate $T$. For every prime
$\ell\neq p$, let
$(V_{i,\ell},F_{i,\ell},P_{i,\ell})_{0\leq i\leq2d}$ be the
smooth-proper
cohomological family. The reciprocal-root multiset is interpreted using the
ordinary and reciprocal-root
convention, and each $P_{i,\ell}$ is the determinant factor in that
cohomological family, explicitly

$$
P_{i,\ell}(T)=\det(1-TF_{i,\ell}\mid V_{i,\ell}).
$$

Let $Z(X_0,T)$ be the
point-count zeta series, and write
$Z(X_0,T)=A(T)/B(T)$ with $A,B\in\mathbf Z[T]$, $A(0)=B(0)=1$,
$\gcd(A,B)=1$ in $\mathbf Q[T]$; this is a chosen presentation satisfying
the normalized integral-fraction
conditions. Fix an algebraic closure $\overline{\mathbf Q}$. For each
$\ell\neq p$, write $\Ql=\mathbf Q_\ell$, choose an algebraic closure
$\Qlb$ of $\Ql$, set
$\overline{\mathbf Q}^{(\ell)} =\{\alpha\in\Qlb:\alpha\text{ is algebraic over }\mathbf Q\}$, the
algebraic closure of $\mathbf Q$
inside $\Qlb$, and choose an isomorphism
$\jmath_\ell:\overline{\mathbf Q}\xrightarrow{\sim} \overline{\mathbf Q}^{(\ell)}$.
For $C\in\{A,B\}$, put
$r_C=\deg C$ and define its reciprocal polynomial by

$$
C^\#(U)=U^{r_C}C(U^{-1}).
$$

For each $0\leq i\leq2d$, form the multiset $R_i$ of those roots of
$A^\#$ when $i$ is odd and of $B^\#$ when $i$ is even
that are $q$-Weil numbers of weight $i$. Put

$$
Q_i(T)=\prod_{\alpha\in R_i}(1-\alpha T)\in\mathbf Z[T].
$$

These $Q_i$ are candidate normalized integral factors.
For every
prime $\ell\neq p$, every ell-adic realization
$\jmath_\ell:\overline{\mathbf Q}\xrightarrow{\sim}\overline{\mathbf Q}^{(\ell)}$,
and every $0\leq i\leq2d$, write
$Q_i^{(\ell,\jmath_\ell)}$ for the scalar extension of $Q_i$ along
$\jmath_\ell$.
Then scalar extension identifies the reciprocal-root multiset of $Q_i$ with
that of $P_{i,\ell}$:

$$
Q_i^{(\ell,\jmath_\ell)}(T)=P_{i,\ell}(T).
$$

Here $Q_i^{(\ell,\jmath_\ell)}$ means coefficientwise extension along
$\jmath_\ell:\overline{\mathbf Q}\xrightarrow{\sim} \overline{\mathbf Q}^{(\ell)}$, so the displayed equality is an equality in
the chosen algebraic closure of $\Ql$ (with $P_{i,\ell}$ viewed through
$\Ql\subset\Qlb$).
Consequently, after these scalar identities are established, each $Q_i$ is
the normalized
integral Frobenius factor
for the common realization.
These scalar identities are independent of the chosen realization and
preserve the normalization $Q_i(0)=1$. If
$N_\ell(T)=\prod_{\substack{0\leq i\leq2d\\i\ {\rm odd}}}P_{i,\ell}(T)$ and
$D_\ell(T)=\prod_{\substack{0\leq i\leq2d\\i\ {\rm even}}}P_{i,\ell}(T)$, the
parity-product construction gives
$A^{(\ell)}=N_\ell$ and $B^{(\ell)}=D_\ell$.
The scalar-extension notation is coefficientwise extension of integral
polynomials.
