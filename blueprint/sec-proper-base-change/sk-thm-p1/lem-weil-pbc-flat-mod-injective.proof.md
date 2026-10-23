+++
kind = "proof"
of = "lem-weil-pbc-flat-mod-injective"
+++
*Step 1.* For an $R$-module $X$ killed by $\mathfrak m$, $N\otimes_RX=(N/\mathfrak mN)\otimes_{R/\mathfrak m}X$ and similarly for $M$; since $\bar u$ is an injective map of vector spaces over the field $R/\mathfrak m$, $u\otimes X$ is injective.

*Step 2.* By induction on $n$, $u\otimes X$ is injective for every $X$ killed by $\mathfrak m^n$: use the exact sequence $0\to\mathfrak mX\to X\to X/\mathfrak mX\to0$, right exactness of $N\otimes_R-$, exactness of $M\otimes_R-$ (flatness), injectivity on $\mathfrak mX$ (induction) and on $X/\mathfrak mX$ (Step 1), and a diagram chase.

*Step 3.* Let $X$ be a finite $R$-module and $\xi\in\ker(u\otimes X)$. By Step 2 applied to $X/\mathfrak m^nX$, $\xi$ maps to zero in $N\otimes_RX/\mathfrak m^nX$, i.e. $\xi\in\mathfrak m^n(N\otimes_RX)$ for all $n$. The module $N\otimes_RX$ is finite over the Noetherian local ring $S$ and $\mathfrak mS\subseteq\mathfrak m_S$, so by Krull's intersection theorem $\xi=0$.

*Step 4.* Taking $X=R/J$ for ideals $J$ shows: $u(x)\in JM$ implies $x\in JN$; for $J=0$ this is injectivity of $u$.

*Step 5.* Flatness of $C=M/u(N)$ by the ideal criterion: let $z\in C\otimes_RJ$ map to $0$ in $C$. Lift $z$ to $y\in M\otimes_RJ$; its image in $M$ is $u(x)$ for some $x\in N$, and lies in $JM$, so $x\in JN$ by Step 4; lift $x$ to $y'\in N\otimes_RJ$. Since $M$ is flat, $M\otimes_RJ\to M$ is injective, so $y=(u\otimes J)(y')$, which maps to zero in $C\otimes_RJ$. Hence $z=0$.
