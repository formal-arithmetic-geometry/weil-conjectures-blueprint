+++
id = "pur9-def-upper-shriek-composition"
kind = "definition"
title = "Composition comparison for standing exceptional inverse images"
order = 2043
tags = ["latex:bpdefinition"]
uses = ["pur9-def-shriek-notation", "pur9-def-standing-choices", "pur9-input-ambient-composition"]
+++
Assume Input [pur9-input-ambient-composition]. For composable $f:X\to Y$ and $g:Y\to S$ as in Definition [pur9-def-standing-choices] and $L\in D(S_{\Proet},\mathcal O_E/\varpi^n)$, let

$$
c_{g,f,L}:R(gf)^!_{\mathcal O_E/\varpi^n}L\longrightarrow Rf^!_{\mathcal O_E/\varpi^n}Rg^!_{\mathcal O_E/\varpi^n}L
$$

be the morphism corresponding, under the composite adjunction $Rg_{!,\mathcal O_E/\varpi^n}Rf_{!,\mathcal O_E/\varpi^n}\dashv Rf^!_{\mathcal O_E/\varpi^n}Rg^!_{\mathcal O_E/\varpi^n}$ of Definition [pur9-def-shriek-notation], to the composite

$$
Rg_{!,\mathcal O_E/\varpi^n}Rf_{!,\mathcal O_E/\varpi^n}R(gf)^!_{\mathcal O_E/\varpi^n}L
\xrightarrow{\alpha_{g,f}}R(gf)_{!,\mathcal O_E/\varpi^n}R(gf)^!_{\mathcal O_E/\varpi^n}L
\xrightarrow{\varepsilon_{gf,L}}L,
$$

where $\varepsilon_{gf}$ is the counit of the standing adjunction for $gf$.
