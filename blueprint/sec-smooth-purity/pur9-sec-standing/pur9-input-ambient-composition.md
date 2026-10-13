+++
id = "pur9-input-ambient-composition"
kind = "remark"
title = "Composition of standing compact-support direct images"
order = 2039
tags = ["latex:bpinput"]
uses = ["pur9-def-standing-choices", "pur9-lem-open-immersion-lower-shriek"]
+++
For composable $f:X\to Y$ and $g:Y\to S$ as in Definition [pur9-def-standing-choices], there are natural isomorphisms

$$
\alpha_{g,f}:Rg_{!,\mathcal O_E/\varpi^n}Rf_{!,\mathcal O_E/\varpi^n}\xrightarrow{\sim}R(gf)_{!,\mathcal O_E/\varpi^n}
$$

of functors $D(X_{\Proet},\mathcal O_E/\varpi^n)\to D(S_{\Proet},\mathcal O_E/\varpi^n)$, such that: $\alpha_{\mathrm{id}_Y,f}$ and $\alpha_{f,\mathrm{id}_X}$ are identities after the identifications $R\mathrm{id}_{!,\mathcal O_E/\varpi^n}\cong\mathrm{id}$ of Lemma [pur9-lem-open-immersion-lower-shriek]; for a further $h:S\to Z$, $\alpha_{h,gf}\circ(Rh_{!,\mathcal O_E/\varpi^n}\alpha_{g,f})=\alpha_{hg,f}\circ(\alpha_{h,g}Rf_{!,\mathcal O_E/\varpi^n})$; and on $\mathscr E^+(X_{\Proet},\mathcal O_E/\varpi^n)$, $\alpha_{g,f}=\alpha_{g,f,\mathcal O_E/\varpi^n}$ of Lemma “The composition law for $Rf_!$ at finite coefficients” (`pur456-lem-proet-composition`). *Status:* Lemmas “The composition law for $Rf_!$ at finite coefficients” (`pur456-lem-proet-composition`), “Identity normalization of the composition law” (`pur456-lem-proet-composition-unit`) and “Associativity of the composition law” (`pur456-lem-proet-composition-assoc`) establish these properties on the étale-origin subcategories only, under the site-comparison inputs; the ambient extension is not established here.
