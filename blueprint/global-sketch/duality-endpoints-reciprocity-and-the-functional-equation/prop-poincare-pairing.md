+++
id = "prop-poincare-pairing"
kind = "theorem"
title = "Poincare duality and Frobenius similitude"
order = 120
tags = ["latex:proposition"]
uses = ["def-frobenius-on-twists", "def-poincare-trace-pairing", "def-smooth-proper-datum", "prop-proper-operation-comparison", "prop-smooth-purity", "prop-verdier-duality", "prop-weil-cup-product-compatibility", "prop-weil-duality-compatibility", "prop-weil-purity-compatibility", "prop-weil-trace-compatibility"]
+++
Let $\mathscr X=(X_0,d,X)$ be a smooth-proper datum and let
$\ell\neq p$ be prime. The trace map is an isomorphism. For every
integer $0\leq i\leq2d$, the cup-product pairing
$\langle-,-\rangle_i$ is perfect. Equivalently, it induces a
Frobenius-equivariant isomorphism

$$
H^{2d-i}(X,\Ql)
\xrightarrow{\sim}H^i(X,\Ql)^\vee(-d).
$$

Since geometric Frobenius acts on $\Ql(-d)$ by $q^d$, for every integer
$0\leq i\leq2d$, every $x\in H^i(X,\Ql)$, and every
$y\in H^{2d-i}(X,\Ql)$,

$$
\langle Fx,Fy\rangle_i=q^d\langle x,y\rangle_i.
$$

For the same $i,x,y$, graded commutativity gives

$$
\langle y,x\rangle_{2d-i}=(-1)^i\langle x,y\rangle_i;
$$

in middle degree the pairing is $(-1)^d$-symmetric.
After scalar extension to any algebraic closure of $\Ql$, the same
duality and Frobenius-similitude identities remain valid.
