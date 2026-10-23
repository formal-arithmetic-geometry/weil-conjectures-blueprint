+++
id = "lem-integral-ctf-equals-bc"
kind = "lemma"
title = "$\\Dctf=\\Dbc$ for integral and rational coefficients"
order = 1245
uses = ["def-weil-finite-tor-amplitude", "det-def-sfb-bounded-constructible", "def-sfb-constructible-module"]
+++
Let $X$ be a qcqs scheme and $\Lambda\in\{\cO_E,E,\Qlb\}$, regarded as a condensed ring, with $E/\mathbf Q_\ell$
finite (so $\Lambda=\mathbf Z_\ell,\mathbf Q_\ell$ are included). Then:

1. every constructible $\Lambda_X$-module ([def-sfb-constructible-module]) has Tor amplitude in $[-1,0]$
   ([def-weil-finite-tor-amplitude]), and in $[0,0]$ if $\Lambda$ is a field;
2. every $K\in\Dbc(X,\Lambda)$ ([det-def-sfb-bounded-constructible]) with cohomology in $[a,b]$ has Tor
   amplitude in $[a-1,b]$, and in $[a,b]$ if $\Lambda=E$ or $\Qlb$: for every sheaf $M$ of
   $\Lambda_X$-modules placed in degree zero,
   $$
   \mathcal H^r\bigl(K\otimes^{\mathbf L}_{\Lambda_X}M\bigr)=0\qquad(r\in\mathbf Z\setminus[a-1,b],
   \text{ resp. } r\notin[a,b]).
   $$
   Hence
   $$
   \Dctf(X,\Lambda)=\Dbc(X,\Lambda).
   $$

For a finite nonregular ring the condition is needed: $\mathbf F_\ell$ over $\mathbf Z/\ell^2$ is
constructible but has infinite projective dimension. Finite Tor amplitude is a condition on the whole
complex: for $A=\mathbf Z/\ell^2$ the complex $[A\xrightarrow{\ell}A]$ is perfect, whereas its nonzero
cohomology modules are $\mathbf F_\ell$, which are not perfect; so $\Dctf(X,A)$ is thick but need not be
stable under standard truncations.
