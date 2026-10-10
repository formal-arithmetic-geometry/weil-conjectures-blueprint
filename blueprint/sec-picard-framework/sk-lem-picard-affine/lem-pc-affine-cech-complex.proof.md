+++
kind  = "proof"
of    = "lem-pc-affine-cech-complex"
+++
Localize the displayed complex at $f_j$. The corresponding cover
contains $D(f_j)_{f_j}=\operatorname{Spec}(A_{f_j})$.
Write alternating cochains using all ordered index tuples, with
repeated indices giving zero and permutations acting by their signs.
Insertion of the index $j$ in the first slot defines a contraction:
$(hc)_{i_0\ldots i_{q-1}}=c_{j i_0\ldots i_{q-1}}$.
The usual restriction to the additional intersection is an
isomorphism after localizing at $f_j$. Expanding the alternating
differential gives $dh+hd=1$, because the term deleting the added
$j$ is the identity and all other terms cancel in pairs.
Consequently the localized complex is exact for every $j$.
Localization is exact, so every cohomology module $N$ satisfies
$N_{f_j}=0$ for all $j$. For $v\in N$, choose exponents $a_j$
with $f_j^{a_j}v=0$. The elements $f_j^{a_j}$ still generate the
unit ideal (no prime contains them all), hence $v=0$.
Thus every cohomology module is zero.
