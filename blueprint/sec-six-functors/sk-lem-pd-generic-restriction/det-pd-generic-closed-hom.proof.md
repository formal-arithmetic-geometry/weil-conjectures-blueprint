+++
kind = "proof"
of = "det-pd-generic-closed-hom"
uses = ["det-pd-generic-direct-image", "lem-exc-closed-support-triangle", "def-weil-open-closed-recollement", "lem-weil-bounded-finite-tor-perfect", "def-weil-site-perfect-complex", "lem-weil-stratum-ambient-hom", "lem-weil-verdier-preservation-strata"]
+++
*Part (1).* Let $j\colon U\hookrightarrow X$ be the open complement of $i$
and pull back the closed-support triangle
([lem-exc-closed-support-triangle])

$$
i_*Ri^!M\longrightarrow M\longrightarrow Rj_*j^*M\longrightarrow.
$$

Inverse image is exact and commutes with closed direct image, and it commutes
with $Rj_*$ by [det-pd-generic-direct-image] applied to $h=j$. The pulled-back
triangle is therefore the closed-support triangle of $g_X^*M$ on the generic
fibre. Since $i_{\bar\eta,*}$ is fully faithful, the identification of the
other two vertices identifies the fibres, $g_Z^*Ri^!M\simeq Ri_{\bar\eta}^!g_X^*M$.

*Part (2).* Choose a finite smooth stratification of $X$, disregarding
nilpotents, on which the restrictions of $K$ are locally perfect
([lem-weil-bounded-finite-tor-perfect], [def-weil-site-perfect-complex]).
The open–closed triangles ([def-weil-open-closed-recollement]) build $K$ by
finitely many cones from objects $t_!P$, where $t\colon S\hookrightarrow X$ is
the inclusion of a stratum and $P$ is locally perfect on $S$. Since both sides
of the comparison are exact in $K$, it suffices to treat $K=t_!P$. Then
([lem-weil-stratum-ambient-hom])

$$
\cHom_X(t_!P,M)\simeq Rt_*\cHom_S(P,Rt^!M)\simeq Rt_*(P^\vee\otimes^{\mathbf L}Rt^!M),
$$

the second step by dualizability of the locally perfect complex $P$. Factor $t$
as an open immersion followed by a closed immersion. Open restriction commutes
with $g^*$, and the closed exceptional restriction does by part (1), so $Rt^!$
commutes with $g^*$. The tensor product $P^\vee\otimes^{\mathbf L}-$ commutes
with inverse image, and $Rt_*$ commutes with $g^*$ by
[det-pd-generic-direct-image]. This proves the comparison on the generators,
and finite cones prove it for $K$. All complexes used remain bounded
constructible ([lem-weil-verdier-preservation-strata]), so each comparison is
applied in its proved range.

*Evaluation.* All maps above are built from localization triangles, pullback
and adjunction units and counits, and the smooth base change, limit and
closed-support comparisons are natural in these maps; hence the comparisons
are compatible with evaluation.
