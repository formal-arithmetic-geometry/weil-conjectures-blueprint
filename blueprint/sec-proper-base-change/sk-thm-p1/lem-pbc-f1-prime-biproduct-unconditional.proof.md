+++
kind = "proof"
of = "lem-pbc-f1-prime-biproduct-unconditional"
uses = ["def-weil-pbc-cohomology-pullback", "def-weil-pbc-eight-curve-assertions"]
+++
*Cohomology of a finite direct sum.* Taking underlying abelian sheaves and taking cohomology $H^q$ are additive functors. Applied to the isomorphism $e$, their composite identifies $H^q(X,H)$ with the finite product $\prod_aH^q(X,G_a)$, with coordinate maps induced by $e$ followed by the projections $\bigoplus_bG_b\to G_a$; this holds also for the empty index set. A product is a singleton if and only if every factor is, since every factor contains zero, and a finite product is finite if and only if every factor is.

*Pullback maps.* For any morphism of schemes $a$ and degree $q$, the cohomology pullback along $a$ [def-weil-pbc-cohomology-pullback] is natural in the sheaf, so in the product coordinates it is the product of the pullback maps of the summands. Surjectivity of the product map is equivalent to surjectivity of each factor: for the forward direction lift vectors supported in one coordinate, for the converse choose coordinate preimages. Injectivity is equivalent too: each summand $G_a$ is a retract of $H$ via the inclusion $G_a\to\bigoplus_bG_b$ followed by $e^{-1}$, and $e$ followed by the projection, which with naturality gives the forward implication; the converse follows from joint injectivity of the coordinates. Bijectivity combines both.

*The assertions.* Unfold $C_1,C_2,C_5,C_7,C_8$ of [def-weil-pbc-eight-curve-assertions] and apply these coordinatewise tests degree by degree. For $C_2$ and $C_7$ the affineness or properness hypothesis is common to $H$ and the $G_a$. For $C_5$ use the assumed constructibility of $H$ in one direction and that of the $G_a$ in the other. Assembling the five equivalences gives the statement.
