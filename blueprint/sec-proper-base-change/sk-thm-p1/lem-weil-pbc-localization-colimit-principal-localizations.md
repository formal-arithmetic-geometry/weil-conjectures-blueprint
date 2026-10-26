+++
id = "lem-weil-pbc-localization-colimit-principal-localizations"
kind = "lemma"
title = "A localization is the filtered colimit of the principal localizations"
lean = ["CommRingCat.localization_colimit_principalLocalizations"]
order = 1864
+++
Let $P$ be a commutative ring and $S\subseteq P$ a multiplicative subset. For $f\in S$ let $P_f$ be the localization of $P$ at $\{1,f,f^2,\dots\}$ and $S^{-1}P$ the localization at $S$ (fractions $a/s$, $a/s=a'/s'$ iff $u(as'-a's)=0$ for some $u\in S$). Preorder $S$ by $f\le g$ iff $g=fh$ for some $h\in P$. Then: (1) this preorder is directed ($f,f'\le ff'$), so, regarded as a category, it is filtered; (2) for $f\le g$, $g=fh$, the map $\rho_{fg}:P_f\to P_g$, $a/f^e\mapsto ah^e/g^e$, is a well defined ring homomorphism, independent of the choice of $h$, with $\rho_{ff}=\mathrm{id}$ and $\rho_{gk}\circ\rho_{fg}=\rho_{fk}$, so $f\mapsto P_f$ is a functor from $S$ to commutative rings; (3) the ring maps $\kappa_f:P_f\to S^{-1}P$, $a/f^e\mapsto a/f^e$, satisfy $\kappa_g\circ\rho_{fg}=\kappa_f$ and make $S^{-1}P$ a colimit of this functor in the category of commutative rings: $S^{-1}P=\varinjlim_{f\in S}P_f$. Moreover $\kappa_f$ composed with $P\to P_f$ is the localization map $P\to S^{-1}P$.
