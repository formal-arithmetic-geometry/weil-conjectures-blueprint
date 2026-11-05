+++
kind = "proof"
of = "lemma-base-change-along-product-projection--1"
order = 706002
uses = ["theorem-results-from-etale-theory--4", "lemma-base-change-along-product-projection", "lemma-degree-zero-calculation", "lemma-integral-changes-source-base", "theorem-proper-base-change-classical-pro", "lemma-identity-pasting"]
+++
All the schemes in the diagram are of finite type over $k$, hence locally
Noetherian, and $g$ and $h$ are quasi-compact and quasi-separated. By the
finite cohomological dimension statement of
[theorem-results-from-etale-theory--4], their derived direct images commute
with the sequential colimits used to express complexes as telescopes.
In Lean these inputs are
`AlgebraicGeometry.Etale.hasFiniteCohomologicalDimensionMorphism` and
`AlgebraicGeometry.Etale.preservesColimitsOfShape_nat_rightDerivedLowerStar`.

First reduce $E$ to a strictly bounded complex of flat sheaves, using
`DerivedCategory.isIso_app_of_isIso_app_Q_obj_flat`. For each such complex,
reduce $F$ to strictly bounded complexes by the same telescope argument.
The resulting bounded-below statement is
`AlgebraicGeometry.Etale.isIso_tensorBaseChangeMap_of_isGE`: a lower bound
on the Tor amplitude of $E$ permits reduction to a flat sheaf $\mathcal E$ and a
sheaf $\cF$, both in degree zero. This gives the intermediate result
`AlgebraicGeometry.Etale.isIso_tensorBaseChangeMap_Q_obj_of_flat`.

For single sheaves, devissage by the nilpotent Jacobson radical of $A$
reduces $\cF$ to sheaves annihilated by that radical. The homology maps then
depend only on the corresponding quotient of $\mathcal E$. Write this quotient
as a filtered colimit of constructible sheaves, embed each constructible
sheaf into a finite sum of direct images of constant sheaves along finite
morphisms, and use dimension shifting. Since the quotient ring is a
product of fields, the constant modules that occur are direct summands of
free modules. Thus it suffices to treat $\mathcal E=\pi_*A$ for $\pi$ finite.
Proper base change and pasting reduce this case to ordinary base change
for the structure morphisms of $X$ and of the source of $\pi$.

The needed result is
`AlgebraicGeometry.Etale.universalBaseChangeProperty_of_field`. In degree
zero, pass to a perfect closure and then to the reduction, using invariance
under universal homeomorphisms as in [lemma-integral-changes-source-base],
and apply [lemma-degree-zero-calculation]. In higher degrees, a first
failure would give a nonzero higher direct image from an algebraically
closed generic field. A limit argument reduces its vanishing to the
degreewise étale form of [lemma-base-change-along-product-projection]
and the vanishing of higher direct images from a separably closed field.
This proves
`AlgebraicGeometry.Etale.isIso_tensorBaseChangeMap_singleFunctor_of_flat`;
the reductions above give the asserted isomorphism for arbitrary $E$ and
$F$.
