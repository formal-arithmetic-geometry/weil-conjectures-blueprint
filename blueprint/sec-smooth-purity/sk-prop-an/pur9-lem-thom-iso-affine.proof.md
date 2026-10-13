+++
kind = "proof"
of = "pur9-lem-thom-iso-affine"
uses = ["pur9-lem-orientation-iso", "pur9-lem-twist-passage", "pur9-lem-upper-shriek-composition"]
+++
Induction on $c$. The case $c=1$ is Lemma [pur9-lem-orientation-iso], applied over $B$ and over $B'$. In the recursive step every factor is an isomorphism: $\mathrm{th}_{c-1}$ by induction, $\mathrm{pur}_{s'}$ by Lemma [pur9-lem-orientation-iso] over $B'$, and $\tau$ and $c$ by Lemmas [pur9-lem-twist-passage] and [pur9-lem-upper-shriek-composition].
