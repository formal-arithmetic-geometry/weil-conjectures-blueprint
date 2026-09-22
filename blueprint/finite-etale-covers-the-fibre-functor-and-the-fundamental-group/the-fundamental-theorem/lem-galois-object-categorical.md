+++
id = "lem-galois-object-categorical"
kind = "lemma"
title = "Galois covers are the connected Galois objects"
order = 3029
lean = ["AlgebraicGeometry.FiniteEtale.isGaloisCover_iff_isGalois"]
uses = ["def-galois-object", "def-galois-category", "def-galois-fibre-functor", "lem-galois-axioms", "lem-fet-galois-category"]
+++
Let $Y$ be connected with a geometric point $\bar y$. Then a finite etale
cover $P\to Y$ is a Galois cover [def-galois-object] if and only if $P$ is
connected and is a Galois object, in the sense of [lem-galois-axioms](6),
of the Galois category $\mathrm{F\acute Et}(Y)$.

## Proof

By [lem-fet-galois-category] the pair $(\mathrm{F\acute Et}(Y),F_{\bar y})$
is a Galois category in the sense of [def-galois-category], with
$F_{\bar y}(P)=P_{\bar y}$ by [def-galois-fibre-functor]. By
[lem-galois-axioms](6) a connected object $P$ of $\mathrm{F\acute Et}(Y)$
is Galois exactly when $\operatorname{Aut}_Y(P)$ acts transitively on
$P_{\bar y}$, and again by [lem-galois-axioms](6) the stabilizer of a point
of $P_{\bar y}$ is trivial, so this is the simple transitivity required in
[def-galois-object].
