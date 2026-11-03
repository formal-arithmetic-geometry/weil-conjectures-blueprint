+++
kind = "proof"
of = "lem-weil-pbc-pair-henselization-filtered"
+++
*Nonempty.* The identity $B\to B$ is an object: $\operatorname{Spec}$ of the identity is the identity, which is etale, and the canonical map $B/J\to B/JB$ is the identity, hence bijective.

*Common successors.* For objects $C$ and $D$, take $C\otimes_BD$ with its two factor maps $C\to C\otimes_BD\leftarrow D$, which are $B$-algebra maps. $C\otimes_BD$ is etale over $B$: it is the base change of $D$ along $B\to C$, hence etale over $C$, and the composite with the etale map $B\to C$ is etale. For the quotient condition, $(C\otimes_BD)/J(C\otimes_BD)\cong(C/JC)\otimes_{B/J}(D/JD)$; since $B/J\to C/JC$ and $B/J\to D/JD$ are bijective, this is $B/J\otimes_{B/J}B/J=B/J$, and the canonical map $B/J\to(C\otimes_BD)/J(C\otimes_BD)$ is bijective. So $C\otimes_BD$ is an object receiving maps from $C$ and $D$.

*Coequalizers.* Let $f,g:C\to D$ be parallel maps. Put $S=C\otimes_BC$, let $m:S\to C$ be the multiplication, $k:S\to D$ the map $c\otimes c'\mapsto f(c)g(c')$, and $T=D\otimes_SC$ (with $D$ an $S$-algebra via $k$ and $C$ via $m$). Since $S$ and $C$ are etale over $B$, the $B$-algebra map $m$ is etale; its base change $D\to T$ is etale, so $B\to T$ is etale by composition. By the previous step $B/J\to S/JS$ is bijective. Extension of $J$ is compatible with towers $B\to S\to C$ and $B\to S\to D$, so, cancelling the bijection $B/J\to S/JS$, the maps $S/JS\to C/JC$ and $S/JS\to D/JD$ are bijective. The argument of the previous step, applied over $S$ with the ideal $JS$, shows that $S/JS\to T/JT$ is bijective, and composing, $B/J\to T/JT$ is bijective. So $T$ is an object and $D\to T$ is a morphism. Finally, for $c\in C$, in $T$ one has $f(c)\otimes1=k(c\otimes1)\otimes1=1\otimes m(c\otimes1)=1\otimes c$ and likewise $g(c)\otimes1=k(1\otimes c)\otimes1=1\otimes m(1\otimes c)=1\otimes c$. Hence the composites of $f$ and $g$ with $D\to T$ agree, and $D\to T$ coequalizes $f$ and $g$.

These three properties say that the category is filtered.
