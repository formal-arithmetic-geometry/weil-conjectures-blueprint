+++
kind = "proof"
of = "lemma-gluing-after-admissible-blow-ups--1"
order = 1455002
uses = ["lemma-schematic-closure-uniqueness", "definition-strict-transform", "theorem-elimination-indeterminacy", "lemma-products-composites-u-admissible-blow", "lemma-making-open-schematically-dense"]
+++
Let $G$ be the scheme-theoretic image of
$(j_1,j_2):U\to T_1\times_ST_2$. By
[lemma-schematic-closure-uniqueness], $U$ is an open subscheme of $G$.
Since each graph is closed over the corresponding copy of $U$, the
projections $p_i:G\to T_i$ restrict to isomorphisms over $j_i(U)$,
and both inverse images of these opens are the same copy of $U$ in $G$.

Apply [theorem-elimination-indeterminacy] to each $p_i$, obtaining
$U$-admissible centers $\mathcal I_i$ on $T_i$ whose strict transforms
are open immersions. The strict transform is the blow-up of $G$ in
$\mathcal K_i=\mathcal I_i\mathcal O_G$, by
`AlgebraicGeometry.Scheme.IdealSheafData.exists_blowup_comap_iso_strictTransform`.
Set

$$
G'=\Bl_{\mathcal K_1\mathcal K_2}(G).
$$

The product formula in [lemma-products-composites-u-admissible-blow]
expresses $G'$ as a further blow-up of either strict transform. These
further centers avoid the inverse image of $U$. Extend them from the
open strict transforms and compose the admissible blow-ups, again by
[lemma-products-composites-u-admissible-blow]. This gives single
$U$-admissible blow-ups $b_i:T_i'\to T_i$ and open immersions
$n_i:G'\to T_i'$ over $T_i$. This extension step is
`AlgebraicGeometry.IsAdmissible.exists_isOpenImmersion_blowup`.
The product center avoids $U$, so $U$ lifts to $G'$ and hence to
both $T_i'$.

The map $G'\to T_1'\times_ST_2'$ is an immersion: it is a graph over
the open immersion $n_1$, and $T_2'$ is separated over $S$.
Its composite with $T_1'\times_ST_2'\to T_1\times_ST_2$ is proper,
since $G'\to G$ is proper and $G\to T_1\times_ST_2$ is a closed
immersion. The comparison morphism of products is separated, so
$G'\to T_1'\times_ST_2'$ is universally closed and is therefore a
closed immersion. Glue $T_1'$ and $T_2'$ along $G'$. The closed graph
gives separatedness of the glued scheme; local finite type and
quasi-compactness follow from the two open charts. This is the
construction in `AlgebraicGeometry.nonempty_commonModification`.

For density, suppose that the $T_i$ are Noetherian. For any common
modification, the image of $u_i$ is $b_i^{-1}(j_i(U))$, since $b_i$ is
an isomorphism over $j_i(U)$. The density argument in
[lemma-making-open-schematically-dense] shows that the complement of
the exceptional divisor is dense in $T_i'$. Over this complement the
blow-up is an isomorphism, so the inverse image of the dense set
$j_i(U)$ is dense in $T_i'$; Lean uses
`AlgebraicGeometry.IsAdmissible.dense_preimage_blowupMap`.
Every nonempty open of $T$ meets one of the two charts, and its inverse
image in that chart meets $u_i(U)$. Thus it meets $j(U)$, as asserted
by `AlgebraicGeometry.CommonModification.dense_range_j`.
