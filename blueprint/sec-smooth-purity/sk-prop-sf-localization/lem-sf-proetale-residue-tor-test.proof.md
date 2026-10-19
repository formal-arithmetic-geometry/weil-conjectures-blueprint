+++
kind  = "proof"
of    = "lem-sf-proetale-residue-tor-test"
+++
One direction is the definition [def-weil-finite-tor-amplitude], the
constant sheaf $\kappa_T$ being a sheaf of $A$-modules placed in degree
zero. Conversely, every sheaf $N$ of $\kappa$-modules is flat over
$\kappa$ (sectionwise tensor over a field is exact, and so is
sheafification), so by associativity of the derived tensor product of
[def-weil-derived-tensor]

$$
\mathcal H^r(K\otimes^L_AN)\cong\mathcal H^r\bigl((K\otimes^L_A\kappa_T)
\otimes^L_\kappa N\bigr)\cong\mathcal H^r(K\otimes^L_A\kappa_T)\otimes_\kappa N,
$$

which vanishes outside $[a,b]$. A sheaf $M$ of $A$-modules has the finite
filtration $\pi_E^sM$, $0\le s\le n$, whose graded pieces are sheaves
of $\kappa$-modules; the long exact cohomology sequences of
$K\otimes^L_A-$ applied to the short exact sequences of this filtration
give $\mathcal H^r(K\otimes^L_AM)=0$ for $r\notin[a,b]$, which is finite
Tor amplitude in $[a,b]$. The argument uses no stalks and no comparison
with the étale site.
