+++
id = "pur713-def-shriek-exchange"
kind = "definition"
title = "Compact-support exchange, finite coefficients"
order = 1872
tags = ["latex:bpdefinition"]
uses = ["pur713-def-base-changed-compactification", "pur713-def-star-exchange", "pur713-input-comparison", "pur713-lem-open-exchange"]
+++
For the chosen compactification $c_f=(j,p)$ of $f$ and its base change $c'=(j',p')$ of Definition [pur713-def-base-changed-compactification], the finite-coefficient compact-support exchange

$$
\operatorname{Ex}_{!,\square,\mathcal O_E/\varpi^n}:
Lg^*_{\mathcal O_E/\varpi^n}Rf_{!,\mathcal O_E/\varpi^n}
\longrightarrow R_{c'}Lg'^*_{\mathcal O_E/\varpi^n},
$$

a natural transformation of functors $D(X_{\Proet},\mathcal O_E/\varpi^n)\to D(Y'_{\Proet},\mathcal O_E/\varpi^n)$ between the functors of Definitions “Finite-coefficient compact-support direct image” (`pur713-def-lower-shriek`) and “Compact-support direct image for an auxiliary compactification” (`pur713-def-lower-shriek-auxiliary`), has component at $K$ the composite

$$
\begin{aligned}
Lg^*_{\mathcal O_E/\varpi^n}Rp_{*,\mathcal O_E/\varpi^n}\mathrm D(j_{!,\mathcal O_E/\varpi^n})K
&\xrightarrow{\operatorname{Ex}_{*,\square_p,\mathcal O_E/\varpi^n}}Rp'_{*,\mathcal O_E/\varpi^n}L\bar g^*_{\mathcal O_E/\varpi^n}\mathrm D(j_{!,\mathcal O_E/\varpi^n})K\\
&\xrightarrow{Rp'_{*,\mathcal O_E/\varpi^n}(b_{j,\bar g,\mathcal O_E/\varpi^n,K})}
Rp'_{*,\mathcal O_E/\varpi^n}\mathrm D(j'_{!,\mathcal O_E/\varpi^n})Lg'^*_{\mathcal O_E/\varpi^n}K,
\end{aligned}
$$

with $\operatorname{Ex}_{*,\square_p,\mathcal O_E/\varpi^n}$ of Definition [pur713-def-star-exchange] for the square $\square_p$ and $b$ of Lemma [pur713-lem-open-exchange]. Its target is formed with the base-changed compactification $c'$, which in general differs from $c_{f'}$; passing to $Rf'_{!,\mathcal O_E/\varpi^n}$ requires a comparison $R_{c'}\cong R_{c_{f'}}$, see Input [pur713-input-comparison].
