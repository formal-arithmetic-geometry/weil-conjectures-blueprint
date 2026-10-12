+++
id = "lem-weil-pbc-finite-idempotent-factor-transfer"
kind = "lemma"
title = "Transfer of a finite idempotent factor through an away isomorphism"
lean = ["Algebra.finite_idempotent_factor_transfer"]
source = "literature/stacks-project/more-algebra.tex, Tag 09XI (lemma-characterize-henselian-pair), proof of (5) implies (2), identifying B'₁ with A'₁ and the compatible fibre splitting; details proved directly from Mathlib localization and integral-algebra lemmas; read at https://stacks.math.columbia.edu/tag/09XI on 2026-10-12"
+++
Let $A,B$ be commutative rings with $B$ an $A$-algebra and $I\subset A$ an ideal. Let $D\subset B$ be an $A$-subalgebra finite as an $A$-module `Module.Finite` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/Finiteness/Defs.lean)). Let $C$ be an $(A/I)$-algebra and $\Phi:D/ID\cong (A/I)\times C$ an isomorphism respecting the $A/I$ structure maps. Suppose $b,d\in D$, $d^2=d$, $\alpha\in A$ is a unit, $bd=\alpha d$, $D[1/b]\to B[1/b]$ is bijective `Localization.Away` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/GroupTheory/MonoidLocalization/Away.lean)), and $\Phi(\bar d)=(1,0)$. For $e$ the image of $d$ in $B$, $A\to B[1/e]$ is integral and the structure map $A/I\to B[1/e]/IB[1/e]$ is bijective.
