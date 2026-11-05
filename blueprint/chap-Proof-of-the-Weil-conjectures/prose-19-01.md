+++
id = "prose-19-01"
kind = "hidden"
title = "Proof of the Weil conjectures"
order = 1369
+++
The Deligne–Laumon theorem is an upper bound for weights, stated with $\ell$-adic
coefficients and one embedding $\iota:\overline{\mathbf Q}_\ell\to\mathbf C$. Weil's
conjectures ask for more: an equality $|\alpha|=q^{i/2}$, for
polynomials $P_i$ with integer coefficients, under every complex
embedding. This chapter closes both gaps.

The lower bound comes from Poincaré duality, and a curve shows how.
Let $X_0$ be a smooth projective curve and $\alpha$ an eigenvalue of
Frobenius on $H^1(X,\overline{\mathbf Q}_\ell)$. Then Theorem [theorem-weights-rf-shriek],
applied to the constant sheaf, gives $|\iota(\alpha)|\le q^{1/2}$. On the other hand, cup
product is a perfect pairing $H^1\times H^1\to H^2=\overline{\mathbf Q}_\ell(-1)$, which
Frobenius multiplies by $q$. Hence $q/\alpha$ is an eigenvalue as well,
and the same bound for $q/\alpha$ says that $|\iota(\alpha)|\ge q^{1/2}$.
In dimension $d$ the argument is the same: an eigenvalue $\alpha$ on
$H^i(X,\overline{\mathbf Q}_\ell)$ satisfies $|\iota(\alpha)|\le q^{i/2}$, while duality makes
$q^d/\alpha$ an eigenvalue on $H^{2d-i}$, of absolute value at most
$q^{(2d-i)/2}$, and we find $|\iota(\alpha)|=q^{i/2}$. This equality is
Weil's axiom (d), and we prove it in Section [sec-The-Riemann-hypothesis],
more generally for the higher direct images of a pure lisse sheaf under
a smooth proper morphism
(Theorem [theorem-purity-higher-direct-images-under]); the case of
the constant sheaf over a point is
Corollary [corollary-purity-cohomology-smooth-proper-variety]. Since
the Deligne–Laumon theorem holds for every $\iota$, purity holds for all complex
embeddings at once. Indeed, every embedding of a number field into
$\mathbf C$ extends to an isomorphism $\overline{\mathbf Q}_\ell\simeq\mathbf C$.

The polynomials $P_{i,\ell}=\det(1-TF\mid H^i(X,\mathbf Q_\ell))$ are defined with
$\ell$-adic coefficients, and a priori they could depend on $\ell$. The
zeta function does not mention $\ell$. It has a unique expression
$Z(X_0,T)=A/B$ with $A,B\in\mathbf Z[T]$ coprime and $A(0)=B(0)=1$
(Lemma [lemma-reduced-fractions-integer-coefficients];
Sections [sec-Rational-power-series]–[sec-Integrality-and-independence-of-ell]). Can each
$P_{i,\ell}$ be read off from $Z(X_0,T)$? The trace formula writes $Z$
as the alternating product of the $P_{i,\ell}$, but an alternating
product can cancel. For example, $X_0=\mathbf G_m\sqcup
\operatorname{Spec}\mathbf F_q$ is not proper, and it has $q^m$ points
over $\mathbf F_{q^m}$, as many as $\mathbf A^1$. Hence
$Z(X_0,T)=1/(1-qT)$. Yet $H^0_c$ and $H^1_c$ are both one-dimensional
with eigenvalue $1$, and the factor $1-T$ cancels between them. For a
smooth proper $X_0$ purity rules this out. The reciprocal roots of
$P_{i,\ell}$ have absolute value $q^{i/2}$, so no root of $P_{i,\ell}$
is a root of $P_{j,\ell}$ for $i\neq j$. It follows that the product of
the $P_{i,\ell}$ with $i$ odd is $A$ and the product with $i$ even is
$B$. Grouping the reciprocal roots of $A$ and $B$ by absolute value then
recovers each $P_{i,\ell}$ from $Z(X_0,T)$ alone
(Theorem [theorem-weil-conjectures-smooth-proper-schemes]). In
particular $P_{i,\ell}$ has integer coefficients and does not depend on
$\ell$.

In terms of point counts, purity gives the classical estimates. For a
smooth proper geometrically connected $X_0$ we obtain
$|\#X_0(\mathbf F_{q^m})-(1+q^{dm})|\le\sum_{i=1}^{2d-1}b_iq^{mi/2}$
(Corollary [corollary-point-count-estimates]). In particular, for a curve of genus $g$
this is Weil's bound $2gq^{m/2}$, and for elliptic curves it is Hasse's
theorem. As an illustration, Example [example-running-example-purity] works this out
for genus-one curves over $\mathbf F_3$.
