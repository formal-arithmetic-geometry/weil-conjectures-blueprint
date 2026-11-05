+++
kind = "proof"
of = "theorem-trace-formula-frobenius-correspondence--1"
order = 1006002
uses = ["corollary-trace-functions-direct-image-compact", "theorem-proper-pushforward-lefschetz-verdier", "proposition-frobenius-local-term-curve"]
+++
Apply the compatibility of trace functions with direct image with compact
support, [corollary-trace-functions-direct-image-compact], in its
$\overline{\mathbf Q}_\ell$ form with the finite-order automorphism $e$.
In Lean this is `AlgebraicGeometry.ProEtale.CondensedRing.weilShriekTraceFunction`.
Take $f=a$, the identity automorphism on the base, and its unique point
$s$ of degree $m$. The left side is $t_{Ra_!K,m}(s)$ by the definition of
compactly supported cohomology of a Weil object. Every point of $P_m(e)$
lies over $s$, so forgetting the redundant condition $a\circ\bar x=s$
identifies the fibre sum with the stated sum. These are the two steps
of `AlgebraicGeometry.ProEtale.CondensedRing.weilTraceFormula`.

The relative compatibility is proved first. Its generic case factors
through finite étale maps, closed immersions and projections of relative
affine lines. For a finite étale map, the Frobenius permutes the summands
in the stalk of the direct image, and only fixed summands contribute.
For a relative affine line, extend by zero to the relative projective
line and use base change to its geometric fibres. On each fibre,
[theorem-proper-pushforward-lefschetz-verdier] and
[proposition-frobenius-local-term-curve] give the formula on the proper
smooth curve; the stalk at infinity is zero. Closed immersions are
handled by base change and extension by zero. Compatibility with
composition combines these cases on a nonempty stable open obtained
from a generic quotient by $e$. Additivity for an open subscheme and
its reduced closed complement then gives the relative formula by
Noetherian induction. These steps are packaged in
`AlgebraicGeometry.ProEtale.CondensedRing.shriekTraceFunctionGenericallyHolds`
and
`AlgebraicGeometry.ProEtale.CondensedRing.weilShriekTraceFunction_of_genericallyHolds`.
