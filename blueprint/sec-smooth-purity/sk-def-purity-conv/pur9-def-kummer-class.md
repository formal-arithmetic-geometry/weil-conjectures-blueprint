+++
id = "pur9-def-kummer-class"
kind = "definition"
title = "Kummer classes"
order = 2234
tags = ["latex:bpdefinition"]
uses = ["pur7710-def-derived-sections", "pur9-lem-roots-constant"]
+++
Let $W$ be a $k$-scheme and $t\in\Gamma(W,\mathcal O_W^\times)$. For $N\geq1$, the Kummer sequence $0\to\mu_{\ell^N,W}\to\mathbb G_{m,W}\xrightarrow{\omega\mapsto\omega^{\ell^N}}\mathbb G_{m,W}\to0$ on $W_{\Et}$ (the sequence of -def-kummerZZ, written on $W$) is exact by -prop-kummer-exactZZ, since $\ell^N$ is invertible on $W$. Let $\kappa_N(t)\in H^1(W_{\Et},\mu_{\ell^N,W})$ be the image of $t\in H^0(W_{\Et},\mathbb G_{m,W})$ under its connecting homomorphism, cohomology being that of abelian sheaves. For admissible $N$, the *Kummer class* of $t$ is

$$
\kappa(t)\in H^1\bigl(W_{\Et},(\mathcal O_E/\varpi^n)_W(1)\bigr):=H^1R\Gamma_{W,\Et,\mathcal O_E/\varpi^n}\bigl((\mathcal O_E/\varpi^n)_W(1)\bigr),
$$

the image of $\kappa_N(t)$ under the map induced by $\mu_{\ell^N,W}\cong\mu_{\ell^N}(k)_W\to P(1)_W$, $\zeta\mapsto\zeta\otimes1$ (Lemma [pur9-lem-roots-constant]), followed by the identification of abelian-sheaf cohomology with module-sheaf cohomology given by Input “Forgetting finite coefficient actions in direct images” (`pur7710-input-cohomology-coefficients`, see [sk-thm-sf-comp-composition]) for the structure morphism $W\to\operatorname{Spec}k$. Derived sections are those of Definition [pur7710-def-derived-sections].
