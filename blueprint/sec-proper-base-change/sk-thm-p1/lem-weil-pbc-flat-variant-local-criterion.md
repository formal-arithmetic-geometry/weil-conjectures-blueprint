+++
id = "lem-weil-pbc-flat-variant-local-criterion"
kind = "lemma"
title = "Variant of the local criterion of flatness"
lean = ["Module.Flat.of_flat_quotient_of_lTensor_injective"]
source = "literature/stacks-project/algebra.tex, Algebra, Lemma Tag 00ML (lemma-variant-local-criterion-flatness, line 23751), with the hypothesis Tor_1^R(M,R/I)=0 rewritten by Remark Tag 00M6 (remark-Tor-ring-mod-ideal, line 18690: Tor_1^R(M,R/I) = Ker(I (x)_R M -> M)); its proofs use Lemma 051C (lemma-what-does-it-mean), Lemma 00MK (lemma-local-criterion-flatness) and Lemma 00HK (lemma-flat-eq)"
+++
Let $\varphi:R\to S$ be a local homomorphism of Noetherian local rings `IsNoetherianRing` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/Noetherian/Defs.lean)) ($\varphi(\mathfrak m_R)\subseteq\mathfrak m_S$), let $I\subsetneq R$ be a proper ideal and let $M$ be a finitely generated $S$-module `Module.Finite` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/Finiteness/Defs.lean)), regarded as an $R$-module via $\varphi$. Assume (1) the $R$-linear multiplication map $I\otimes_RM\to M$, $a\otimes x\mapsto\varphi(a)x$, is injective (by Stacks, Remark 00M6, its kernel is $\mathrm{Tor}_1^R(M,R/I)$, so this is the hypothesis $\mathrm{Tor}_1^R(M,R/I)=0$), and (2) $M/IM$ is a flat $R/I$-module `Module.Flat, RingHom.Flat` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/Flat/Basic.lean)). Then $M$ is a flat $R$-module.
