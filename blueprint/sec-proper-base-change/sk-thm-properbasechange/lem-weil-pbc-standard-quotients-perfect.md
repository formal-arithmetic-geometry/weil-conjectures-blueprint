+++
id = "lem-weil-pbc-standard-quotients-perfect"
kind = "lemma"
title = "Perfectness of the standard quotients"
order = 1254
uses = ["def-weil-pbc-adic-coefficient-datum"]
+++
For $A=\Zl$ and $I=(\ell)$, the quotient $P_n=\mathbf Z/\ell^n\mathbf Z$ is
perfect over $\Zl$, represented by

$$
 [\Zl\xrightarrow{\ell^n}\Zl]
$$

in degrees $-1$ and $0$, in the sense of
[def-weil-pbc-adic-coefficient-datum]. The analogous two-term resolution
holds for $\mathcal O_E/\varpi^n$ over the ring of integers $\mathcal O_E$ of
a finite extension $E/\Ql$.

## Proof

A uniformizer is a non-zero-divisor in a complete discrete valuation ring, so
the displayed two-term complex is a finite free resolution of the quotient,
which is therefore perfect as required by
[def-weil-pbc-adic-coefficient-datum].
