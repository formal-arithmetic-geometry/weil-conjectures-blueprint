+++
kind = "proof"
of = "lemma-inverse-image-tensor-product--6"
order = 494013
uses = ["proposition-extension-zero-restriction-closed-subscheme", "lemma-inverse-image-coefficient-sheaves", "definition-lisse-sheaves"]
+++
Pullback is exact and commutes with cohomology. If the restrictions have
cohomology in $[a_U,b_U]$ and $[a_Z,b_Z]$, then $K$ has cohomology in
$[\min(a_U,a_Z),\max(b_U,b_Z)]$: outside this interval both restrictions
of each cohomology sheaf vanish, and open and closed restriction jointly
detect zero objects. For each degree, concatenate stratifications of the
two restrictions. The resulting stratification of $X$ shows that the
cohomology sheaf is constructible. These are the sheaf statements
`AlgebraicGeometry.ProEtale.CondensedRing.isZero_of_isZero_upperStar_of_isCompl`
and
`AlgebraicGeometry.ProEtale.CondensedRing.isConstructibleModuleObject_of_openClosed`.
