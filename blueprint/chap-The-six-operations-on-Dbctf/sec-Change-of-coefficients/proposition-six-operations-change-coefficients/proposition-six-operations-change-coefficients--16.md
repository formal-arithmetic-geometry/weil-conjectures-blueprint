+++
id = "proposition-six-operations-change-coefficients--16"
kind = "proposition"
title = "Compactly supported direct image: composing reduction comparisons"
order = 645032
aliases = ["bp-r197-16"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.etaleReductionLowerShriekIsoOfComp"]
uses = ["definition-change-of-coefficients-maps", "proposition-composition-base-change-rf-shriek"]
+++
Let $X\xrightarrow{f}Y\xrightarrow{g}S$ be morphisms of separated schemes of finite type over a field of characteristic $p\ne\ell$, let $h=gf$, and fix $E\subset\Qbarl$ finite over $\Qell$ and $n\geq 0$. Write $\mathrm{red}$ for reduction modulo $\ell^n$ followed by the étale reading.

Given natural isomorphisms
$$
\gamma_f:\mathrm{red}_Y Rf_{!,\mathcal O_E}\xrightarrow{\sim}Rf_{!,\mathcal O_E/\ell^n}\mathrm{red}_X,
\qquad
\gamma_g:\mathrm{red}_S Rg_{!,\mathcal O_E}\xrightarrow{\sim}Rg_{!,\mathcal O_E/\ell^n}\mathrm{red}_Y,
$$
there is a composite comparison $\gamma_h$ of the same form for $h$. It is defined by pasting these comparisons and transporting along the composition isomorphisms for $Rf_!$ over $\mathcal O_E$ and on the étale site.
