+++
id = "prose-09-23"
kind = "hidden"
title = "Integral coefficients (3)"
order = 778
+++
All operations on towers are defined levelwise, and the functor $Rg_*$ is
computed levelwise as well, since an injective tower is levelwise a summand
of finite products of injective sheaves. So proper base change and the
projection formula hold for towers.

Moreover $Rf_{!,\bullet}$ preserves constructible towers. Each level lies
in $D^b_{\mathrm{ctf}}$ by Proposition [proposition-six-operations-dctf], so we only
check that the bounds are independent of $n$. For cohomology, note that for a compactification
$f=pj$, $Rf_!$ has amplitude $[0,\operatorname{cd}_\ell(p)]$ for every
torsion coefficient ring [Stacks, [0F10](https://stacks.math.columbia.edu/tag/0F10)]. For Tor amplitude we use the
projection formula
$(Rf_!C_n)\otimes^{\mathbf L}N\simeq Rf_!(C_n\otimes^{\mathbf L}N)$ for every
$\mathcal O_E/\ell^n$-module $N$, which follows from the comparison $b$ and
shows that if all $C_n$ have Tor amplitude in $[a,b]$, then all $Rf_!C_n$
have Tor amplitude in $[a,b+\operatorname{cd}_\ell(p)]$.

We do not use Brown representability for towers. Instead we construct the
right adjoint of $Rf_{!,\bullet}$ on constructible towers by repeating the geometric argument with finite coefficients in the category
of towers.
