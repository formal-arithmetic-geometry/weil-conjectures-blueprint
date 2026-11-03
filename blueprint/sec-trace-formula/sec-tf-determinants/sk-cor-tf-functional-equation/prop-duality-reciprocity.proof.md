+++
kind  = "proof"
of    = "prop-duality-reciprocity"
+++
1. **1.** Write $V_i=H^i(X,\Ql)$, put
$n_i=\dim_{\Ql}V_i$, and let
$\alpha_{i,1},\ldots,\alpha_{i,n_i}$ denote the eigenvalues of $F$ on
$V_i$, counted with algebraic multiplicity. The trace–cup pairing of
[prop-poincare-pairing] is perfect by the degreewise duality
[thm-pod-degreewise-perfectness-over-a-field] for $K=(\Ql)_X$ ($X$ proper, so
$H_c^i=H^i$), and it induces
$$
V_{2d-i}\xrightarrow{\sim}V_i^\vee(-d),\qquad
y\longmapsto\bigl(x\longmapsto\langle x,y\rangle_i\bigr).
$$
Since $F$ acts on $\Ql(-d)$ by $q^d$, the operator transported to the
right-hand side is $q^d(F^{-1})^\vee$ ([cor-pod-reciprocal-eigenvalues], with
$K=K^\vee=(\Ql)_X$). Its eigenvalue multiset is
$$
\{\alpha_{2d-i,1},\ldots,\alpha_{2d-i,n_{2d-i}}\}
=
\{q^d/\alpha_{i,1},\ldots,q^d/\alpha_{i,n_i}\}.
$$
In particular the two multisets have the same cardinality.
1. **2.** By the Betti-number convention in
[def-weil-betti-numbers], $b_j=\dim_{\Ql}V_j=n_j$. The cardinality
comparison in Step 1 therefore gives
$$
b_{2d-i}=b_i.
$$
The determinant-constant definition in
[def-weil-determinant-constants] and the factorization
$P_i(T)=\prod_{r=1}^{b_i}(1-\alpha_{i,r}T)$ give
$$
D_i=(-1)^{b_i}[T^{b_i}]P_i(T)
=\prod_{r=1}^{b_i}\alpha_{i,r}.
$$
Using the reciprocal multiset from Step 1,
$$
D_{2d-i}
=\prod_{r=1}^{b_i}\frac{q^d}{\alpha_{i,r}}
=\frac{q^{db_i}}{D_i},
$$
and hence $D_iD_{2d-i}=q^{db_i}$.
1. **3.** The same factorization gives, as an identity in
$\mathbf Q[T,T^{-1}]$,
$$
\begin{aligned}
P_{2d-i}(q^{-d}T^{-1})
&=\prod_{r=1}^{b_i}
\left(1-\frac{1}{\alpha_{i,r}}T^{-1}\right)\\
&=(-1)^{b_i}T^{-b_i}
\left(\prod_{r=1}^{b_i}\alpha_{i,r}\right)^{-1}
\prod_{r=1}^{b_i}(1-\alpha_{i,r}T)\\
&=(-1)^{b_i}T^{-b_i}D_i^{-1}P_i(T).
\end{aligned}
$$
This is the claimed Laurent-polynomial reciprocity.
1. **4.** For $i=d$, the symmetry clause of
[prop-poincare-pairing] makes the pairing $(-1)^d$-symmetric. If
$d$ is odd, choose a nonzero $\Ql$-linear trivialization
$\Ql(-d)\xrightarrow{\sim}\Ql$; this is possible because the Tate-twist
construction in [def-coefficient-twists-detailed] makes
$\Ql(-d)$ an invertible rank-one coefficient space. Transporting the
pairing along this trivialization gives a nondegenerate alternating
$\Ql$-valued form on $V_d$. The
coefficient field is $\Ql=\mathbf Q_\ell$, of characteristic zero under
the finite-field convention of [def-weil-finite-field-fiber], so its
characteristic is not $2$. Applying
[lem-weil-alternating-form-dimension] gives
$\dim_{\Ql}V_d$ even; [def-weil-betti-numbers] then gives that
$b_d$ is even.
