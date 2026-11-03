+++
kind  = "proof"
of    = "lem-sfb-extend-subfield-constructible"
uses = ["lem-sfb-subfield-flat", "sk-def-sfb-constructible"]
+++
The extension of scalars $F_X\otimes_{E_X}-$ is exact ([lem-sfb-subfield-flat]), so $T_{E,F}$
is computed termwise and $H^n(T_{E,F}K)=F_X\otimes_{E_X}H^n(K)$; in particular $T_{E,F}K$ is
bounded. A constructible module ([sk-def-sfb-constructible]) is, on the strata of a finite
stratification, locally finitely presented; tensoring a local finite presentation
$E_X^m\to E_X^n\to M\to0$ with $F_X$ gives a local finite presentation of $F_X\otimes_{E_X}M$
(right exactness), on the same stratification. So the cohomology sheaves of $T_{E,F}K$ are
constructible.
