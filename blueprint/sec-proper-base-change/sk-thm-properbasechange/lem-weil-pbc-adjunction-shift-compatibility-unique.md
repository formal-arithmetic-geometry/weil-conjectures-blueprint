+++
id = "lem-weil-pbc-adjunction-shift-compatibility-unique"
kind = "lemma"
title = "Shift isomorphisms compatible with an adjunction: counit from unit, and uniqueness on the right adjoint"
uses = ["def-weil-pbc-triangles-with-shift", "lem-weil-pbc-commshift-nattrans-comp-whisker"]
lean = ["CategoryTheory.Adjunction.CommShift.compatibilityCounit_of_compatibilityUnit"]
tags = ["mathlib", "stacks-0A8D"]
+++
Let $\mathcal C,\mathcal D$ be categories with shift functors $[a ]$, $a\in\mathbf Z$ [def-weil-pbc-triangles-with-shift], let $F:\mathcal C\to\mathcal D$ be left adjoint to $G:\mathcal D\to\mathcal C$ with unit $\eta:\mathrm{id}\to GF$ and counit $\varepsilon:FG\to\mathrm{id}$, and fix $a\in\mathbf Z$. For natural isomorphisms $e_{1,X}:F(X[a ])\xrightarrow{\sim}F(X)[a ]$ ($X\in\mathcal C$) and $e_{2,Y}:G(Y[a ])\xrightarrow{\sim}G(Y)[a ]$ ($Y\in\mathcal D$) say that $(e_1,e_2)$ is *compatible with the unit* if $\eta_X[a ]=e_{2,FX}\circ G(e_{1,X})\circ\eta_{X[a ]}$ for all $X$, and *compatible with the counit* if $\varepsilon_{Y[a ]}=\varepsilon_Y[a ]\circ e_{1,GY}\circ F(e_{2,Y})$ for all $Y$. Then: (i) compatibility with the unit implies compatibility with the counit; (ii) for given $e_1$ there is at most one $e_2$ such that $(e_1,e_2)$ is compatible with the unit, namely $e_{2,Y}^{-1}=G(\varepsilon_Y[a ])\circ G(e_{1,GY})\circ\eta_{G(Y)[a ]}$; (iii) if $(F,e_1)$ is a functor commuting with the shift (isomorphisms $e_1^{(a)}$ for all $a$, compatible with $[a ][b ]\cong[a+b ]$ and $[0 ]\cong\mathrm{id}$ [lem-weil-pbc-commshift-nattrans-comp-whisker]), then $G$ carries a structure $(G,e_2)$ of functor commuting with the shift such that $(e_1^{(a)},e_2^{(a)})$ is compatible with the unit and with the counit for every $a$; by (ii) it is the only such structure.
