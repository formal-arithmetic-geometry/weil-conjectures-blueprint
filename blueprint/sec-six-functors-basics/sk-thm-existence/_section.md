+++
id = "sk-thm-existence"
kind = "theorem"
title = "The exceptional inverse image"
order = 2782
uses = ["sk-def-sfb-constructible", "sk-def-localizing-closure", "lem-integral-ctf-equals-bc"]
tags = ["sketch"]
+++
Let $\Lambda\in\{A,\mathbf Z_\ell,\cO_E,\mathbf Q_\ell,E,\Qlb\}$ be an admissible coefficient
ring and $f\colon X\to Y$ a morphism of separated schemes of finite type over $k$.

1. The objects of $\Dctf(X,\Lambda)$ ([sk-def-sfb-constructible]) are compact in
   $\Loc(\Dctf(X,\Lambda))$ ([sk-def-localizing-closure]) and a small skeleton compactly
   generates it.
2. Compactifications define an exact functor
   $Rf_!\colon\Loc(\Dctf(X,\Lambda))\to\Loc(\Dctf(Y,\Lambda))$, preserving direct sums and
   sending $\Dctf(X,\Lambda)$ into $\Dctf(Y,\Lambda)$.
3. The functor $Rf_!$ has an exact right adjoint
   $f^!\colon\Loc(\Dctf(Y,\Lambda))\to\Loc(\Dctf(X,\Lambda))$, obtained from Brown
   representability.
4. This right adjoint sends $\Dctf(Y,\Lambda)$ into $\Dctf(X,\Lambda)$, so its adjunction
   restricts to $\Dctf$.

By [lem-integral-ctf-equals-bc], the theorem holds with $\Dbc$ in place of $\Dctf$ for
$\Lambda=\mathbf Z_\ell,\cO_E,\mathbf Q_\ell,E,\Qlb$.

For proper $p$ we may use the trivial compactification, so that $Rp_!=Rp_*$, and by part (4)
the functor $Rp_*\colon\Dctf(X,\Lambda)\to\Dctf(Y,\Lambda)$ has the right adjoint $p^!$
([det-cor-existence-ii]).
