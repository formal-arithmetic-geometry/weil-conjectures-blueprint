+++
kind = "proof"
of = "corollary-degreewise-duality-over-fields--1"
order = 859002
uses = ["theorem-poincare-duality", "theorem-global-verdier-duality", "lemma-perfect-complexes-geometric-point", "definition-tate-twists", "proposition-forgetting-supports-composition"]
+++
Let $a:X_0\to\Spec k_0$ be the structure map. The lisse form of
Theorem [theorem-poincare-duality] identifies
$\mathbb D_{X_0}\cF$ with $\cF^\vee(d)[2d]$. Verdier exchange, as in
Theorem [theorem-global-verdier-duality], then gives

$$
(Ra_*\cF^\vee(d))[2d]\simeq\mathbb D_{\Spec k_0}(Ra_!\cF).
$$

Take cohomology in degree $-i$. Duality on the point identifies this
cohomology on the right with the coefficient dual of the degree $i$
cohomology of $Ra_!\cF$. Taking global sections on the point, or
equivalently its geometric stalk, gives a Frobenius-equivariant isomorphism

$$
e:H^j(X,\cF^\vee(d))\xrightarrow{\sim}
\Hom_{\Qbarl}(H_c^i(X,\cF),\Qbarl).
$$

This is
`AlgebraicGeometry.WeilSheaf.nonempty_equiv_cohomology_dual_compactlySupportedCohomology`.
Set $P(x,y)=e(y)(x)$. The cohomology spaces are finite-dimensional,
as in Lemma [lemma-perfect-complexes-geometric-point]; in Lean this is
carried by their Frobenius modules, using
`AlgebraicGeometry.WeilSheaf.finiteDimensional_globalSections` on the
cohomology sheaves over $\Spec k_0$. Evaluation therefore gives a perfect
pairing. Frobenius on the dual is the inverse transpose, so
$e(\Frob y)=e(y)\circ\Frob^{-1}$ and
$P(\Frob x,\Frob y)=P(x,y)$.

For the second pairing,
`AlgebraicGeometry.WeilSheaf.nonempty_equiv_cohomology_constantTwist`
identifies the underlying vector space of $H^j(X,\cF^\vee(d))$ with
$H^j(X,\cF^\vee)$, with Frobenius multiplied by $q^{-d}$.
Transport $P$ along the inverse of this identification. Perfectness is
preserved, and the Frobenius identity becomes
$P_0(\Frob x,\Frob y)=q^dP_0(x,y)$.

For proper $X_0$, use the Frobenius-equivariant comparison
`AlgebraicGeometry.WeilSheaf.nonempty_equiv_compactlySupportedCohomology_cohomology`,
the Weil-sheaf form of Proposition [proposition-forgetting-supports-composition],
and transport the first factor of each pairing along its inverse.
