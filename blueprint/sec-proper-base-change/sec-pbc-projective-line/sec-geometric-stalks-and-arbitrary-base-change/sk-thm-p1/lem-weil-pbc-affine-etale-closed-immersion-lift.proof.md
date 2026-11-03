+++
kind = "proof"
of = "lem-weil-pbc-affine-etale-closed-immersion-lift"
uses = ["def-pc-scheme", "lem-exc-etale-algebra-lift"]
+++
Write $X=\operatorname{Spec}R$. A closed immersion into an affine scheme is the spectrum of a quotient map: there are an ideal $I\subseteq R$, an isomorphism $Z\cong\operatorname{Spec}(R/I)$ and a factorization of $i$ through $\operatorname{Spec}(R\to R/I)$. Write $V=\operatorname{Spec}B$; under these identifications $p$ is $\operatorname{Spec}$ of a ring map $R/I\to B$, which is etale since $p$ is ([def-pc-scheme]).

By [lem-exc-etale-algebra-lift] the etale $R/I$-algebra $B$ lifts to an etale $R$-algebra $C$ with an isomorphism $C/IC\cong B$ of $R/I$-algebras. Composing with the canonical isomorphism $C\otimes_R(R/I)\cong C/IC$ gives $C\otimes_R(R/I)\cong B$, compatible with the maps from $C$ and from $R/I$; so the square of rings with sides $R\to C$, $R\to R/I$, $C\to B$, $R/I\to B$ is a pushout. ([lem-exc-etale-algebra-lift]).

The spectrum functor takes this pushout of rings to a pullback of affine schemes. Put $U=\operatorname{Spec}C$, let $q:U\to X$ be induced by $R\to C$ (etale, since $R\to C$ is), and let $a:V\to U$ be induced by $C\to B$. Transporting the pullback square along the identifications of $X$, $Z$ and $V$ with spectra shows that $(a,p,q,i)$ is a fibre product square.
