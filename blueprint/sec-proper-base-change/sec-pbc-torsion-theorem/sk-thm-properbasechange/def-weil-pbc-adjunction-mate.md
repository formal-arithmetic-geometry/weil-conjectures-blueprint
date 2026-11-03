+++
id = "def-weil-pbc-adjunction-mate"
kind = "definition"
title = "Mate of a transformation under two adjunctions"
lean = ["CategoryTheory.mateEquiv"]
order = 2092
tags = ["mathlib", "stacks-07A7"]
+++
Let $\mathcal C,\mathcal D,\mathcal E,\mathcal F$ be categories, let $L_1:\mathcal C\to\mathcal D$ be left adjoint to $R_1:\mathcal D\to\mathcal C$ (unit $\eta_1:\mathrm{id}\to R_1L_1$, counit $\varepsilon_1:L_1R_1\to\mathrm{id}$), let $L_2:\mathcal E\to\mathcal F$ be left adjoint to $R_2:\mathcal F\to\mathcal E$ (unit $\eta_2$, counit $\varepsilon_2$), and let $G:\mathcal C\to\mathcal E$ and $H:\mathcal D\to\mathcal F$ be functors. For a natural transformation $\alpha:L_2G\to HL_1$ its *mate* is the natural transformation $\alpha^\flat:GR_1\to R_2H$ with components

$$
 GR_1d\xrightarrow{\eta_{2,GR_1d}}R_2L_2GR_1d\xrightarrow{R_2\alpha_{R_1d}}R_2HL_1R_1d\xrightarrow{R_2H\varepsilon_{1,d}}R_2Hd ,
$$

equivalently the transformation whose transpose under $L_2\dashv R_2$ is $L_2GR_1\xrightarrow{\alpha R_1}HL_1R_1\xrightarrow{H\varepsilon_1}H$. The assignment $\alpha\mapsto\alpha^\flat$ is a bijection between natural transformations $L_2G\to HL_1$ and natural transformations $GR_1\to R_2H$, with inverse $\beta\mapsto (L_2G\xrightarrow{L_2G\eta_1}L_2GR_1L_1\xrightarrow{L_2\beta L_1}L_2R_2HL_1\xrightarrow{\varepsilon_2HL_1}HL_1)$.
