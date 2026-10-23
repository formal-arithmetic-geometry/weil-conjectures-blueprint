+++
id = "sk-thm-existence"
kind = "theorem"
title = "The exceptional inverse image"
order = 2136
uses = ["sk-def-sfb-dc-lower-shriek", "sk-def-localizing-closure", "sk-def-sfb-constructible", "sk-def-sfb-dc-setting"]
tags = ["sketch"]
+++
Let $\Lambda\in\{A,\mathbf Z_\ell,\cO_E,\mathbf Q_\ell,E,\Qlb\}$ be an admissible coefficient
ring and $f\colon X\to Y$ a morphism of the standing schemes (separated and of finite type
over the standing field $k$, with $\ell\ne\operatorname{char}k$; [sk-def-sfb-dc-setting]).

1. The objects of $\Dctf(X,\Lambda)$ ([sk-def-sfb-constructible]) are compact in
   $\Loc(\Dctf(X,\Lambda))$ ([sk-def-localizing-closure]) and a small skeleton compactly
   generates it.
2. Compactifications define an exact functor
   $Rf_!\colon\Loc(\Dctf(X,\Lambda))\to\Loc(\Dctf(Y,\Lambda))$, preserving direct sums and
   sending $\Dctf(X,\Lambda)$ into $\Dctf(Y,\Lambda)$ (compare [sk-def-sfb-dc-lower-shriek]).
3. A single application of Brown representability gives an exact right adjoint
   $f^!\colon\Loc(\Dctf(Y,\Lambda))\to\Loc(\Dctf(X,\Lambda))$.
4. This right adjoint sends $\Dctf(Y,\Lambda)$ into $\Dctf(X,\Lambda)$, so its adjunction
   restricts to $\Dctf$.

For $\Lambda=\mathbf Z_\ell,\cO_E,\mathbf Q_\ell,E,\Qlb$ one has $\Dctf=\Dbc$, so the theorem
holds with $\Dbc$ in place of $\Dctf$. The finite ring $A$ is arbitrary; it need not be
regular or Gorenstein. The $\mathbf Z_\ell$ and $\mathbf Q_\ell$ cases are the integral and
rational cases with $E=\mathbf Q_\ell$.
