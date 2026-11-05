+++
kind = "proof"
of = "proposition-composition-base-change-rf-shriek--5"
order = 516006
uses = ["proposition-construction-independence-rf-shriek", "proposition-dense-compactifications-form-cofiltered-category", "remark-base-change-compactification"]
+++
First consider compatible refinements of the two compactifications.
`CategoryTheory.ExchangeFormalism.shriekBaseChange_refinementComparison`
shows that the base change maps commute with their refinement comparisons.
For two compactifications of $f$, choose a common refinement and pull it
back along $v$. Apply the refinement identity to both maps out of the
common refinement, then use the cocycle condition to compare the original
two base change maps. This gives
`AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructibleLowerShriekOfCompactificationBaseChange_padicAlgCl_iso'`.

For a pair of compactifications lying over one another as in the statement,
compare the upper compactification with the pullback of the lower one.
The same refinement identity identifies their exchange maps. Conjugating
by the comparisons with the chosen compactifications proves the stated
formula for $\Ex_!$.
