+++
id = "lem-weil-pbc-injective-acyclicity-bounded-below"
kind = "lemma"
title = "Injective acyclicity gives bounded-below base change (Lean split, general coefficients)"
uses = ["def-weil-proper-morphism", "def-weil-pbc-cartesian-square", "def-weil-pbc-derived-categories", "def-weil-pbc-torsion-etale-sheaf", "def-weil-pbc-direct-image", "def-weil-pbc-inverse-image", "def-weil-pbc-derived-exchange"]
tags = ["sheaf-dag", "stacks-0A4B"]
+++
Let $\Lambda$ be a commutative ring and $f:X\to Y$ a proper morphism of schemes [def-weil-proper-morphism]. Call a sheaf $F$ of $\Lambda_X$-modules on $X_{\Et}$ [def-weil-pbc-derived-categories] *torsion* if its underlying abelian sheaf is torsion [def-weil-pbc-torsion-etale-sheaf] (equivalently, every geometric stalk is a torsion abelian group). Assume that for every morphism $g:Y'\to Y$, every cartesian square [def-weil-pbc-cartesian-square]

$$
 \begin{array}{ccc}
 X'&\xrightarrow{g'}&X\\
 f'\downarrow&&\downarrow f\\
 Y'&\xrightarrow{g}&Y
 \end{array}
$$

and every injective object $I$ of $\Mod(X_{\Et},\Lambda)$ which is torsion, the higher direct images [def-weil-pbc-direct-image] of the inverse image [def-weil-pbc-inverse-image] vanish:

$$
 R^qf'_*\,g'^{-1}I=0\qquad(q>0),
$$

$R^qf'_*$ being the $q$-th cohomology sheaf of $Rf'_*$ applied to $g'^{-1}I$ placed in degree $0$. Then for every such cartesian square and every $K\in\Dplus(X_{\Et},\Lambda)$ all of whose cohomology sheaves $\mathcal H^n(K)$ are torsion, the derived exchange morphism [def-weil-pbc-derived-exchange]

$$
 \Ex_{\square,K}:g^{-1}Rf_*K\longrightarrow Rf'_*g'^{-1}K
$$

is an isomorphism in $\Dplus(Y'_{\Et},\Lambda)$. No hypothesis is put on $g$.
