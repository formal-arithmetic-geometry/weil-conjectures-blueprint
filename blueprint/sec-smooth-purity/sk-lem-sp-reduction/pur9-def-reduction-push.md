+++
id = "pur9-def-reduction-push"
kind = "definition"
title = "Reduction comparison for direct image"
order = 2365
uses = ["sk-prop-sf-pf-reduction"]
+++
Under Input “Reduction commutes with inverse image and tensor product” (`pur9-input-reduction-monoidal`, in [sk-prop-sf-pf-reduction]), for $p:\overline X\to Y$ and $M\in D(\overline X_{\Proet},\mathcal O_E/\varpi^n)$, let

$$
r_{*,p,M}:\mathrm{red}_{n,m}Rp_{*,\mathcal O_E/\varpi^n}M\to Rp_{*,\mathcal O_E/\varpi^m}\mathrm{red}_{n,m}M
$$

in $D(Y_{\Proet},\mathcal O_E/\varpi^m)$ be the adjoint, under $Lp^*_{\mathcal O_E/\varpi^m}\dashv Rp_{*,\mathcal O_E/\varpi^m}$ (Lemma “Finite-coefficient derived inverse-image adjunction” (`pur713-lem-star-adjunction`)), of

$$
Lp^*_{\mathcal O_E/\varpi^m}\mathrm{red}_{n,m}Rp_{*,\mathcal O_E/\varpi^n}M\xrightarrow{(r^*_p)^{-1}}\mathrm{red}_{n,m}Lp^*_{\mathcal O_E/\varpi^n}Rp_{*,\mathcal O_E/\varpi^n}M\xrightarrow{\mathrm{red}_{n,m}\varepsilon_{p,M}}\mathrm{red}_{n,m}M.
$$

For $f$ with chosen compactification $c_f=(j,p)$ and $K\in D(X_{\Proet},\mathcal O_E/\varpi^n)$, let $r_{!,f,K}:\mathrm{red}_{n,m}Rf_{!,\mathcal O_E/\varpi^n}K\to Rf_{!,\mathcal O_E/\varpi^m}\mathrm{red}_{n,m}K$ be $r_{*,p,\mathrm D(j_{!,\mathcal O_E/\varpi^n})K}$ followed by $Rp_{*,\mathcal O_E/\varpi^m}$ of the identification $\mathrm{red}_{n,m}\mathrm D(j_{!,\mathcal O_E/\varpi^n})\cong\mathrm D(j_{!,\mathcal O_E/\varpi^m})\mathrm{red}_{n,m}$ of Input “Reduction commutes with inverse image and tensor product” (`pur9-input-reduction-monoidal`, in [sk-prop-sf-pf-reduction]).
