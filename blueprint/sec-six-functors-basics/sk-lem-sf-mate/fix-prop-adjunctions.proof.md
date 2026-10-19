+++
kind  = "proof"
of    = "fix-prop-adjunctions"
+++
Step 1: the derived adjunction $(Lf^*,Rf_*)$. The sheaf-level
adjunction of inverse image and direct image, its derived form
$Lf^*\dashv Rf_*$ on the categories of
[def-weil-pbc-derived-categories], and its unit and counit
$\eta_f,\varepsilon_f$ are [def-weil-pbc-inverse-image] of
the ambient-foundations chapter (finite etale level; the pro-etale level is the site
transport of the same datum, the operations being those of
[def-weil-derived-pullback-tensor-hom] and
[def-weil-derived-direct-image]); the triangle identities hold
for the derived adjunction because the derived unit and counit are
the images of the sheaf-level ones under K-injective and K-flat
replacement of [def-weil-pbc-kinjective-resolutions], the
resolution-independence of
[lem-weil-derived-tensor-resolution-independent], and the sheaf-level
triangle identities are preserved by the derived functors. Step 2:
the exceptional adjunction $(Rf_!,Rf^!)$. The natural adjunction
isomorphisms $\Hom_Y(Rf_!K,L)\cong\Hom_X(K,Rf^!L)$ characterize
$Rf^!$ by [def-weil-exceptional-inverse-image], so the
adjunction $Rf_!\dashv Rf^!$, its unit and counit, and the
triangle identities are, at the finite level, the datum of
[def-weil-exceptional-adjoint-admissibility]; the agreement of
the units and the counits with the refinement comparisons is
condition (1) of that definition, and the restriction to the
finite-Tor subcategories is condition (3) of the same definition. At
$\Lambda=\mathcal O_E,E,\Qlb$ the adjunction $Rf_!\dashv Rf^!$ on the
condensed categories is that of [sk-thm-existence] (3), it restricts to
$\Dctf=\Dbc$ by [sk-thm-existence] (4), and it agrees with the composite
adjunction $Rp_*i_!\dashv i^*Rp^!$ of [sk-def-sfb-dc-upper-shriek]; the
agreement with the refinement comparisons follows from the uniqueness of
adjoints, the right adjoint $Rp^!$ being determined up to unique
isomorphism.
Step 3: composition. The composite adjunction of step 1 is the
paste of the component adjunctions (the unit of the composite is the
composite of the units, the counit the composite of the counits, and
the triangle identities of the composite are the composites of the
triangle identities of the components, through the composition
isomorphisms $R(gf)_*\cong Rg_*Rf_*$ of
[lem-weil-derived-direct-image-composition], which are natural, unital
and associative); for the
exceptional pair, the mate of the composition isomorphism of
[thm-sf-comp-composition] (at $\mathcal O_E,E,\Qlb$ the composition
isomorphism of [sk-thm-sf-comp-composition] (1) on the condensed categories)
gives an
isomorphism $(g\circ f)^!\cong f^!g^!$, the pasted units and
counits are the mates of this isomorphism through the two component
adjunctions, and the triangle identities are the composite versions
of the component ones. Step 4: exchange compatibility. The
transpose of $\operatorname{Ex}_!$ is obtained by the mate
calculus of [def-exchange-projection]: the exchange
transformation is defined as the transpose of the compatibility of
the pullbacks with the counit, and the same holds for
$\operatorname{Ex}_*$; the compatibility of these transposes with
the composition law is [fix-lem-exchanges].
