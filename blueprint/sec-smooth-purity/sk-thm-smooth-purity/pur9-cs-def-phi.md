+++
id = "pur9-cs-def-phi"
kind = "definition"
title = "The tensor comparison of a smooth morphism"
order = 2941
uses = ["pur713-def-shriek-projection", "det-def-sf-operations", "sk-prop-cohsm", "sk-thm-sf-pf-finite"]
+++
Assume Inputs “Finite-coefficient proper-adjoint input” (`pur713-input-proper-adjoint`, in [det-def-sf-operations]), “Preservation of finite-Tor constructible objects” (`pur9-input-preservation`) and “Closure of the bounded constructible categories” (`pur9-cs-input-constructible-closure`, in [sk-prop-cohsm]) and the hypotheses of Lemma “The pro-étale compact-support projection formula” (`pur9-lem-proet-projection-formula`, in [sk-thm-sf-pf-finite]). For $f:X\to Y$ and $K\in D^b_{ctf}(Y_{\Proet},\mathcal O_E/\pi_E^n)$, the object $\omega_f$ lies in $D^b_{ctf}(X_{\Proet},\mathcal O_E/\pi_E^n)$ by Input “Preservation of finite-Tor constructible objects” (`pur9-input-preservation`), so the projection map $\operatorname{PF}_{f,\omega_f,K,\mathcal O_E/\pi_E^n}$ of Definition [pur713-def-shriek-projection] is invertible by Lemma “The pro-étale compact-support projection formula” (`pur9-lem-proet-projection-formula`, in [sk-thm-sf-pf-finite]). Define

$$
\varphi_{f,K}:Lf^*_{\mathcal O_E/\pi_E^n}K\otimes^L_{\mathcal O_E/\pi_E^n}\omega_f\longrightarrow Rf^!_{\mathcal O_E/\pi_E^n}K
$$

as the morphism corresponding, under the standing adjunction of Definition “Standing compact-support and exceptional functors” (`pur9-def-shriek-notation`), to

$$
Rf_{!,\mathcal O_E/\pi_E^n}(Lf^*_{\mathcal O_E/\pi_E^n}K\otimes^L_{\mathcal O_E/\pi_E^n}\omega_f)
\cong Rf_{!,\mathcal O_E/\pi_E^n}(\omega_f\otimes^L_{\mathcal O_E/\pi_E^n} Lf^*_{\mathcal O_E/\pi_E^n}K)
\xrightarrow{(\operatorname{PF}_{f,\omega_f,K,\mathcal O_E/\pi_E^n})^{-1}}
Rf_{!,\mathcal O_E/\pi_E^n}\omega_f\otimes^L_{\mathcal O_E/\pi_E^n} K
\xrightarrow{\varepsilon_{f}\otimes1}(\mathcal O_E/\pi_E^n)_Y\otimes^L_{\mathcal O_E/\pi_E^n} K\cong K,
$$

where the unnamed isomorphisms are the symmetry and unit isomorphisms of Definition “Finite-coefficient derived tensor product” (`pur713-def-tensor`) and $\varepsilon_f$ is the counit of the standing adjunction at $(\mathcal O_E/\pi_E^n)_Y$.
