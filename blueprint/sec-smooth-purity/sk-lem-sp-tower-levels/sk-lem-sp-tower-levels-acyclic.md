+++
id = "det-sp-tower-injective-components"
kind = "lemma"
title = "Components of injective towers are acyclic"
uses = ["det-sp-tower-evaluation-adjoint"]
+++
Let $I_\bullet$ be an injective object of $\operatorname{Tow}(T,\mathcal O_E)$. Then for
every $r$, the component $I_r$ is a direct summand of a finite product of
sheaves $J_n$ ($n\leq r$), each an injective $\mathcal O_{E,T}/\ell^n$-module
viewed as an $\mathcal O_{E,T}/\ell^r$-module. In particular $I_r$ is acyclic
for sections over every object of $T_{\mathrm{proét}}$, hence $g_*$-acyclic for
every morphism $g:T\to S$. Consequently, for
$C_\bullet\in D^+(\operatorname{Tow}(T,\mathcal O_E))$ with a bounded below injective
resolution $C_\bullet\to I_\bullet^\cdot$, the complex $I_n^\cdot$ computes
$Rg_{*,\mathcal O_E/\ell^n}C_n$, and so
$(Rg_{*,\bullet}C_\bullet)_n\simeq Rg_{*,\mathcal O_E/\ell^n}C_n$.
