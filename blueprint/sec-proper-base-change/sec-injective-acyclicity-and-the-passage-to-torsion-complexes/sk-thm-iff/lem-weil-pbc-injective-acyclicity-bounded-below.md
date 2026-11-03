+++
id = "lem-weil-pbc-injective-acyclicity-bounded-below"
kind = "lemma"
title = "Injective acyclicity gives bounded-below base change (torsion coefficient ring)"
lean = ["AlgebraicGeometry.Etale.HasInjectiveAcyclicity.hasTorsionBaseChange", "AlgebraicGeometry.Etale.HasInjectiveAcyclicity.hasTorsionBaseChange_of_isIso_baseChangeMap"]
order = 1673
uses = ["def-weil-proper-morphism", "def-weil-pbc-cartesian-square", "def-weil-pbc-derived-categories", "def-weil-pbc-direct-image", "def-weil-pbc-inverse-image", "def-weil-pbc-derived-exchange"]
tags = ["stacks-0A4B"]
+++
Let $\Lambda$ be a commutative ring which is torsion as an additive group
(equivalently, $N\cdot1=0$ in $\Lambda$ for some integer $N\geq1$, e.g.
$\Lambda=\mathbf Z/\ell^n\mathbf Z$), and let $f:X\to Y$ be a proper morphism of
schemes [def-weil-proper-morphism]. Assume that for every morphism $g:Y'\to Y$,
every cartesian square [def-weil-pbc-cartesian-square]

$$
 \begin{array}{ccc}
 X'&\xrightarrow{g'}&X\\
 f'\downarrow&&\downarrow f\\
 Y'&\xrightarrow{g}&Y
 \end{array}
$$

and every injective object $I$ of $\Mod(X_{\Et},\Lambda)$
[def-weil-pbc-derived-categories], the higher direct images
[def-weil-pbc-direct-image] of the inverse image [def-weil-pbc-inverse-image]
vanish:

$$
 R^qf'_*\,g'^{-1}I=0\qquad(q>0),
$$

$R^qf'_*$ being the $q$-th cohomology sheaf of $Rf'_*$ applied to $g'^{-1}I$
placed in degree $0$. Then for every such cartesian square and every
$K\in\Dplus(X_{\Et},\Lambda)$ the derived exchange morphism
[def-weil-pbc-derived-exchange]

$$
 \Ex_{\square,K}:g^{-1}Rf_*K\longrightarrow Rf'_*g'^{-1}K
$$

is an isomorphism in $\Dplus(Y'_{\Et},\Lambda)$. No hypothesis is put on $g$.
(Since $\Lambda$ is torsion, every sheaf of $\Lambda$-modules is torsion, so
these are the injective acyclicity and base change properties for torsion
coefficients.)
