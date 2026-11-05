+++
kind = "proof"
of = "lemma-sheaves-finite-support-finite-morphisms--2"
order = 1597004
uses = ["lemma-sheaves-finite-support-finite-morphisms--1", "proposition-extension-zero-restriction-closed-subscheme", "lemma-finite-morphisms", "lemma-finite-morphisms-cohomology"]
+++
The projection $g$ gives a bijection of the finite sets of points of
$C'$ and $C$, and $C'$ again has dimension at most zero. Choose a
$k'$-valued geometric point $t_y$ over each $y\in C'$ and use
$g\circ t_y$ as the corresponding geometric point of $C$.

Identify global sections on both schemes with the products of these
stalks, as in [lemma-sheaves-finite-support-finite-morphisms--1].
Here Lean uses `AlgebraicGeometry.Scheme.zeroDimensional_sections_stalks`:
the singleton opens are spectra of strictly henselian local rings,
their sections are the chosen geometric stalks, and the sheaf condition
for the disjoint cover gives the product. Inverse image identifies
$(g^*F)_{t_y}$ with $F_{g\circ t_y}$, compatibly with germs of global
sections. Under the product identifications, the canonical pullback map
is therefore a product of stalk isomorphisms, reindexed by the point
bijection, and is an isomorphism. The same argument includes the empty
scheme, with empty products.

In the curve argument, this calculation is applied to the reduced closed
complement $i:Z\hookrightarrow X$ of a dense open $U$. A sheaf $Q$
with $Q|_U=0$ is identified with $i_*i^*Q$ by the open-closed exact
sequence [proposition-extension-zero-restriction-closed-subscheme].
The complement $Z$ has dimension at most zero. Finite base change
[lemma-finite-morphisms] and the cohomology comparison
[lemma-finite-morphisms-cohomology] transport the degree-zero pullback
isomorphism from $Z$ to $X$. This is the passage through
`AlgebraicGeometry.IsCurve.dense_open_closed_term` in the Lean proof.
