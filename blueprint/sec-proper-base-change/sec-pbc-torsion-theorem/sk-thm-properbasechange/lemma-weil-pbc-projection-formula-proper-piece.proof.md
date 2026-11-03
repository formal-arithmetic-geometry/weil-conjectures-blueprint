+++
kind  = "proof"
of    = "lemma-weil-pbc-projection-formula-proper-piece"
+++
Let $F^\vee$ be a dual of $F$. The functor $Lp^*$ is monoidal, so
$Lp^*F$ is dualizable with dual $Lp^*F^\vee$. For every object $T$ on $Y$ we
get bijections, natural in $T$,

$$
\begin{aligned}
\operatorname{Hom}(T,(Rp_*M)\otimes^LF)
&\cong\operatorname{Hom}(T\otimes^LF^\vee,Rp_*M)
\cong\operatorname{Hom}(Lp^*T\otimes^LLp^*F^\vee,M)\\
&\cong\operatorname{Hom}(Lp^*T,M\otimes^LLp^*F)
\cong\operatorname{Hom}(T,Rp_*(M\otimes^LLp^*F)),
\end{aligned}
$$

using duality for $F$, the adjunction $Lp^*\dashv Rp_*$ with the monoidal
structure of $Lp^*$, duality for $Lp^*F$, and the adjunction again. Unwinding
the units, counits and evaluation maps, the composite bijection is
composition with $\pi_{p,M,F}$. By the Yoneda lemma $\pi_{p,M,F}$ is an
isomorphism.
