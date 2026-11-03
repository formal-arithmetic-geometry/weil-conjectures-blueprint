+++
kind  = "proof"
of    = "the-subsheaf-ff-and-its-representability--remark-1"
uses = ["lem-pc-zero-scheme-recd", "lem-pc-zero-scheme-properties"]
+++
*Well defined.* For $\cL\in F(T)$ with $Rf_{T,*}\cL\cong\cN[0]$, the zero
scheme $D=Z(s)$ of the adjoint section is a relative effective Cartier divisor
on $X_T/T$, finite locally free of degree $g$ over $T$ ([lem-pc-zero-scheme-recd]); so
$D\in\Hilb^g_{X/k}(T)$. It does not depend on the choice of $\cN$: another
choice differs by an invertible module on $T$, which multiplies $s$ by a unit
and leaves $Z(s)$ unchanged.

*Natural.* For $h:T'\to T$, cohomology and base change for $\cL\in F(T)$ gives
$Rf_{T',*}(h^*\cL)\cong h^*\cN[0]$, and the adjoint section of $h^*\cL$ is the
pullback of $s$. Zero schemes commute with pullback ([lem-pc-zero-scheme-properties](2)), so
$Z(h^*s)=Z(s)\times_TT'$, which is $\Phi_{T'}(h^*\cL)=h^*\Phi_T(\cL)$.

*Injective.* Since $s$ is a section of $\cL\otimes f_T^*\cN^{-1}$ with zero
scheme $D$, it identifies $\cO(D)\cong\cL\otimes f_T^*\cN^{-1}$. Pulling back
along $\sigma_T$ gives
$\sigma_T^*\cO(D)\cong\sigma_T^*\cL\otimes\cN^{-1}\cong\cN^{-1}$, because $\cL$
is $\sigma$-normalized. Hence
$\cO(D)\otimes\operatorname{pr}_T^*\sigma_T^*\cO(D)^{-1}\cong\cL$, so $\cL$ is
recovered from $D$. That is the stated inverse, and $\Phi_T$ is injective.
