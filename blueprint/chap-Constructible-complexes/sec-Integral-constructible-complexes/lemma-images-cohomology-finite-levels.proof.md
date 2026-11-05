+++
kind = "proof"
of = "lemma-images-cohomology-finite-levels"
order = 236
+++
The two-term resolution of $\mathcal O_E/\pi_E^n$ gives an exact sequence

$$
0\to H^q(Q^\bullet)/\pi_E^n\to H^q(Q^\bullet/\pi_E^n)
\to H^{q+1}(Q^\bullet)[\pi_E^n]\to0.
$$

For the transition from level $m$ to level $n$,
the induced map on the right-hand terms is multiplication by
$\pi_E^{m-n}$, because the corresponding map of resolutions is the
identity in degree zero and multiplication by $\pi_E^{m-n}$ in degree
$-1$. If $m-n\ge e$, this map is zero, since $H^{q+1}(Q^\bullet)[\pi_E^m]$
consists of torsion elements and $\pi_E^e$ kills them. The image of
$H^q(Q^\bullet/\pi_E^m)$ therefore lies in the left-hand term
$H^q(Q^\bullet)/\pi_E^n$ at level $n$, which is the image of
$H^q(Q^\bullet)$. The reverse inclusion holds because the map from
$H^q(Q^\bullet)$ factors through level $m$.
