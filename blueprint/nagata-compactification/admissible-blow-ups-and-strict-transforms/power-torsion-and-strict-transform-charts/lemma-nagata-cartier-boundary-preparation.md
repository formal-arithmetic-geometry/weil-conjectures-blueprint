+++
id = "lemma-nagata-cartier-boundary-preparation"
kind = "lemma"
title = "Preparation of a Cartier boundary, [stacks-project]"
order = 358
lean = ["AlgebraicGeometry.exists_admissibleBlowup_cartierBoundary"]
uses = ["def-nagata-admissible-blowup", "def-nagata-effective-cartier-ideal", "lemma-nagata-qc-open-complement-ideal-exists", "thm-nagata-blowup-principalizes-center", "thm-nagata-global-blowup-complement"]
+++
Let $X$ be qcqs and let $U\subseteq X$ be a quasi-compact open. There is a
$U$-admissible blow-up $X_1\to X$ for which the complement of the inverse
image of $U$ is the support of an effective Cartier ideal.

## Proof

Choose the finite type quasi-coherent ideal $\mathcal I$ with
$V(\mathcal I)=X\setminus U$ supplied by
[lemma-nagata-qc-open-complement-ideal-exists]. Its restriction to
$U$ is the unit ideal, so its blow-up is $U$-admissible. Moreover,
[thm-nagata-blowup-principalizes-center] makes the extended ideal an
effective Cartier ideal. Its vanishing locus is the inverse image of
$V(\mathcal I)$, which is the complement of the inverse image of $U$;
the latter inverse image is the preserved open by
[thm-nagata-global-blowup-complement]. Hence this Cartier ideal has
precisely the required boundary support.
