+++
kind  = "proof"
of    = "lem-fin-normalization-extends-cover"
+++
By [lem-fin-etale-normal-components], connectedness
makes $P$ normal integral. Its function field is
finite over that of $V$, because the map is finite.
On an affine open $\operatorname{Spec}B\subset V$, write
its inverse image as $\operatorname{Spec}D$. Here $D$
is a normal domain, finite and integral over $B$, with
fraction field $k(P)$. An element of $k(P)$ integral
over $B$ is also integral over $D$, hence belongs to
$D$; conversely every element of $D$ is integral over
$B$. Thus $D$ is exactly the integral closure of
$B$. This identifies the restrictions of the construction
in [def-fin-normalization-extension]; it glues because
the identifications are the identity inside the function
field. The total extension is finite by
[lem-fin-normalization-extension-finite] and has normal
integral source in the sense of
[def-sbc-normal-dominant-galois].
