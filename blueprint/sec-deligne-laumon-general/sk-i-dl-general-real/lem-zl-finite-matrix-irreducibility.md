+++
id = "lem-zl-finite-matrix-irreducibility"
kind = "lemma"
title = "Absolute irreducibility has a finite matrix witness"
order = 3135
lean = ["Representation.exists_forall_isIrreducible_baseChange_of_congr"]
uses = ["lem-wf-schur-scalar", "p-real-integral"]
+++
Let $\mathcal O$ be a Noetherian local domain with maximal ideal
$\mathfrak m$ and fraction field $E$, and let $K\supseteq E$ be an
algebraically closed field. Let $\rho:\Pi\to\operatorname{GL}_E(V)$ be a
representation of a group $\Pi$ on an $n$-dimensional $E$-vector space
$V$, and let $b$ be a basis of $V$ in which every matrix $\rho(g)$ has
entries in $\mathcal O$. Assume that $V\otimes_E K$ is irreducible.
Then there is $N\geq1$ with the following property: if a subgroup
$\Pi'\subseteq\Pi$ contains, for every $g\in\Pi$, an element $h$ whose
matrix in $b$ is congruent to that of $g$ modulo $\mathfrak m^N$, then
$\Pi'$ acts absolutely irreducibly on $V$, i.e. $V\otimes_E K'$ is
irreducible under $\Pi'$ for every field $K'\supseteq E$.
