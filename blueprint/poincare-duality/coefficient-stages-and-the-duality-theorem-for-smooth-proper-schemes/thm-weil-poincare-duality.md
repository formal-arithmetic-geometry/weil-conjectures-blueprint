+++
id = "thm-weil-poincare-duality"
kind = "theorem"
title = "Poincare duality for smooth proper schemes"
order = 3837
uses = ["cor-pod-reciprocal-eigenvalues", "cor-pod-untwisted-similitude", "def-coefficient-twists-detailed", "def-trf-frobenius-operators", "def-weil-exceptional-adjoint-admissibility", "def-weil-exceptional-inverse-image", "def-weil-finite-field-fiber", "def-weil-frobenius-coefficient-twists", "def-weil-frobenius-detailed", "def-weil-geometric-hypotheses", "def-weil-global-geometric-frobenius", "def-weil-ordinary-compact-cohomology", "def-weil-poincare-trace-cup", "def-weil-weil-sheaf-complex", "prop-cohomological-finiteness", "thm-pod-poincare-duality"]
+++
Let $p$ be prime, let $a\in\mathbf Z_{\geq1}$, put $q=p^a$, and set
$k_0=\Fq$, and let $k=\Fbar$ be the
fixed algebraic closure of $k_0$.
Fix a prime $\ell\neq p$, write $\Ql=\mathbf Q_\ell$, and choose an
algebraic closure $\Qlb$ of $\Ql$. Let $X_0/k_0$
be smooth, proper, geometrically
connected of pure dimension $d\in\mathbf Z_{\geq0}$, and put
$X=X_0\times_{k_0}k$. Let $a_X:X\to\Spec k$ be the structure
morphism and assume it is
exceptional-adjoint
admissible at $\Ql$. Let $Ra_X^!$ denote the
exceptional inverse image, and
choose an orientation isomorphism

$$
\eta_X:Ra_X^!\Ql\xrightarrow{\sim}(\Ql)_X(d)[2d]
$$

and let $K_X=(\Ql)_X$ with its
canonical Weil structure. Let $F$ be
the endomorphism of $R\Gamma(X,K_X)$ induced by the
global geometric Frobenius
with the normalization in the geometric
Frobenius convention; write $F$ for its induced automorphisms on every
$H^i(X,\Ql)$. Here $H^i$ and $H_c^i$ denote the
ordinary and compactly
supported cohomology groups, $\Ql(m)$ denotes the
Tate twist, and geometric Frobenius acts on
it by the specified twist
normalization. Then the Poincare duality interface holds: the trace
map

$$
\operatorname{tr}^{(-d)}_X:H^{2d}(X,\Ql)\xrightarrow{\sim}\Ql(-d)
$$

is an isomorphism, the groups $H^i(X,\Ql)$ are finite-dimensional
and vanish for $i\notin[0,2d]$, the
trace–cup-product pairings
$\langle-,-\rangle_i$ with values in $\Ql(-d)$ are perfect for
every $0\leq i\leq2d$ and satisfy

$$
\langle Fx,Fy\rangle_i=q^d\langle x,y\rangle_i
\qquad
(x\in H^i(X,\Ql),\ y\in H^{2d-i}(X,\Ql)),
$$

there is a Frobenius-equivariant duality isomorphism
$H^{2d-i}(X,\Ql)\simeq H^i(X,\Ql)^\vee(-d)$, and the
base-change clause holds for every finite extension $k_0'/k_0$
contained in $k$. These five clauses are precisely the items
(Trace), (Finiteness), (Pairing), (Frobenius similitudine), and
(Reciprocity), together with the base-change item, of
[thm-pod-poincare-duality] of the Poincare-duality chapter, read in the
conventions fixed here.

## Proof

The interface statement is the smooth-proper-geometrically-connected
case of the Poincare duality theorem of the Poincare-duality chapter,
[thm-pod-poincare-duality], whose six items (trace
isomorphism, finiteness, perfect pairings, Frobenius similitudine,
reciprocity, and base change) are the six clauses of the interface:
the trace map is the trace of [def-weil-poincare-trace-cup], the
finiteness item is the constant-sheaf case of
[prop-cohomological-finiteness], the Frobenius items use the
global operator of [def-weil-global-geometric-frobenius] with the
twist normalization of [def-weil-frobenius-coefficient-twists]
and the untwisted Frobenius similitude of
[cor-pod-untwisted-similitude], and the reciprocity and base
change are [cor-pod-reciprocal-eigenvalues] and the
Frobenius-operator convention of [def-trf-frobenius-operators].
Both the
interface and [thm-pod-poincare-duality] are expressed in the
ordinary and compact-support conventions of
[def-weil-ordinary-compact-cohomology] and the Tate twist
conventions of [def-coefficient-twists-detailed], with the orientation
datum specified in the interface statement entering only through the
identification $\eta_X$ recorded there; the two statements therefore
agree clause by clause.
