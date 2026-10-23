+++
kind = "proof"
of = "lem-weil-pbc-flat-module-powers"
+++
Let $J\subseteq R$ be an ideal and $x\in M\otimes_RJ$ with image $0$ in $M$.

*Step 1.* For $k\ge1$, flatness of $M/I^kM$ over $R/I^k$ makes $M\otimes_R\bar J\to M\otimes_RR/I^k$ injective, where $\bar J$ is the image of $J$ in $R/I^k$; the image of $x$ there is zero. By right exactness for $J\cap I^k\to J\to\bar J\to0$, $x$ lies in the image of $M\otimes_R(J\cap I^k)$.

*Step 2.* By Artin–Rees there is $c$ with $J\cap I^{n+c}\subseteq I^nJ$ for all $n$. Hence $x\in I^n(M\otimes_RJ)$ for all $n\ge0$.

*Step 3.* $J$ is finite over the Noetherian ring $R$, so $M\otimes_RJ$ is a finite module over the Noetherian ring $S$, and $x\in(IS)^n(M\otimes_RJ)$ for all $n$. By the Krull intersection theorem there is $r\in IS$ with $(1-r)x=0$. If $IS\subseteq\mathfrak q$, then $1-r\notin\mathfrak q$.

*Step 4.* Localizing at $\mathfrak q$ commutes with $-\otimes_RJ$. An element of $M_{\mathfrak q}\otimes_RJ$ mapping to $0$ in $M_{\mathfrak q}$ comes, up to a unit, from some $x\in M\otimes_RJ$ whose image in $M$ is killed by some $s\notin\mathfrak q$; applying Steps 1–3 to $sx$ gives an element $1-r\notin\mathfrak q$ killing $sx$, so the localized element is zero. By the ideal criterion $M_{\mathfrak q}$ is flat over $R$.

*Step 5.* If $S$ is local and $IS\subseteq\mathfrak m_S$, take $\mathfrak q=\mathfrak m_S$; then $M_{\mathfrak q}=M$.
