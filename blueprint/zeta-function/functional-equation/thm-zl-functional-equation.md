+++
id = "thm-zl-functional-equation"
kind = "theorem"
title = "Functional equation"
order = 4352
uses = ["def-weil-algebraically-closed-coefficients", "def-weil-finite-field-fiber", "def-weil-frobenius-detailed", "def-weil-geometric-hypotheses", "def-weil-global-geometric-frobenius", "def-weil-point-counts-zeta", "def-weil-smooth-proper-cohomological-family", "def-weil-weil-sheaf-complex", "lem-zl-poincare-duality-roots", "thm-zl-lefschetz-weil-identity"]
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
in the geometric-Frobenius convention.
Let $(V_{i,\ell},F_{i,\ell},P_{i,\ell})_{0\leq i\leq2d}$ be the
smooth-proper
cohomological family extended to $\Qlb$, and let $Z(X_0,T)$ be the
point-count zeta series, which by
[thm-zl-lefschetz-weil-identity] is the rational function

$$
Z(X_0,T)=\prod_{i=0}^{2d}P_{i,\ell}(T)^{(-1)^{i+1}}.
$$

Put

$$
b_i=\dim_{\Qlb}H^i(X,\Qlb),\qquad
\chi=\sum_{i=0}^{2d}(-1)^ib_i,\qquad
D_i=\det\bigl(F\mid H^i(X,\Qlb)\bigr),
$$

$$
\Delta_\ell=\prod_{i=0}^{2d}D_i^{(-1)^i},\qquad
\varepsilon=(-1)^\chi q^{-d\chi/2}\Delta_\ell,
$$

and assume the duality statements [lem-zl-poincare-duality-roots]
(the duality root reciprocity of the preceding lemma, whose input is the
Poincare duality of the zeta chapter). Then

$$
Z(X_0,q^{-d}T^{-1})
=(-1)^\chi T^\chi\Delta_\ell\,Z(X_0,T)
\quad\text{in }\Qlb(T),
$$

equivalently

$$
\boxed{
Z(X_0,q^{-d}T^{-1})
=\varepsilon\,q^{d\chi/2}T^\chi Z(X_0,T)}
\quad\text{in }\Qlb(T).
$$

## Proof

Step 1: reindexing. The involution $i\mapsto 2d-i$ preserves the
exponent $(-1)^{i+1}$, because $(-1)^{2d}=1$; hence in
$\Qlb(T)$,

$$
Z(X_0,q^{-d}T^{-1})
=\prod_{i=0}^{2d}P_{i,\ell}(q^{-d}T^{-1})^{(-1)^{i+1}}
=\prod_{i=0}^{2d}P_{2d-i,\ell}(q^{-d}T^{-1})^{(-1)^{i+1}},
$$

the first identity by [thm-zl-lefschetz-weil-identity] and the
second by the substitution $i\mapsto2d-i$ in the finite product.

Step 2: substitution of the dual determinant identity. By
[lem-zl-poincare-duality-roots], item (e), making the product
explicit,

$$
Z(X_0,q^{-d}T^{-1})
=\prod_{i=0}^{2d}
\left((-1)^{b_i}T^{-b_i}D_i^{-1}P_{i,\ell}(T)\right)^{(-1)^{i+1}}.
$$

Step 3: separation. Collecting the three scalar families,

$$
Z(X_0,q^{-d}T^{-1})
=\left(\prod_{i=0}^{2d}(-1)^{b_i(-1)^{i+1}}\right)
\left(\prod_{i=0}^{2d}T^{-b_i(-1)^{i+1}}\right)
\left(\prod_{i=0}^{2d}D_i^{-(-1)^{i+1}}\right)
Z(X_0,T).
$$

For the sign: $b_i(-1)^{i+1}\equiv b_i\pmod2$, so

$$
\prod_{i=0}^{2d}(-1)^{b_i(-1)^{i+1}}
=(-1)^{\sum_i b_i}
=(-1)^\chi,
$$

because $\sum_ib_i\equiv\sum_i(-1)^ib_i=\chi\pmod2$. For the Laurent
exponent:

$$
\prod_{i=0}^{2d}T^{-b_i(-1)^{i+1}}
=T^{-\sum_i(-1)^{i+1}b_i}=T^\chi.
$$

For the determinant scalar:
$-(-1)^{i+1}=(-1)^i$, so the third factor is $\Delta_\ell$. This is
the raw functional equation

$$
Z(X_0,q^{-d}T^{-1})=(-1)^\chi T^\chi\Delta_\ell\,Z(X_0,T).
$$

Rewriting the scalar $(-1)^\chi\Delta_\ell$ as
$\varepsilon q^{d\chi/2}$, which is the definition
$\varepsilon=(-1)^\chi q^{-d\chi/2}\Delta_\ell$ of the normalized sign,
gives the boxed normalized form.
