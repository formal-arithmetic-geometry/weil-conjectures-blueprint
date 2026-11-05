+++
id = "prose-18-06"
kind = "hidden"
title = "Mixedness of real sheaves (1)"
order = 1333
+++
With these curves we pass from the purity theorem for real sheaves on
curves (Theorem [theorem-purity-real-sheaves-curves]) to the
mixedness of real sheaves on any base. The curves preserve
geometric irreducibility, so we first split a lisse sheaf into
geometrically irreducible pieces. These pieces need not be Weil
sheaves, because an irreducible Weil sheaf need not be geometrically
irreducible. For example, let $\chi$ be a character of
$\mathbf F_{q^2}^\times$ with $\chi^q\ne\chi$, and let $g$ be the map
from $\mathbf G_m$ over $\mathbf F_{q^2}$ to $\mathbf G_m$ over
$\mathbf F_q$. Geometrically, the direct image under $g$ of the Kummer
sheaf of $\chi$ splits into the Kummer sheaves of $\chi$ and $\chi^q$,
which are distinct. Frobenius exchanges them, and so the direct image
is an irreducible Weil sheaf of rank two. After the quadratic constant
extension the two pieces are Weil sheaves themselves. In general, the
geometric constituents become Weil subquotients after a finite constant
extension
(Lemma [lemma-geometric-constituents-after-constant-extension]).
In the proof of
Theorem [theorem-real-constructible-sheaves-are-mixed] we descend
mixedness back along this extension by a trace retraction. We also
reduce constructible sheaves to lisse sheaves on smooth affine strata,
and glue the strata using
Lemma [lemma-finite-quasi-finite-direct-images].
