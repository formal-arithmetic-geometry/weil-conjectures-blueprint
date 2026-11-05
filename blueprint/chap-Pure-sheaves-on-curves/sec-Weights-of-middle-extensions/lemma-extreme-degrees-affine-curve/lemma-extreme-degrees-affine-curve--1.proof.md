+++
kind = "proof"
of = "lemma-extreme-degrees-affine-curve--1"
order = 1186004
uses = ["lemma-cohomological-range-curve", "definition-compactification-refinement", "proposition-extension-zero-restriction-closed-subscheme"]
+++
Since $j_*F$ is a sheaf, its direct image with compact support has
no negative cohomology. For $r>2$, apply the cohomological range
on the smooth affine curve $C_0$ to $j_*F$
([lemma-cohomological-range-curve]). Neither argument needs density
or geometric connectedness.

For degree zero, choose a compactification $i:C_0\hookrightarrow Z_0$.
The group $H_c^0(C,j_*F)$ is the space of global sections of
$i_!j_*F$ on the geometric fibre of $Z_0$; this is the reduction in
`AlgebraicGeometry.WeilSheaf.subsingleton_compactlySupportedCohomology_zero_of_forall_eq_zero`.
The smooth geometrically connected curve $C$ is irreducible, and
its image in the proper compactification is not closed: otherwise
$C$ would be both affine and proper, hence finite, contrary to its
dimension one. Its generic point therefore specializes to a point
outside $C$, and every point of $U$ is a specialization of that
generic point.

A section extended by zero vanishes near this boundary point.
Lisseness propagates this vanishing along the preceding
specializations, so its restriction to $U$ is zero and hence the
section itself is zero. Lean applies
`AlgebraicGeometry.ProEtale.eq_zero_of_forall_specializes_notMem_range`
to make this last step.
