+++
id = "thm-exc-proetale-recollement"
kind = "theorem"
title = "The ambient open-closed derived triangle"
order = 1903
uses = ["def-weil-open-closed-recollement", "def-weil-pbc-derived-categories", "def-weil-pbc-scheme-conventions", "lem-exc-proetale-closed-exact", "lem-weil-extension-by-zero-exact", "prop-weil-pbc-proetale-constant-exact", "thm-exc-proetale-open-closed-exact"]
+++
For a closed immersion with quasi-compact complementary open immersion, the
canonical pair of the open-closed recollement extends to a natural
distinguished triangle
$$
 j_!j^*K\longrightarrow K\longrightarrow Ri_*i^*K
 \longrightarrow j_!j^*K[1]
$$
on the ambient ordinary derived category of constant-coefficient pro-etale
module sheaves. No boundedness or constructibility of $K$ is required.

## Proof

Represent $K$ by an ordinary complex. Apply
[thm-exc-proetale-open-closed-exact] degree by degree; naturality makes the
resulting maps commute with the differentials, giving a short exact sequence
of complexes. The functors $j_!$, $j^*$, $i^*$, and $i_*$ are exact, by
exactness of extension by zero, of constant-coefficient pro-etale inverse
image, and by [lem-exc-proetale-closed-exact]. Consequently they preserve
acyclic complexes and quasi-isomorphisms. In particular $Ri_*$ is
represented by the underived $i_*$ on any complex, even when unbounded. The
triangle of a short exact sequence of complexes therefore gives the
displayed distinguished triangle. Its first two maps are the specified
counit and unit of the recollement, by the sheaf-level theorem. Morphisms of
complexes give morphisms of these exact sequences and their triangles, which
descend through quasi-isomorphisms. This proves the claimed naturality in
the ordinary derived category.
