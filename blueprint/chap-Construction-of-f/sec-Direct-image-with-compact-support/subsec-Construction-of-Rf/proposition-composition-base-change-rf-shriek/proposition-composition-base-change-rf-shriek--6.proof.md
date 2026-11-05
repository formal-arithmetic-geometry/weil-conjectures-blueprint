+++
kind = "proof"
of = "proposition-composition-base-change-rf-shriek--6"
order = 516007
uses = ["proposition-composition-base-change-rf-shriek--5", "proposition-construction-independence-rf-shriek", "definition-pro-etale-base-change-map"]
+++
For successive changes of base, compute the three exchange maps using a
compactification, its base change, and its iterated base change. This is
permitted by [proposition-composition-base-change-rf-shriek--5]. The pasting
laws for proper base change and for extension by zero give the formula on
these compactifications. Their comparison maps cancel by the cocycle
condition.

For composition of the direct images, choose a triangle of compactifications
for $f$ and $g$ and base change that triangle. Express the composition maps
through these triangles and the base change maps through their open and
proper squares. The exchange identity
`AlgebraicGeometry.ProEtale.CondensedRing.pasteVert_compIso_shriekBaseChange`
identifies the two composites. Conjugating by the compactification
comparisons gives
`AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructibleLowerShriekBaseChange_padicAlgCl_paste_vert'`;
evaluating it on a complex gives the displayed formula.
