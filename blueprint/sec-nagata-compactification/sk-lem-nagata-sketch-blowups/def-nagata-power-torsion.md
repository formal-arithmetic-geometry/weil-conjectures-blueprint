+++
id = "def-nagata-power-torsion"
kind = "definition"
title = "Power-torsion submodule"
order = 146
lean = ["Submodule.powTorsion"]
+++
Let $R$ be a ring, let $M$ be an $R$-module, and let $a\in R$. Define

$$
\Gamma_{(a)}(M)
=\{m\in M\mid \text{there is }n\geq0\text{ with }a^nm=0\}.
$$

This is an $R$-submodule of $M$, the torsion submodule for the
multiplicative set $\{a^n\}_{n\geq0}$: zero is killed by $a^0$; if
$a^mm_1=0$ and $a^nm_2=0$, then $a^{m+n}(m_1+m_2)=0$; and
$a^m(rm_1)=r(a^mm_1)=0$ for $r\in R$.
