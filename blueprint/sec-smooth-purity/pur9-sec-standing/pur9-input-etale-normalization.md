+++
id = "pur9-input-etale-normalization"
kind = "remark"
title = "Exceptional inverse image along étale morphisms"
order = 2045
tags = ["latex:bpinput"]
uses = ["pur9-def-standing-choices", "pur9-def-upper-shriek-composition", "pur9-input-ambient-composition", "pur9-lem-open-immersion-upper-shriek"]
+++
For every étale morphism $u:U\to X$ as in Definition [pur9-def-standing-choices], there is a specified natural isomorphism $\epsilon_u:Ru^!_{\mathcal O_E/\varpi^n}\xrightarrow{\sim}Lu^*_{\mathcal O_E/\varpi^n}$ of functors $D(X_{\Proet},\mathcal O_E/\varpi^n)\to D(U_{\Proet},\mathcal O_E/\varpi^n)$, such that: if $u$ is an open immersion, $\epsilon_u$ is the equality of Lemma [pur9-lem-open-immersion-upper-shriek] followed by the identification $\mathrm D(u^*_{\mathcal O_E/\varpi^n})\cong Lu^*_{\mathcal O_E/\varpi^n}$ of Lemma “The finite-coefficient derived inverse image is levelwise” (`pur713-lem-finite-pull-levelwise`); and for composable étale $v:W\to U$ and $u:U\to X$,

$$
\mu_{u,v,\mathcal O_E/\varpi^n}\circ(\epsilon_vLu^*_{\mathcal O_E/\varpi^n})\circ(Rv^!_{\mathcal O_E/\varpi^n}\epsilon_u)\circ c_{u,v}=\epsilon_{uv},
$$

with $\mu$ the composition comparison of Lemma “The finite-coefficient inverse-image composition comparison is invertible” (`pur713-lem-pull-composition`) and $c_{u,v}$ of Definition [pur9-def-upper-shriek-composition] (so this clause presupposes Input [pur9-input-ambient-composition]). *Status:* for open immersions the isomorphism is Lemma [pur9-lem-open-immersion-upper-shriek]; for general étale $u$ neither the isomorphism nor the composition equation is established here.
