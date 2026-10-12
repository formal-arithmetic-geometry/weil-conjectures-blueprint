+++
id = "lem-weil-pbc-idempotents-determined-modulo-radical"
kind = "lemma"
title = "Idempotents are determined modulo an ideal in the Jacobson radical"
lean = ["IsIdempotentElem.eq_of_sub_mem_of_le_jacobson"]
source = "literature/stacks-project/more-algebra.tex, Lemma Tag 09XF (lemma-idempotents-determined-modulo-radical), with Definition Tag 0ELY (definition-zariski-pair: a pair $(A,I)$ with $I$ in the Jacobson radical); its proof: an idempotent of a local ring is $0$ or $1$, so an idempotent is determined by the set of maximal ideals where it vanishes (Algebra, Lemma Tag 00HN, lemma-characterize-zero-local)"
+++
Let $R$ be a commutative ring and $J\subseteq R$ an ideal contained in the Jacobson radical of $R$. If $e,e'\in R$ are idempotents ($e^2=e$, $e'^2=e'$) with $e-e'\in J$, then $e=e'$; that is, the map from idempotents of $R$ to idempotents of $R/J$ is injective.
