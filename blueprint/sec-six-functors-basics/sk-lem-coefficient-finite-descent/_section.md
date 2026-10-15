+++
id = "sk-lem-coefficient-finite-descent"
kind = "lemma"
title = "Descent to a finite coefficient field"
order = 1517
uses = ["sk-prop-sfb-qlbar-colimit-x", "sk-lem-coefficient-heart", "sk-lem-constructible-ext-continuity", "sk-prop-sfb-finite-extension-compatibility"]
tags = ["sketch"]
+++
The coefficient ring $\Qlb$ is a filtered union of the fields $E$, but integral lattices exist
only over a single $E$. We therefore show that every object and every morphism of
$\Dbc(X,\Qlb)$ is defined over some finite $E$. For $C\in D(X_{\mathrm{proét}},E)$ and a finite
extension $F/E$ we write $C_F=F_X\otimes_{E_X}C$ and $C_{\Qlb}=\QbarX\otimes_{E_X}C$ for the
extensions of scalars, given by functors $D(X_{\mathrm{proét}},E)\to D(X_{\mathrm{proét}},F)$ and
$D(X_{\mathrm{proét}},E)\to D(X_{\mathrm{proét}},\Qlb)$; since $F_X$ and $\QbarX$ are flat over
$E_X$ ([sk-prop-sfb-finite-extension-compatibility]), these need no deriving.

Let $X$ be a standing scheme.

1. Every lisse $\QbarX$-module is isomorphic to $L_{\Qlb}$ for a lisse $E_X$-module $L$ and
   some finite $E/\mathbf Q_\ell$.
2. For $C,D\in\Dbc(X,E)$ and every integer $r$, extension of scalars induces an isomorphism
   $$
   \varinjlim_{F\supset E}\Hom_{D(X_{\mathrm{proét}},F)}(C_F,D_F[r])\xrightarrow{\ \sim\ }
   \Hom_{D(X_{\mathrm{proét}},\Qlb)}(C_{\Qlb},D_{\Qlb}[r]),
   $$
   the colimit running over finite extensions $F$ of $E$ in $\Qlb$.
3. Every object of $\Dbc(X,\Qlb)$ is isomorphic to $K_{\Qlb}$ for some $K\in\Dbc(X,E)$ and
   some finite $E/\mathbf Q_\ell$.

Parts (2) and (3) are the content of the $2$-colimit description of [sk-thm-sfb-qlbar-two-colimit].
