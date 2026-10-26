+++
id = "prop-sfb-bounded-constructible-triangulated"
kind = "proposition"
title = "Bounded constructible complexes form a triangulated subcategory"
order = 1151
uses = ["def-sfb-bounded-constructible-complexes", "det-def-sfb-pulled-back-coefficients-definition", "def-sfb-continuous-map-condensed-ring", "def-sfb-padic-subfield-condensed-ring", "def-sfb-padic-integers-condensed-ring"]
lean = ["AlgebraicGeometry.ProEtale.isTriangulated_boundedConstructible"]
+++
In the situation of [def-sfb-bounded-constructible-complexes], take $\mathcal A=\Ab$ and
$\mathcal R=\Lambda_X$ the coefficient ring pulled back from the point
[det-def-sfb-pulled-back-coefficients-definition], where $\ell$ is a prime and $\Lambda$ is
one of the following commutative condensed rings: $\underline E$ for a finite extension $E$
of $\mathbf Q_\ell$ [def-sfb-padic-subfield-condensed-ring]; $\underline{\cO}_E$ for its ring
of integers $\cO_E$ [def-sfb-padic-integers-condensed-ring]; the condensed ring
$\underline{\Qlb}$ of continuous maps with values in a finite subextension of
$\Qlb/\mathbf Q_\ell$; or $\underline T$ [def-sfb-continuous-map-condensed-ring] for a finite
discrete commutative ring $T$ with $\ell^nT=0$ for some $n$. Assume that the underlying
topological space of $X$ is Noetherian. Then the bounded constructible complexes form a
triangulated subcategory of $D(\Mod_{\Lambda_X})$: they contain $0$, are stable under
shifts and isomorphisms, and with two vertices of a distinguished triangle contain the
third.
