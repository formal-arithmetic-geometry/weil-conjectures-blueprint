+++
id = "thm-sf-dual-base-change"
kind = "theorem"
title = "Dual base change"
order = 2578
uses = ["def-exchange-projection", "def-sf-datum", "fix-prop-adjunctions", "lem-sf-mate", "lemma-weil-pbc-prime-proper-base-change", "sbc-thm-smooth-base-change", "sk-prop-sf-cbc", "sk-thm-sfb-shriek-base-change", "sk-thm-sfb-proper-base-change", "thm-cbc-finite-level-proetale", "thm-cbc-finite-torsion", "thm-weil-pbc-bounded-below", "thm-weil-pbc-finite-level-proetale"]
+++
In the setting of [def-sf-datum], let

$$
\begin{array}{ccc}
X' & \xrightarrow{g'} & X\\
f'\downarrow && \downarrow f\\
Y' & \xrightarrow{g} & Y
\end{array}
$$

be a Cartesian square of separated finite-type $S$-schemes. Then there is a
canonical isomorphism, natural in the square and compatible with the pasting
of squares,

$$
Rf^!Rg_*\xrightarrow{\ \sim\ }Rg'_*Rf'^!,
$$

the right adjoint of the base-change isomorphism
$\operatorname{Ex}_!:Lg^*Rf_!\cong Rf'_!Lg'^*$. If $g$ is proper, so that
$g'$ is proper as well and $Rg_!=Rg_*$, $Rg'_!=Rg'_*$ by [fix-prop-adjunctions],
the same isomorphism reads

$$
Rf^!Rg_!\xrightarrow{\ \sim\ }Rg'_!Rf'^!.
$$
