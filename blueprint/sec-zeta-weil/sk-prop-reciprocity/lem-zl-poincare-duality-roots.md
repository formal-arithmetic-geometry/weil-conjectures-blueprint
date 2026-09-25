+++
id = "lem-zl-poincare-duality-roots"
kind = "lemma"
title = "Duality reciprocity of Frobenius roots"
order = 3139
uses = ["def-weil-algebraically-closed-coefficients", "def-weil-finite-field-fiber", "def-weil-frobenius-coefficient-twists", "def-weil-frobenius-detailed", "def-weil-geometric-hypotheses", "def-weil-global-geometric-frobenius", "def-weil-ordinary-compact-cohomology", "def-weil-ordinary-reciprocal-roots", "def-weil-poincare-trace-cup", "def-weil-smooth-proper-cohomological-family", "def-weil-weil-sheaf-complex", "lem-wf-tate-twist-frobenius", "thm-weil-poincare-duality"]
+++
Fix the finite-field datum
$(p,a,q,k_0,k)$, where $q=p^a$, and a prime $\ell\neq p$; write
$\Ql=\mathbf Q_\ell$, choose an algebraic closure $\Qlb$ of $\Ql$,
and interpret the $\Qlb$-objects in the
algebraically closed
coefficient category. Let $X_0/k_0$ be
smooth, proper, geometrically
connected of pure dimension $d\in\mathbf Z_{\geq0}$, put
$X=X_0\times_{k_0}k$, let $(\Qlb)_X$ be the constant
Weil sheaf, and let $F$ be the
global geometric Frobenius
in the geometric-Frobenius convention. Let

$$
\langle-,-\rangle_i:
H^i(X,\Qlb)\times H^{2d-i}(X,\Qlb)\longrightarrow\Qlb(-d)
$$

be the trace–cup-product pairing
with values in the Tate twist $\Qlb(-d)$, and let
$P_{i,\ell}(T)=\det(1-TF_i\mid V_i)$, $V_i=H^i(X,\Qlb)$,
$F_i=F|_{V_i}$, be the determinant factors of the
smooth-proper
cohomological family extended to $\Qlb$, with roots taken in the
ordinary/reciprocal-root
convention. Assume the Poincare duality statements
[thm-weil-poincare-duality] of the Poincare-duality chapter for the constant Weil
sheaf with its canonical structure: the pairing
$\langle-,-\rangle_i$ is perfect, and it is a Frobenius similitude
$\langle Fx,Fy\rangle_i=q^d\langle x,y\rangle_i$. Then, for every
$0\leq i\leq2d$, the following hold:

1. **(a)** the pairing $\langle-,-\rangle_i$ is perfect, and
$$
\langle Fx,Fy\rangle_i=q^d\langle x,y\rangle_i
\qquad\bigl(x\in H^i(X,\Qlb),\ y\in H^{2d-i}(X,\Qlb)\bigr);
$$
1. **(b)** the multiset of eigenvalues of $F$ on $H^{2d-i}(X,\Qlb)$,
counted with algebraic multiplicity, is
$$
\left\{\frac{q^d}{\alpha}:\ \alpha\text{ an eigenvalue of }F\text{ on }
H^i(X,\Qlb)\right\};
$$
1. **(c)** the reciprocal
roots of $P_{2d-i,\ell}$, counted with multiplicity, are exactly
$$
\left\{q^d\alpha^{-1}:\ \alpha\text{ a reciprocal root of }
P_{i,\ell}\right\}
=\left\{q^d\beta:\ \beta\text{ an ordinary root of }P_{i,\ell}\right\};
$$
1. **(d)** for $b_j=\dim_{\Qlb}H^j(X,\Qlb)$ and
$D_j=\det(F\mid H^j(X,\Qlb))$, one has
$$
b_{2d-i}=b_i,\qquad D_iD_{2d-i}=q^{db_i};
$$
1. **(e)** the *dual determinant identity*
$$
P_{2d-i,\ell}(q^{-d}T^{-1})
=(-1)^{b_i}T^{-b_i}D_i^{-1}P_{i,\ell}(T)
\quad\text{in }\Qlb[T,T^{-1}].
$$

