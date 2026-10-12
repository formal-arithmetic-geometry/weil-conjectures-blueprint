+++
id = "lem-weil-pbc-etale-section-localization"
kind = "lemma"
title = "Localization equivalence from an idempotent kernel"
lean = ["Algebra.Etale.exists_localization_equiv_of_idempotent"]
source = "literature/stacks-project/more-algebra.tex, proof of Lemma Tag 09XI (lemma-characterize-henselian-pair), (5)$\\Rightarrow$(2), first paragraph: 'the surjective ring map $A'/IA'\\to A/I$ is etale by Algebra, Lemma 00U7 (lemma-map-between-etale) and then we get the desired idempotent by Algebra, Lemma 00U8 (lemma-surjective-flat-finitely-presented)' (literature/stacks-project/algebra.tex); used without comment in the proof of Lemma Tag 0A02 (lemma-henselization): '$B'/IB'=A/I\\times C$'"
+++
Let R and S be commutative rings, S an R-algebra, and s:S→R an R-algebra homomorphism. Let e in S be idempotent, s(e)=1, and ker(s)=(1-e)S. There is an R-algebra equivalence S[1/e]≅R sending x/1 to s(x) for every x in S.
