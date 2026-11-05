+++
kind = "proof"
of = "lemma-additivity-open-subscheme-complement--2"
order = 1002004
uses = ["lemma-additivity-open-subscheme-complement--1", "proposition-construction-independence-rf-shriek", "proposition-composition-base-change-rf-shriek", "proposition-properties-trace"]
+++
Apply the Weil direct image $Rf_{0!}$ to the equivariant localization
triangle of [lemma-additivity-open-subscheme-complement--1]. It remains
distinguished with equivariant connecting map by
`AlgebraicGeometry.ProEtale.CondensedRing.WeilBoundedConstructible.IsDistTriang.weilLowerShriek_map`.

Take cohomology sheaves and then stalks at $\bar y$. This gives a bounded
long exact sequence of finite free objects whose maps, including the
connecting maps, commute with the $m$-th local Frobenius operators.
Their alternating traces add by
`CategoryTheory.superTrace_eq_add_of_exact`, as packaged in
`AlgebraicGeometry.ProEtale.CondensedRing.weilStalkTraceAlternatingSum_eq_add_of_isDistTriang`.
This is the cohomological trace calculation underlying
[proposition-properties-trace].

Finally, the composition isomorphisms for direct image with compact
support identify the outer terms with $R(f_0j_0)_!j_0^*K$ and
$R(f_0i_0)_!i_0^*K$, respecting their Weil structures
(`AlgebraicGeometry.ProEtale.CondensedRing.weilLowerShriekCompIso`).
Local traces are invariant under these isomorphisms. For the structure
morphism, the stalk of the direct image at the geometric point of the
base is $R\Gamma_c$, giving the last formula.
