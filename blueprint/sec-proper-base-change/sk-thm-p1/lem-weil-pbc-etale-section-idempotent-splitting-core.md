+++
id = "lem-weil-pbc-etale-section-idempotent-splitting-core"
kind = "lemma"
title = "Core idempotent decomposition"
lean = ["Algebra.Etale.exists_idempotent_core"]
source = "literature/stacks-project/more-algebra.tex, proof of Lemma Tag 09XI (lemma-characterize-henselian-pair), (5)$\\Rightarrow$(2), first paragraph: 'the surjective ring map $A'/IA'\\to A/I$ is etale by Algebra, Lemma 00U7 (lemma-map-between-etale) and then we get the desired idempotent by Algebra, Lemma 00U8 (lemma-surjective-flat-finitely-presented)' (literature/stacks-project/algebra.tex); used without comment in the proof of Lemma Tag 0A02 (lemma-henselization): '$B'/IB'=A/I\\times C$'"
+++
Let R and S be commutative rings, with S an étale R-algebra `AlgebraicGeometry.Etale` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/AlgebraicGeometry/Morphisms/Etale.lean)), and let s:S→R be an R-algebra homomorphism. There is an idempotent e in S such that s(e)=1 and ker(s)=(1-e)S. The corner C=(1-e)S, with identity 1-e and R-algebra map r↦(1-e)algebraMap(r), admits an R-algebra equivalence S≅R×C whose first projection is s.
