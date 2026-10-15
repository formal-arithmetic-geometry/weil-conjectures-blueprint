+++
id = "lem-sfb-grothendieck-k-injective"
kind = "lemma"
title = "Grothendieck abelian categories have K-injective resolutions"
order = 1608
uses = ["def-weil-abstract-derived-category"]
lean = ["CategoryTheory.Abelian.hasKInjectiveResolutions_of_isGrothendieckAbelian"]
+++
Let $\mathcal C$ be a Grothendieck abelian category. Then every cochain complex $K$ in
$\mathcal C$ admits a monomorphic quasi-isomorphism $K\to I$ into a K-injective complex
$I$. Here K-injective means that $\Hom_{K(\mathcal C)}(A,I)=0$ for every acyclic complex
$A$.
