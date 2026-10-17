+++
kind = "proof"
of = "det-tf-ibc-pasting"
+++
A factorization $f=\bar fj$ exists by Nagata compactification
[thm-nagata-compactification]. The cartesian square for $h$ over $f$ is the vertical
pasting of the cartesian squares for $j_T$ over $j$ and for $\bar h$ over $\bar f$.
The base change map is the mate of the commutative square of inverse images, and
mates paste: the base change map of the pasted square is the composite of the two
base change maps, with the composition isomorphisms of derived direct images at both
ends. This is the vertical pasting law [lemma-weil-pbc-derived-exchange-coherence];
its proof uses only the adjunctions between inverse and direct images, and applies
verbatim to the pro-étale ones.

The base change map for $j$ is an isomorphism by [det-geo-open-finiteness-base-change],
and $Rj_*M$ is bounded constructible by [cor-fin-deligne-open-finite-coefficients];
both are transported to the pro-étale site through the comparison theorems as in
[det-tf-ibc-proper-step]. Since $Rj_*M\in\Dbc(\bar X,A)$,
[det-tf-ibc-proper-step] applies to $N=Rj_*M$ and shows that the base change map for
$\bar f$ is an isomorphism. Hence the composite is an isomorphism.
