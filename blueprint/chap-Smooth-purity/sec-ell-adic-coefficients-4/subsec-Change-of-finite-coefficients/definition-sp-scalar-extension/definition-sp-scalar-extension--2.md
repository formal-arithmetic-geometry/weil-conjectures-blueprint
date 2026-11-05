+++
id = "definition-sp-scalar-extension--2"
kind = "lemma"
title = "Extension of scalars (2)"
name_showing = false
order = 767002
aliases = ["bp-r231-2"]
lean = ["CategoryTheory.Mod.derivedExtendScalarsCompIso"]
+++
Let $\mathcal A$ be a closed symmetric monoidal Grothendieck abelian category
with biadditive tensor product and functorial flat resolutions. Let
$\varphi:A\to B$, $\psi:B\to C$ and $\chi:A\to C$ be morphisms of commutative
algebra objects with $\psi\circ\varphi=\chi$. Write $\mathbf L(B\otimes_A-)$ for
the derived extension of scalars along $\varphi$, and similarly for $\psi$
and $\chi$. There is a canonical natural isomorphism

$$
\mathbf L(C\otimes_A-)\simeq\mathbf L(C\otimes_B-)\circ\mathbf L(B\otimes_A-)
$$

of functors $D(\operatorname{Mod}_A(\mathcal A))\to
D(\operatorname{Mod}_C(\mathcal A))$.

Taking $\mathcal A$ to be the category of abelian sheaves on
$T_{\mathrm{pro}\acute{e}t}$ and the algebra objects to be $A_T,B_T,C_T$
gives $(K_B)_C\simeq K_C$, with the notation of
[definition-sp-scalar-extension--1], naturally for every
$K\in D(T_{\mathrm{pro}\acute{e}t},A)$. No flatness hypothesis on the
coefficient maps is needed.
