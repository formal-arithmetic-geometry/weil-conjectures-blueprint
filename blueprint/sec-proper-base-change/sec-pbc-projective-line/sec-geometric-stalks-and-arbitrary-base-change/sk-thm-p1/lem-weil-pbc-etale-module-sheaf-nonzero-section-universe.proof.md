+++
kind = "proof"
of = "lem-weil-pbc-etale-module-sheaf-nonzero-section-universe"
+++
Let $A$ be any type in universe $u$. Form the disjoint union $V=\coprod_{a\in A}U$ of copies of $U$ indexed by $A$, a scheme in universe $u$. Its structure map to $X$ is etale, being etale on each summand (etaleness is local on the source), and the summand inclusions form an etale covering of $V$ whose images are pairwise disjoint.

Put $E=F(U)$. For each $a\in A$ prescribe, on the summand indexed by $b\in A$, the $\Lambda$-linear map $E\to F(U)$ which is the identity if $b=a$ and zero if $b\ne a$. This family is compatible for the covering: the fibre product of a summand with itself is that summand, as summand inclusions are monomorphisms, and the fibre product of two distinct summands is empty, while $F(\emptyset)=0$ by the sheaf condition for the empty covering. The sheaf condition for $F$ therefore gives a $\Lambda$-linear map $t(a):E\to F(V)$ whose restriction to the summand $b$ is the prescribed map.

If $t(a)=t(b)$ with $a\ne b$, restricting to the summand $a$ gives $\mathrm{id}_E=0$, and evaluating at $s$ contradicts $s\ne0$. Thus $a\mapsto t(a)$ is an injection of $A$ into the set of $\Lambda$-linear maps $E\to F(V)$, a type in universe $\max(v,w)$, so $A$ is in bijection with a type in universe $\max(v,w)$. Since $A$ was arbitrary, universe $u$ is no larger than universe $\max(v,w)$. Empty $A$ causes no problem, and the existence of $s\ne0$ excludes $U=\emptyset$ and $\Lambda=0$.
