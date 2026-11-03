+++
kind  = "proof"
of    = "prop-poincare-pairing"
+++
1. **1.** The orientation and coefficient multiplication in
[def-weil-poincare-trace-cup] identify the trace and pairing used here:
$$
\langle x,y\rangle_i=\operatorname{tr}^{(-d)}_X(x\smile y)
\quad\text{in }\Ql(-d),
\qquad
x\in H^i(X,\Ql),\ y\in H^{2d-i}(X,\Ql).
$$
Thus the pairing in the proposition is the one to which the duality
interface applies, rather than an auxiliary bilinear form.
1. **2.** The trace isomorphism and perfectness are supplied by
[thm-weil-poincare-duality]. For each $0\leq i\leq2d$, perfectness
means that the map
$$
\Phi_i:H^{2d-i}(X,\Ql)\longrightarrow
H^i(X,\Ql)^\vee(-d),\qquad
y\longmapsto\bigl(x\longmapsto\langle x,y\rangle_i\bigr)
$$
is an isomorphism, and the same interface gives
$\operatorname{tr}^{(-d)}_X:H^{2d}(X,\Ql)\xrightarrow{\sim}\Ql(-d)$.
This proves both the asserted perfect pairings and the displayed duality
isomorphism.
1. **3.** The Frobenius clause of
[thm-weil-poincare-duality] says that the trace target has scalar
action $q^d$ and that
$$
\langle Fx,Fy\rangle_i=q^d\langle x,y\rangle_i.
$$
Equivalently, under $\Phi_i$, the operator on the second factor is
$q^d(F^{-1})^\vee$. This is precisely the Frobenius similitude asserted
in the proposition.
1. **4.** The cup product in
[def-weil-poincare-trace-cup] is graded-commutative. Taking degrees
$i$ and $2d-i$ gives
$$
y\smile x=(-1)^{i(2d-i)}x\smile y=(-1)^i x\smile y,
$$
because $2d$ is even. Applying the trace therefore yields
$$
\langle y,x\rangle_{2d-i}=(-1)^i\langle x,y\rangle_i.
$$
For $i=d$ this is $(-1)^d$-symmetry, completing all the claims.
