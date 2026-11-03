+++
id = "lem-weil-pbc-flat-variant-local-criterion"
kind = "lemma"
title = "Variant of the local criterion of flatness"
lean = ["Module.Flat.of_flat_quotient_of_lTensor_injective"]
order = 1912
+++
Let $R\to S$ be a homomorphism of Noetherian commutative rings, let $I\subseteq R$ be an ideal such that $IS$ is contained in the Jacobson radical of $S$, and let $M$ be a finitely generated $S$-module, regarded as an $R$-module. Assume (1) the $R$-linear multiplication map $I\otimes_RM\to M$, $a\otimes x\mapsto ax$, is injective (its kernel is $\mathrm{Tor}_1^R(M,R/I)$, so this is the hypothesis $\mathrm{Tor}_1^R(M,R/I)=0$), and (2) $M/IM$ is a flat $R/I$-module. Then $M$ is a flat $R$-module. In particular this applies when $R\to S$ is a local homomorphism of Noetherian local rings and $I\subseteq\mathfrak m_R$.
