+++
kind  = "proof"
of    = "lemma-weil-pbc-prime-factor-induction"
uses = ["lem-weil-pbc-prime-factor-devissage", "lemma-weil-pbc-five-lemma-transfer"]
+++
Let $P(E)$ be the property that $\Ex^q_{\square,E}$ is an isomorphism for every
$q$. By the five-lemma transfer [lemma-weil-pbc-five-lemma-transfer], $P$ is
stable under extensions: if $0\to F_1\to F\to F_2\to0$ is exact and $P$ holds
for $F_1$ and $F_2$, it holds for $F$. By hypothesis $P$ holds for every sheaf
killed by a prime. The prime-factor devissage
[lem-weil-pbc-prime-factor-devissage] in the abelian category of sheaves of
$\Lambda$-modules on $X_{\Et}$ then gives $P(F)$ for every $F$ killed by a
positive integer $n$. Explicitly, one inducts on the number of prime factors of
$n$: for $n=1$ the sheaf $F=0$ is killed by any prime, and otherwise, for a
prime $\ell\mid n$, the sequence $0\to F[\ell]\to F\xrightarrow{\ell}\ell F\to0$
has kernel killed by $\ell$ and image killed by $n/\ell$, so $P$ holds for both
ends and hence for $F$.
