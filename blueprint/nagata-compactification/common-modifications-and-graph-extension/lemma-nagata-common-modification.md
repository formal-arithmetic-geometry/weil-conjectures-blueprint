+++
id = "lemma-nagata-common-modification"
kind = "lemma"
title = "Properties of the common modification, [stacks-project]"
order = 444
lean = ["AlgebraicGeometry.nonempty_commonModification"]
uses = ["def-nagata-common-modification", "lemma-nagata-admissible-blowup-comp", "lemma-nagata-elimination-indeterminacy", "lemma-nagata-extend-admissible-blowup", "lemma-nagata-product-ideal-common-blowup", "lemma-nagata-proper-to-separated-target", "lemma-nagata-scheme-image-partial-section", "lemma-nagata-separated-two-open-cover"]
+++
Each constructed map $X'_i\to X_i$ is a $U$-admissible blow-up. Each
$X'_i\to\mathsf{CM}(X_1,X_2;U)$ is an open immersion, their two copies of
$U$ agree, and $\mathsf{CM}(X_1,X_2;U)$ is separated and of finite type
over $S$.

## Proof

Apply Stacks Project, Tag 0F3X (Lemma 38.33.4), with the qcqs base $S$,
the common quasi-compact open $U$, and the separated finite-type
morphisms $X_i\to S$. The two input maps are open immersions and are
identified over $U$, so the hypotheses of that theorem are exactly the
hypotheses of the present construction. Its scheme-theoretic image
$X_{12}\subseteq X_1\times_SX_2$ is the object named in
[def-nagata-common-modification]; the two projections are the partial
sections used by
[lemma-nagata-scheme-image-partial-section]. The theorem first
principalizes the two projection ideals and then takes their product
center, which is the map $X'_{12}\to X_{12}$ supplied by
[lemma-nagata-product-ideal-common-blowup]. Its strict-transform
comparison gives $X'_{12}\subseteq X'_i$ as an open subscheme, with both
restrictions identified with $U$; this is the extension step recorded by
[lemma-nagata-extend-admissible-blowup]. Consequently the two open
immersions glue along exactly $X'_{12}$, not merely along their underlying
topological intersection. The graph of this overlap is a closed immersion
because $X'_2\to S$ is separated. The composite
$X'_{12}\to X_1\times_SX_2$ is proper, and the product map from
$X'_1\times_SX'_2$ to $X_1\times_SX_2$ is separated; hence the graph map
is proper by
[lemma-nagata-proper-to-separated-target]. It is therefore closed,
so the two-open diagonal criterion
[lemma-nagata-separated-two-open-cover] proves that the glued scheme
is separated. The same theorem gives finite type, and the composition
statement
[lemma-nagata-admissible-blowup-comp] shows that each projection is a
$U$-admissible blow-up.
