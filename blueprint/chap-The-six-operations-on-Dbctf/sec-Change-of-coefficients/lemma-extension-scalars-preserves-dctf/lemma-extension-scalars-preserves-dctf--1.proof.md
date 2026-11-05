+++
kind = "proof"
of = "lemma-extension-scalars-preserves-dctf--1"
order = 633002
uses = ["proposition-topos-functoriality", "definition-change-of-coefficients-maps--1"]
+++
Extension of scalars preserves colimits and sends the free module of rank
one over $R$ to the free module of rank one over $S$. It therefore sends a
finite free presentation to a finite free presentation. Pullback commutes
with extension of scalars: as in
[definition-change-of-coefficients-maps--1], the comparison comes from
uniqueness of left adjoints, using the pullback adjunction of
[proposition-topos-functoriality]. In Lean this comparison is
`AlgebraicGeometry.ProEtale.pullbackExtendScalarsComparison`.

Apply these facts on the original pro-étale presentation cover to obtain
preservation of local finite presentation
(`AlgebraicGeometry.ProEtale.lfp_extend`). Applying the same comparison on
each stratum shows that the original stratification still witnesses
constructibility after extension of scalars.

Put $F=S\otimes_R-$. Since $F$ also preserves finite limits, it is exact,
and there are natural isomorphisms
$$
H^n(\mathbf L F(K))\simeq F(H^n(K)).
$$
These are `CategoryTheory.Functor.leftDerivedFunctorHomologyFunctorIso`.
The right hand side is constructible by the preceding argument. Moreover,
$F$ preserves zero objects, so the same cohomological bounds as for $K$
apply to $\mathbf L F(K)$. This proves the assertion.
