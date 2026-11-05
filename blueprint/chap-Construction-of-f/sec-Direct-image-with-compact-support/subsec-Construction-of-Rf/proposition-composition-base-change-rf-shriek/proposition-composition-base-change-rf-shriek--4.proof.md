+++
kind = "proof"
of = "proposition-composition-base-change-rf-shriek--4"
order = 516005
uses = ["proposition-proper-direct-image-constructible-complexes", "proposition-comparison-immersions", "proposition-construction-independence-rf-shriek", "remark-base-change-compactification", "proposition-proper-base-change-etale-site", "theorem-proper-base-change-classical-pro"]
+++
Choose a compactification $f=pj$ and pull it back along $v$.
The defining map (5.8) is proper base change for $p$, applied after $j_!$,
followed by the base change isomorphism for extension by zero. Proper base
change for bounded constructible $E$-, $\Oe$- and $\Qbarl$-complexes makes
both factors isomorphisms. The comparison from the pulled-back
compactification to the chosen compactification of $f'$ is also an
isomorphism by [proposition-construction-independence-rf-shriek].

For finite étale coefficients the same argument uses unbounded proper base
change for the finite ring $\Lambda$.
`AlgebraicGeometry.Etale.isIso_rightDerivedLowerShriekOfCompactificationBaseChangeMap_of_finite`
proves invertibility before the final comparison, and
`AlgebraicGeometry.Etale.rightDerivedLowerShriekIso` supplies that comparison
under the stated quasi-compactness hypothesis.
