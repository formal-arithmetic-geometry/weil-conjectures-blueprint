+++
id = "sk-def-pe-replete"
kind = "definition"
title = "Repleteness"
order = 973
lean = ["CategoryTheory.GrothendieckTopology.IsReplete"]
tags = ["sketch"]
+++
A topos $\mathcal T$ is *replete* if, for every inverse sequence
$\cdots\to F_2\to F_1\to F_0$ of sheaves of sets with epimorphic transition maps, the
projection $\varprojlim_nF_n\to F_m$ is an epimorphism for every $m$.

Inverse limits are needed to pass from torsion to adic coefficients. Since surjectivity
and exactness can be checked on sections over weakly contractible objects, sequential
limits along epimorphisms remain epimorphic and products are exact.
