+++
id = "det-def-localizing-closure-ctf-equals-bc"
kind = "lemma"
title = "$D^b_{ctf}=D^b_c$ for integral and rational coefficients"
uses = ["det-def-sfb-constructible-local-model", "det-def-sfb-constructible-tor-amplitude", "det-prop-integral-criterion-constant-coefficients", "det-def-localizing-closure-existence"]
+++
Let $X$ be a qcqs scheme and $\Lambda\in\{\mathbf Z_\ell,\cO_E,\mathbf Q_\ell,E,\Qlb\}$. Then:

1. every constructible $\Lambda_X$-module has Tor amplitude in $[-1,0]$, and in $[0,0]$ if
   $\Lambda$ is a field;
2. every $K\in\Dbc(X,\Lambda)$ with cohomology in $[a,b]$ has Tor amplitude in $[a-1,b]$;
   hence $\Dctf(X,\Lambda)=\Dbc(X,\Lambda)$ and
   $\Loc(\Dctf(X,\Lambda))=\Loc(\Dbc(X,\Lambda))$.

For a finite nonregular ring the condition is essential: $\mathbf F_\ell$ over
$\mathbf Z/\ell^2$ is constructible but has infinite projective dimension. Finite Tor
amplitude is a condition on the whole complex: for $A=\mathbf Z/\ell^2$ the complex
$[A\xrightarrow{\ell}A]$ is perfect, whereas its nonzero cohomology modules are
$\mathbf F_\ell$, which are not perfect; so $\Dctf(X,A)$ is thick but need not be stable
under standard truncations.
