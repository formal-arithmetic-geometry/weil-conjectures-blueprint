+++
id = "prose-20-04"
kind = "hidden"
title = "Real sheaves on an arbitrary base"
order = 771
+++
With these curves we extend the purity theorem for real sheaves on
curves (Theorem [sk-p-real-purity]) to mixedness of real sheaves on
any base. The curves preserve geometric irreducibility, so we first
split a lisse sheaf into geometrically irreducible pieces.

Geometric irreducibility, rather than irreducibility as a Weil sheaf,
is what the curves can preserve, and the two notions differ. An irreducible Weil sheaf need not be
geometrically irreducible. Let $\chi$ be a character of
$\mathbf F_{q^2}^\times$ with $\chi^q\ne\chi$, and let $g$ be the map
from $\mathbf G_m$ over $\mathbf F_{q^2}$ to $\mathbf G_m$ over
$\mathbf F_q$. The direct image under $g$ of the Kummer sheaf of $\chi$ is an
irreducible Weil sheaf of rank two, because Frobenius exchanges the two
geometrically distinct Kummer sheaves of $\chi$ and $\chi^q$ into which
it splits geometrically. After the quadratic constant extension the
two pieces are Weil sheaves themselves. In general a finite constant
extension makes the geometric constituents into Weil subquotients
(Lemma [sk-lem-wgen-geometric-constituents]), and the proof of
Theorem [sk-i-dl-general-real] descends mixedness back along this
extension by a trace retraction. Constructible sheaves are reduced to
lisse sheaves on smooth affine strata, and the strata are glued by
Lemma [sk-l-dl-general-quasifinite].
