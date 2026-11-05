+++
kind = "proof"
of = "lemma-degree-zero-top-cohomology--4"
order = 1150011
uses = ["theorem-nagata-s-compactification-theorem", "proposition-construction-independence-rf-shriek", "proposition-extension-zero-restriction-closed-subscheme"]
+++
Choose a compactification $U_0\hookrightarrow Z_0\to\operatorname{Spec}\Fq$
and pass to the geometric fibre. The degree-zero derived direct image
identifies $H_c^0(U,\mathcal F)$ with $\Gamma(Z,j_!\mathcal F)$.

The affine smooth curve $U$ is not proper. There is a boundary point
$z\in Z-U$ which is a specialization of a point of $U$. A global
section of $j_!\mathcal F$ vanishes near $z$, and therefore at a
geometric point of $U$. Lissity and connectedness imply that it
vanishes everywhere on $U$, hence everywhere on $Z$.
This is the route through
`AlgebraicGeometry.exists_specializes_notMem_range_of_isProper` and
`AlgebraicGeometry.ProEtale.IsAdicLisseSheaf.isZero_globalSections_adicOpenImmersionLowerShriek`.
