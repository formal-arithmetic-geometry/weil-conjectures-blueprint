+++
kind = "proof"
of = "lemma-mixedness-descends-constant-extension--1"
order = 1337002
+++
Put $S=\sum_{n=0}^{M-1}T^n(P)$. Periodicity gives $T^n(P)\subseteq S$
for every $n\geq 0$. Since $T$ preserves sums, $T(S)\subseteq S$.
Conversely,
$T^n(P)=T(T^{n+M-1}(P))$ for $0\leq n<M$, so $S\subseteq T(S)$.
Thus $T(S)=S$.

Every translate $T^n(P)$ is lisse, and a finite sum of lisse
subsheaves of the lisse sheaf $\overline F$ is lisse on the locally
Noetherian scheme $X$. The equality $T(S)=S$ equips $S$ with a Weil
structure compatible with its inclusion in $\overline F$
(`AlgebraicGeometry.WeilSheaf.exists_mono_of_frobeniusTwist_eq`).
It therefore underlies a lisse Weil subsheaf of $F$. This subsheaf is
nonzero because it contains $P$, so irreducibility of $F$ makes its
inclusion an isomorphism. Hence $S=\overline F$.
