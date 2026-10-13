+++
id = "pur9-cs-def-phi"
kind = "definition"
title = "The tensor comparison of a smooth morphism"
order = 2336
tags = ["latex:bpdefinition"]
uses = ["pur713-def-shriek-projection", "pur713-input-proper-adjoint", "pur9-cs-input-constructible-closure", "pur9-def-shriek-notation", "pur9-input-preservation", "pur9-lem-proet-projection-formula"]
+++
Assume Inputs [pur713-input-proper-adjoint], [pur9-input-preservation] and [pur9-cs-input-constructible-closure] and the hypotheses of Lemma [pur9-lem-proet-projection-formula]. For $f:X\to Y$ and $K\in D^b_{ctf}(Y_{\Proet},\mathcal O_E/\varpi^n)$, the object $\omega_f$ lies in $D^b_{ctf}(X_{\Proet},\mathcal O_E/\varpi^n)$ by Input [pur9-input-preservation], so the projection map $\operatorname{PF}_{f,\omega_f,K,\mathcal O_E/\varpi^n}$ of Definition [pur713-def-shriek-projection] is invertible by Lemma [pur9-lem-proet-projection-formula]. Define

$$
\varphi_{f,K}:Lf^*_{\mathcal O_E/\varpi^n}K\otimes^L_{\mathcal O_E/\varpi^n}\omega_f\longrightarrow Rf^!_{\mathcal O_E/\varpi^n}K
$$

as the morphism corresponding, under the standing adjunction of Definition [pur9-def-shriek-notation], to

$$
Rf_{!,\mathcal O_E/\varpi^n}(Lf^*_{\mathcal O_E/\varpi^n}K\otimes^L_{\mathcal O_E/\varpi^n}\omega_f)
\cong Rf_{!,\mathcal O_E/\varpi^n}(\omega_f\otimes^L_{\mathcal O_E/\varpi^n} Lf^*_{\mathcal O_E/\varpi^n}K)
\xrightarrow{(\operatorname{PF}_{f,\omega_f,K,\mathcal O_E/\varpi^n})^{-1}}
Rf_{!,\mathcal O_E/\varpi^n}\omega_f\otimes^L_{\mathcal O_E/\varpi^n} K
\xrightarrow{\varepsilon_{f}\otimes1}(\mathcal O_E/\varpi^n)_Y\otimes^L_{\mathcal O_E/\varpi^n} K\cong K,
$$

where the unnamed isomorphisms are the symmetry and unit isomorphisms of Definition “Finite-coefficient derived tensor product” (`pur713-def-tensor`) and $\varepsilon_f$ is the counit of the standing adjunction at $(\mathcal O_E/\varpi^n)_Y$.
