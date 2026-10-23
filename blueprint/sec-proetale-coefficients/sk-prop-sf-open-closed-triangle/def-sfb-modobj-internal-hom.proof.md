+++
kind  = "proof"
of    = "def-sfb-modobj-internal-hom"
+++
Since $\mathcal C$ is closed and symmetric, $X\otimes-$ and $-\otimes X$ preserve colimits.
So [def-sfb-modobj-symmetric-tensor] and [lem-sfb-modobj-abelian] apply.

Let $L$ be an $\mathcal R$-module object. An $\mathcal R$-linear map
$L\otimes_{\mathcal R}M\to N$ is a morphism $g\colon L\otimes M\to N$ of $\mathcal C$ with
two properties:
- $g$ is *balanced*: it coequalizes the actions of $\mathcal R$ on $L$ and on $M$;
- $g$ is $\mathcal R$-linear for the action through $L$.

Together these say that
$g$ is linear for the action of $\mathcal R$ through $M$ as well, i.e. that "act on $M$,
then apply $g$" equals "apply $g$, then act on $N$". Let $g^\sharp\colon L\to\underline{\Hom}(M,N)$
be the adjoint of $g$ (using the symmetry to move $M$ to the left). Under the adjunction of
$\mathcal C$, this condition says that $g^\sharp$ equalizes the two maps defining
$\Hom_{\mathcal R}(M,N)$. Linearity through $L$ says that the resulting map
$L\to\Hom_{\mathcal R}(M,N)$ is $\mathcal R$-linear for the action through $N$. On the
equalizer this action agrees with the action through $M$, because $\mathcal R$ is
commutative. So $g\mapsto g^\sharp$ is a bijection between $\mathcal R$-linear maps
$L\otimes_{\mathcal R}M\to N$ and $\mathcal R$-linear maps $L\to\Hom_{\mathcal R}(M,N)$.
It is natural in $L$ and $N$ because the adjunction of $\mathcal C$ is.