## Proof

Step 1: the similitude data. Assertion (a) is items (3) and (4) of
[thm-weil-poincare-duality] (the perfectness of the trace–cup
pairings, whose value line is $\Qbarl(-d)$, and the Frobenius
similitude for the constant sheaf); the value-line convention is
[def-weil-poincare-trace-cup], and the normalization of the
Frobenius action $q^d$ on $\Qlb(-d)$ is
[def-weil-frobenius-coefficient-twists] (its stalk-level form is
[lem-wf-tate-twist-frobenius]).

Step 2: the adjoint relation. Put
$V_i=H^i(X,\Qlb)$, $V_{2d-i}=H^{2d-i}(X,\Qlb)$,
$F_i=F|_{V_i}$, $F_{2d-i}=F|_{V_{2d-i}}$, and let

$$
\Phi:V_{2d-i}\longrightarrow V_i^\vee,\qquad
\Phi(y)(x)=\langle x,y\rangle_i,
$$

be the adjoint of the pairing. By perfectness of
[thm-weil-poincare-duality], $\Phi$ is an isomorphism. The
similitude of step 1, with $x$ replaced by $F_i^{-1}x$, reads

$$
\langle x,F_{2d-i}y\rangle_i
=q^d\langle F_i^{-1}x,y\rangle_i,
$$

i.e. $\Phi\circ F_{2d-i}=q^d\,(F_i^{-1})^{\mathsf t}\circ\Phi$, where
$(F_i^{-1})^{\mathsf t}$ is the transpose of the inverse operator on
the dual $V_i^\vee$. Hence $F_{2d-i}$ is conjugate, via $\Phi$,
to $q^d(F_i^{-1})^{\mathsf t}$.

Step 3: eigenvalues. A linear operator and its transpose have the same
characteristic polynomial, and conjugation does not change the
eigenvalue multiset; therefore the eigenvalues of $F_{2d-i}$ are
exactly the $q^d\alpha^{-1}$, $\alpha$ running over the eigenvalues
of $F_i$, each with the same multiplicity. This is (b), and it is the
reciprocity assertion contained in [thm-weil-poincare-duality].

Step 4: roots. Over the algebraically closed field $\Qlb$, the
determinant $P_{j,\ell}(T)=\det(1-TF_j)$ factors as
$\prod(1-\alpha T)$ with $\alpha$ running over the eigenvalues of
$F_j$, those being the reciprocal roots in the convention of
[def-weil-ordinary-reciprocal-roots]; applying (b) degree by degree
gives (c) (the second form is the substitution
$\beta=\alpha^{-1}$, $\beta$ an ordinary root of $P_{i,\ell}$).

Step 5: dimensions and determinants. By (b), the two eigenvalue
multisets have equal cardinality, so $b_{2d-i}=b_i$; the dimensions are
the degrees of the determinant polynomials, by
[def-weil-smooth-proper-cohomological-family]. Multiplying out the
reciprocal multiset,

$$
D_{2d-i}=\prod_{\alpha}\frac{q^d}{\alpha}
=\frac{q^{db_i}}{\prod_{\alpha}\alpha}
=\frac{q^{db_i}}{D_i},
$$

which is the second identity of (d).

Step 6: the dual determinant identity. Factor
$P_{i,\ell}(T)=\prod_{\alpha}(1-\alpha T)$ and
$P_{2d-i,\ell}(S)=\prod_{\alpha}\bigl(1-q^d\alpha^{-1}S\bigr)$, products
over the reciprocal roots with multiplicity, using (c). Then

$$
1-q^d\alpha^{-1}q^{-d}T^{-1}=1-\alpha^{-1}T^{-1}
=-\alpha^{-1}T^{-1}(1-\alpha T),
$$

so multiplying over the $b_i$ factors and using
$D_i=\prod_{\alpha}\alpha$ from step 5,

$$
P_{2d-i,\ell}(q^{-d}T^{-1})
=(-1)^{b_i}T^{-b_i}D_i^{-1}P_{i,\ell}(T),
$$

which is (e).
