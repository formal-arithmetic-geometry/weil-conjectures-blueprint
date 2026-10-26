+++
id = "pur9-def-purity-comparison"
kind = "definition"
title = "Purity comparison for a vector bundle"
order = 2894
uses = ["pur713-def-shriek-projection", "sk-thm-sf-pf-finite"]
+++
Let $\pi:V\to Z$ be a vector bundle of rank $c$ as in Lemma “Gluing the trace of a vector bundle” (`pur9-lem-bundle-trace-gluing`), and $K\in D^b_{ctf}(Z_{\Proet},\mathcal O_E/\pi_E^n)$. The purity comparison

$$
\gamma_{\pi,K}:L\pi^*_{\mathcal O_E/\pi_E^n}K(c)[2c]\longrightarrow R\pi^!_{\mathcal O_E/\pi_E^n}K
$$

is the morphism corresponding, under the standing adjunction $R\pi_{!,\mathcal O_E/\pi_E^n}\dashv R\pi^!_{\mathcal O_E/\pi_E^n}$ (Definition “Standing compact-support and exceptional functors” (`pur9-def-shriek-notation`)), to the composite

$$
R\pi_{!,\mathcal O_E/\pi_E^n}\bigl(L\pi^*_{\mathcal O_E/\pi_E^n}K(c)[2c]\bigr)\cong R\pi_{!,\mathcal O_E/\pi_E^n}\bigl((\mathcal O_E/\pi_E^n)_V(c)[2c]\otimes^L_{\mathcal O_E/\pi_E^n} L\pi^*_{\mathcal O_E/\pi_E^n}K\bigr)
\xrightarrow{\operatorname{PF}^{-1}}R\pi_{!,\mathcal O_E/\pi_E^n}\bigl((\mathcal O_E/\pi_E^n)_V(c)\bigr)[2c]\otimes^L_{\mathcal O_E/\pi_E^n} K
\xrightarrow{\int_\pi\otimes1}K,
$$

all at the coefficient $\mathcal O_E/\pi_E^n$: the first isomorphism is the symmetry of the tensor product, $\operatorname{PF}$ is the compact-support projection transformation of Definition [pur713-def-shriek-projection] for the standing compactification, invertible here by Lemma “The pro-étale compact-support projection formula” (`pur9-lem-proet-projection-formula`, in [sk-thm-sf-pf-finite]) (the constant sheaf lies in $D^b_c(V_{\Proet},\mathcal O_E/\pi_E^n)$), and the last map uses the unit isomorphism of the tensor product. For $V=\Aaf^c_B$ with its standard trivialization, $\int_\pi=\int_{p_c}$.
