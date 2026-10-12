+++
kind  = "proof"
of    = "sk-thm-sfb-shriek-base-change"
uses = ["sk-thm-sfb-proper-base-change"]
+++
By definition ([sk-def-sfb-shriek-base-change-morphism]), $\mathrm{Ex}_!^c$ is the composite of
two morphisms. The first is the base change morphism of the cartesian square formed by
$p\colon Z\to Y$, $p'\colon Z\times_YY'\to Y'$ and the projections, whiskered by $i_!$. Since $p$
is proper, this is an isomorphism by proper base change [sk-thm-sfb-proper-base-change] for
$\Lambda=\underline E$ resp. $\underline{\Qlb}$. The second is $Rp'_*$ applied to the inverse of
the extension-by-zero exchange isomorphism ([sk-def-sfb-open-base-change]), which is an
isomorphism. A composite of isomorphisms is an isomorphism. Properness enters only through the
structure morphism $p$ of the compactification, not through $f$.
