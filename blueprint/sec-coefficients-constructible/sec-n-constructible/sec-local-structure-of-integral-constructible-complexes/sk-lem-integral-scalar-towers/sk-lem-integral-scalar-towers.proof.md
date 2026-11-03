+++
kind = "proof"
of = "sk-lem-integral-scalar-towers"
+++
For (1) we use that a minimal complex over the local ring
$\mathcal O_E/\pi_E^n$ is determined up to isomorphism of complexes, not
only up to homotopy, so that the transition maps can be made into
equalities of matrices and passed to the limit. Represent each $M_n$ by a minimal finite free complex, obtained by
cancelling unit entries in the differential matrices. Its reduction
modulo $\pi_E$ has zero differential, so its rank in each degree is
$\dim_{\mathbf F_E}H^q(M_1)$, independent of $n$ and nonzero only in
finitely many degrees. The given isomorphism
$M_{n+1}/\pi_E^n\simeq M_n$ between minimal complexes is represented
by a chain homotopy equivalence $f$, with homotopy inverse $g$. Since
both complexes have zero differential modulo $\pi_E$, the relations
$gf-1=dh+hd$ and $fg-1=dh'+h'd$ show that $f$ is an isomorphism modulo
$\pi_E$ in each degree. Hence its matrices are already invertible over
$\mathcal O_E/\pi_E^n$. Lifting them to invertible matrices over
$\mathcal O_E/\pi_E^{n+1}$ and changing bases, we may assume that the
differential at level $n+1$ reduces exactly to the differential at
level $n$, with the given transition in the derived category.
By induction we get compatible matrices. Their limits define
$P^\bullet$, whose differential squares to zero because it does so
modulo every $\pi_E^n$. The identifications with the $M_n$ are
compatible by construction.

(2) The two-term resolution of $\mathcal O_E/\pi_E^n$ gives an exact sequence

$$
0\to H^q(Q^\bullet)/\pi_E^n\to H^q(Q^\bullet/\pi_E^n)
\to H^{q+1}(Q^\bullet)[\pi_E^n]\to0.
$$

For the transition from level $m$ to level $n$,
the induced map on the right-hand terms is multiplication by
$\pi_E^{m-n}$, because the corresponding map of resolutions is the
identity in degree zero and multiplication by $\pi_E^{m-n}$ in degree
$-1$. If $m-n\ge e$, this map is zero, since $H^{q+1}(Q^\bullet)[\pi_E^m]$
consists of torsion elements and $\pi_E^e$ kills them. Hence the image of
$H^q(Q^\bullet/\pi_E^m)$ lies in the left-hand term
$H^q(Q^\bullet)/\pi_E^n$ at level $n$, which is the image of
$H^q(Q^\bullet)$. Conversely, the map from $H^q(Q^\bullet)$ factors
through level $m$. This proves the equality.
