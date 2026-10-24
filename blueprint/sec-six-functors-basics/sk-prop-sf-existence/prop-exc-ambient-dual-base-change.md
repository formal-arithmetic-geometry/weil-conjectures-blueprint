+++
id = "prop-exc-ambient-dual-base-change"
kind = "theorem"
title = "Dual base change for the ambient right adjoint is formal"
order = 2330
tags = ["latex:proposition"]
uses = ["def-cbc-exchange-map", "def-sf-fullcd-used-class", "def-weil-ambient-exceptional-adjoint", "def-weil-pbc-derived-categories", "lem-weil-pbc-comparison-pullback", "prop-weil-pbc-comparison-direct-image", "thm-sf-ambient-adjoint-class"]
+++
Let

$$
\begin{array}{ccc}
X'&\xrightarrow{\ g'\ }&X\\
f'\downarrow&&\downarrow f\\
Y'&\xrightarrow{\ g\ }&Y
\end{array}
$$

be Cartesian with $f,f'$ separated finite type carrying the ambient
exceptional right adjoint datum of
[def-weil-ambient-exceptional-adjoint], and let $g$ be arbitrary.
Then the right-adjoint mate of the compact-support base-change
isomorphism of [def-cbc-exchange-map],

$$
\beta^{\vee}:\ Rf^{\times}Rg_*\xrightarrow{\ \sim\ }Rg'_*Rf'^{\times},
$$

is an isomorphism. On the blueprint's coefficient class
[def-sf-fullcd-used-class], for a Cartesian square of finite-type schemes
over $k=\overline{\mathbf F}_q$ and $A=A_{E,n}$, the ambient datum is not
needed: there $Rf^{\times}$ and $Rf'^{\times}$ are the right adjoints
relative to the bounded-below objects of étale origin of
[thm-sf-ambient-adjoint-class], and $\beta^{\vee}_L$ is an isomorphism for
every bounded-below $L$ on $Y'$ without hypothesis. The unrestricted
ambient datum is false in general and is retained only for the complexes
outside that class, [rem-sf-class-adjoint-residue].
