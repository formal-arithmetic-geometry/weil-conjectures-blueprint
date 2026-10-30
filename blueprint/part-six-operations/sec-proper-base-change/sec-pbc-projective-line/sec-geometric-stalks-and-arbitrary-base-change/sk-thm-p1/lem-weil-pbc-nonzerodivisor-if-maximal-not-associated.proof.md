+++
kind = "proof"
of = "lem-weil-pbc-nonzerodivisor-if-maximal-not-associated"
+++
Let $A=\operatorname{Ass}_R(M)$, the associated primes defined by annihilators as in the statement. It is finite, since $R$ is Noetherian and $M$ is finite. For every $\mathfrak q\in A$, the ideal $\mathfrak q$ is proper, hence $\mathfrak q\subseteq\mathfrak m$ because $R$ is local. By the hypothesis $\mathfrak q\ne\mathfrak m$, so $\mathfrak m\not\subseteq\mathfrak q$.

If $A$ is nonempty, list its distinct members as $\mathfrak q_1,\ldots,\mathfrak q_r$ with $r\ge1$. Step 1 gives $\mathfrak m\not\subseteq\mathfrak q_i$ for each $i$, and each $\mathfrak q_i$ is prime. Prime avoidance, applied to $J=\mathfrak m$ and the $\mathfrak q_i$, yields $x\in\mathfrak m$ outside every member of $A$. If $A$ is empty, take $x=0\in\mathfrak m$, which is also outside every member of $A$.

The chosen $x$ belongs to no associated prime of $M$. Since over a Noetherian ring the zerodivisors on $M$ are exactly the elements of the union of the associated primes of $M$, $x$ is therefore not a zerodivisor on $M$: if $xz=0$, then $z=0$. Thus multiplication by $x$ is injective. This also covers $A=\varnothing$: then the union of associated primes is empty, so even $x=0$ is regular on $M$ (necessarily $M=0$).
