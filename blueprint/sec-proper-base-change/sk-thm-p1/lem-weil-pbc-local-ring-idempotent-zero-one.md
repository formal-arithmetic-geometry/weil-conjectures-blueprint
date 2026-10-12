+++
id = "lem-weil-pbc-local-ring-idempotent-zero-one"
kind = "lemma"
title = "An idempotent of a local ring is 0 or 1"
lean = ["IsLocalRing.eq_zero_or_eq_one_of_isIdempotentElem"]
source = "literature/stacks-project/algebra.tex, Algebra, Lemma Tag 00E9 (lemma-characterize-local-ring), (1)⇒(4): a local ring is not the zero ring and for every x one of x, 1-x is a unit; the idempotent statement itself is not stated in Stacks: e(1-e)=0 and one of e, 1-e is a unit, so the other is 0"
+++
Let $R$ be a local ring (a commutative ring with exactly one maximal ideal $\mathfrak m$; in particular $0\neq1$ in $R$) and $e\in R$ an idempotent, $e^2=e$. Then $e=0$ or $e=1$. Consequently, for an idempotent $e$ of $R$ the conditions $e\neq0$, $e=1$ and $e\notin\mathfrak m$ ($e$ a unit) are equivalent.
