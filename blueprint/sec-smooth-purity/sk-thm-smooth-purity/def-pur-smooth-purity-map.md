+++
id = "def-pur-smooth-purity-map"
kind = "definition"
title = "The smooth purity isomorphism for an arbitrary coefficient object"
lean = ["AlgebraicGeometry.Etale.smoothPurityIso"]
order = 2356
uses = ["pur9-cs-def-phi", "sk-prop-cohsm"]
+++
Under the hypotheses of Theorem “Finite-coefficient smooth purity” (`pur9-thm-smooth-purity`) and Lemma “Tensor formula for smooth morphisms” (`pur9-cs-lem-tensor-formula`, in [sk-prop-cohsm]), for $K\in D^b_{ctf}(Y_{\Proet},\mathcal O_E/\varpi^n)$ let

$$
\gamma^{\mathrm{sm}}_{f,K}:Lf^*_{\mathcal O_E/\varpi^n}K\otimes^L_{\mathcal O_E/\varpi^n}(\mathcal O_E/\varpi^n)_X(d)[2d]\xrightarrow{1\otimes\Pi_f^{-1}}Lf^*_{\mathcal O_E/\varpi^n}K\otimes^L_{\mathcal O_E/\varpi^n}\omega_f\xrightarrow{\varphi_{f,K}}Rf^!_{\mathcal O_E/\varpi^n}K,
$$

with $\Pi_f$ of Theorem “Finite-coefficient smooth purity” (`pur9-thm-smooth-purity`) and $\varphi$ of Definition [pur9-cs-def-phi].
