+++
kind = "proof"
of = "det-properbasechange-modules"
+++
*Step 1: the identification.* Choose a bounded below complex $I^\bullet$ of
injective $\Lambda$-module sheaves with $K\simeq I^\bullet$, and a
quasi-isomorphism $g'^{-1}I^\bullet\to J^\bullet$ into a bounded below complex
of injective $\Lambda$-module sheaves on $X'$. By the resolution formula
[lemma-weil-pbc-derived-exchange-replacement], $\Ex^\Lambda_{\square,K}$ is
represented by

$$
g^{-1}f_*I^\bullet\xrightarrow{\ \Ex^0_{\square,I^\bullet}\ }
f'_*g'^{-1}I^\bullet\longrightarrow f'_*J^\bullet .
$$

The underived exchange map is defined by the unit, the square isomorphism and
the counit of the adjunctions $u^{-1}\dashv u_*$; these are the same maps of
underlying abelian sheaves whether one regards the sheaves as module sheaves
or as abelian sheaves, because inverse and direct image of module sheaves are
computed on underlying abelian sheaves. Hence
$\mathrm{For}(\Ex^0_{\square,I^m})=\Ex^0_{\square,\mathrm{For}I^m}$ in every
degree. By parts (1) and (3) of [det-pbc-conventions-module-cohomology], the terms of
$\mathrm{For}I^\bullet$ are $f_*$-acyclic and those of $\mathrm{For}J^\bullet$
are $f'_*$-acyclic, so by the complex form of
[lemma-weil-pbc-leray-acyclicity] the complexes $f_*\mathrm{For}I^\bullet$ and
$f'_*\mathrm{For}J^\bullet$ compute $Rf_*\mathrm{For}K$ and
$Rf'_*g'^{-1}\mathrm{For}K$. Now choose a quasi-isomorphism
$\mathrm{For}I^\bullet\to I'^\bullet$ into a bounded below complex of
injective abelian sheaves and an injective replacement
$g'^{-1}I'^\bullet\to J'^\bullet$ together with a map
$\mathrm{For}J^\bullet\to J'^\bullet$ compatible with
$g'^{-1}\mathrm{For}I^\bullet\to g'^{-1}I'^\bullet$ (it exists and is unique
up to homotopy because $J'^\bullet$ is a bounded below complex of injectives
and $g'^{-1}\mathrm{For}I^\bullet\to\mathrm{For}J^\bullet$ is a
quasi-isomorphism). Naturality of $\Ex^0$ in the sheaf gives a commutative
diagram of complexes

$$
\begin{array}{ccccc}
g^{-1}f_*\mathrm{For}I^\bullet & \to & f'_*g'^{-1}\mathrm{For}I^\bullet & \to & f'_*\mathrm{For}J^\bullet\\
\downarrow & & \downarrow & & \downarrow\\
g^{-1}f_*I'^\bullet & \to & f'_*g'^{-1}I'^\bullet & \to & f'_*J'^\bullet
\end{array}
$$

whose vertical outer arrows are quasi-isomorphisms (both rows' end terms
compute the same derived functors, by acyclicity). The bottom row represents
$\Ex^{\mathbf Z}_{\square,\mathrm{For}K}$ by
[lemma-weil-pbc-derived-exchange-replacement], and the top row is
$\mathrm{For}$ of the representative of $\Ex^\Lambda_{\square,K}$. This
proves the identification.

*Step 2: the consequence.* If $\mathrm{For}K$ has torsion cohomology sheaves,
$\Ex^{\mathbf Z}_{\square,\mathrm{For}K}$ is an isomorphism by
[thm-weil-pbc-bounded-below]. By Step 1, $\mathrm{For}$ of
$\Ex^\Lambda_{\square,K}$ is an isomorphism. The forgetful functor is exact
and conservative on sheaves, so it reflects quasi-isomorphisms of complexes,
and $\Ex^\Lambda_{\square,K}$ is an isomorphism in $D^+(Y'_{\Et},\Lambda)$.
