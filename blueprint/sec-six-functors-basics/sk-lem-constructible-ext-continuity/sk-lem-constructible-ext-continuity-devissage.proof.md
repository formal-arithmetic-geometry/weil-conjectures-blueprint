+++
kind  = "proof"
of    = "det-lem-constructible-ext-continuity-devissage"
+++
Shifts: $\Hom(C[n],K[q])=\Hom(C,K[q-n])$ for both sides, compatibly with the map. Isomorphisms
are clear.

Extensions: $\Hom(-,K_i[q])$ and $\Hom(-,K[q])$ are cohomological functors, so the triangle
gives long exact sequences
$$
\Hom(C'[1],K_i[q])\to\Hom(C'',K_i[q])\to\Hom(C,K_i[q])\to\Hom(C',K_i[q])\to\Hom(C''[-1],K_i[q]),
$$
natural in $i$ and mapping to the corresponding sequence for $K$. Filtered colimits of
abelian groups are exact, so the colimit over $i$ of the first sequence is exact. The four
outer comparison maps are bijective because $C',C''\in\mathcal C$ (and $\mathcal C$ is
closed under shifts), so the middle one is bijective by the five lemma.

The consequence follows by induction along the finite construction; for $\Lambda=E,\Qlb$,
every object of $\Dbc$ is built from objects $a_!L[n]$ with $L$ lisse, i.e. finite locally
free, by finitely many cones.
