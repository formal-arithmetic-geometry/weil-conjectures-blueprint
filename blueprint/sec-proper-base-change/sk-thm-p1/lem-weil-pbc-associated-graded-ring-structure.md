+++
id = "lem-weil-pbc-associated-graded-ring-structure"
kind = "lemma"
title = "The associated graded ring of an ideal is a commutative graded ring and an A/J-algebra"
lean = ["Ideal.associatedGradedMul", "Ideal.associatedGradedCommRing", "Ideal.associatedGraded_mul", "Ideal.associatedGraded_one", "Ideal.associatedGradedAlgebra", "Ideal.algebraMap_associatedGraded_injective", "Ideal.associatedGraded_smul"]
order = 1686
+++
Let $A$ be a commutative ring and $J\subseteq A$ an ideal, with $J^0=A$ and $J^{k+1}=J^kJ$. For $n\ge0$ let $G_n=J^n/J^{n+1}$ be the quotient of the $A$-module $J^n$ by its submodule $J^{n+1}$, and let $G=\bigoplus_{n\ge0}G_n$, with canonical inclusions $\iota_n:G_n\to G$. Then:
(1) for all $n,m\ge0$ there is a unique map $\mu_{n,m}:G_n\times G_m\to G_{n+m}$ with $\mu_{n,m}(a\bmod J^{n+1},\,b\bmod J^{m+1})=ab\bmod J^{n+m+1}$ for all $a\in J^n$, $b\in J^m$; it is biadditive (indeed $A$-bilinear);
(2) the multiplication on $G$ defined by $(\xi\eta)_k=\sum_{n+m=k}\mu_{n,m}(\xi_n,\eta_m)$ for $\xi=(\xi_n)$, $\eta=(\eta_m)$ in $G$, together with the addition of $G$, makes $G$ a commutative ring with unit $\iota_0(1\bmod J)$, and $\iota_n(x)\iota_m(y)=\iota_{n+m}(\mu_{n,m}(x,y))$;
(3) $G_0=J^0/J^1$ is the quotient ring $A/J$ as an abelian group, and $\iota_0:A/J\to G$ is an injective ring homomorphism; thus $G$ is an $A/J$-algebra through $\iota_0$, and for $a\in A$, $n\ge0$ and $x\in J^n$: $\iota_0(a\bmod J)\cdot\iota_n(x\bmod J^{n+1})=\iota_n(ax\bmod J^{n+1})$, so each $\iota_n(G_n)$ is an $A/J$-submodule of $G$.
