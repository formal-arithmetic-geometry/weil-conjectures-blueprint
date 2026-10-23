+++
id = "det-sp-tower-evaluation-adjoint"
kind = "lemma"
title = "Evaluation of towers has an exact right adjoint"
order = 3013
uses = ["det-sp-coefficient-towers-abelian"]
+++
For $n\geq1$ and an $\mathcal O_{E,T}/\ell^n$-module sheaf $J$ on $T_{\mathrm{proét}}$,
let $r_nJ\in\operatorname{Tow}(T,\mathcal O_E)$ be the tower with $(r_nJ)_r=J$ for
$r\geq n$ (an $\mathcal O_{E,T}/\ell^r$-module by restriction of scalars along
$\mathcal O_{E,T}/\ell^r\to\mathcal O_{E,T}/\ell^n$), $(r_nJ)_r=0$ for $r<n$,
identity transitions $(r_nJ)_{r+1}\to(r_nJ)_r$ for $r\geq n$ and zero
transitions below. Then $r_n$ is an exact functor, right adjoint to evaluation
$C_\bullet\mapsto C_n$. Consequently $r_n$ preserves injective objects, and
every tower $C_\bullet$ embeds into $\prod_{n\geq1}r_nJ_n$ for injective
$\mathcal O_{E,T}/\ell^n$-modules $J_n\supset C_n$.
