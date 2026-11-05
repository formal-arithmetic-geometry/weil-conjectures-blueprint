+++
kind = "proof"
of = "proposition-forgetting-supports-composition--2"
order = 519005
uses = ["definition-compactification-refinement", "proposition-construction-independence-rf-shriek", "proposition-forgetting-supports-composition--1"]
+++
First let $r:c\to d$ be a refinement for which the square on the open
subscheme is cartesian, as in [definition-compactification-refinement].
Expand the comparison $Rf_!^{\,d}\to Rf_!^{\,c}$ as the unit for the
refinement morphism, the base change isomorphism for extension by zero,
and ordinary direct-image composition. Transpose the open-immersion
comparison under $j^*\dashv Rj_*$. The composite counit formula and the
compatibility of the extension-by-zero unit with base change show that
its transpose is the same inverse unit as in
[proposition-forgetting-supports-composition--1]. Naturality and
associativity of ordinary direct-image composition then give, for the
refinement comparison $\rho_r:Rf_!^{\,d}\to Rf_!^{\,c}$,

$$
\eta_f^{\,c}(K)\circ\rho_r(K)=\eta_f^{\,d}(K).
$$

This is
`AlgebraicGeometry.Etale.rightDerivedLowerShriekOfCompactificationComparison_app_comp_toLowerStar`.
The comparison $\kappa_{c,d}$ is the comparison from $c$ to the common
refinement $c\wedge d$, followed by the inverse of the comparison from
$d$ to that refinement. These comparisons are isomorphisms by
[proposition-construction-independence-rf-shriek]. Apply the refinement
identity twice and cancel the inverse comparison. This proves the
asserted equality on every unbounded complex.
