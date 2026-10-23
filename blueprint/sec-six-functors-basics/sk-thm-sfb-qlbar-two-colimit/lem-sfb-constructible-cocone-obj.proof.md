+++
kind  = "proof"
of    = "lem-sfb-constructible-cocone-obj"
uses = ["sk-prop-sfb-qlbar-colimit-x", "sk-def-sfb-constructible", "det-def-sfb-bounded-constructible", "lem-sfb-qlbar-flat", "lem-sfb-constructible-cocone-hom-surj"]
+++
Constructible descent, by induction on the number of nonzero cohomology sheaves of $K$.

*Modules.* Let $M$ be a constructible $\overline{\mathbf Q}_{\ell,X}$-module ([sk-def-sfb-constructible]): on the
strata of a finite stratification of $X$ it is locally finitely presented. A finite
presentation is a matrix with finitely many entries, sections of
$\overline{\mathbf Q}_{\ell,X}=\operatorname{colim}_EE_X$ ([sk-prop-sfb-qlbar-colimit-x]) over quasi-compact
opens, and finitely many such sections are defined over a single finite extension $E$. So $M$
is $\overline{\mathbf Q}_{\ell,X}\otimes_{E_X}M_E$ for a constructible $E_X$-module $M_E$, glued over the finitely
many strata and charts; the gluing data are again finitely many morphisms, which descend after
enlarging $E$.

*Complexes.* For $K$ with more than one nonzero cohomology sheaf, a truncation triangle
$\tau_{\le n}K\to K\to\tau_{>n}K\xrightarrow{\delta}$ has outer terms of shorter length, which by
induction are $T_{E,\Qlb}$ of bounded constructible $E_X$-complexes for a common $E$. The
extension of scalars is exact ([lem-sfb-qlbar-flat]) and so commutes with truncations. The
connecting morphism $\delta$ descends to some finite $E'\supseteq E$ by
[lem-sfb-constructible-cocone-hom-surj]; its cone over $E'$ is bounded constructible (the
bounded constructible complexes form a triangulated subcategory on Noetherian $X$,
[det-def-sfb-bounded-constructible]), and its extension of scalars is isomorphic to $K$.
