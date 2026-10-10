+++
kind  = "proof"
of    = "lem-pur-lisse-uniqueness"
+++
By [lem-pur-lisse-morphism-rigidity](1) the sheaf
$\mathcal Hom(L,M)$ is finite locally constant on the source, and by
[lem-pur-lisse-morphism-rigidity](2) a morphism between finite
locally constant sheaves vanishes as soon as it vanishes at one
geometric point of every connected component of that source. Apply
this to the difference of the two morphisms. For the first assertion
the difference vanishes on $\mathbf G_{m,B}$, and every connected
component of $\mathbf A^1_B$ meets $\mathbf G_{m,B}$ by
[lem-pur-a1-components](2); for the second assertion the
difference is a morphism on $\mathbf G_{m,B}$ whose stalk vanishes at
the unit section, and every connected component of
$\mathbf G_{m,B}$ meets the image of that section by
[lem-pur-a1-components](3). This is ordinary faithfulness for
morphisms of sheaves, not the false derived-category faithfulness
excluded in the remark after [thm-pur-td-criterion].
