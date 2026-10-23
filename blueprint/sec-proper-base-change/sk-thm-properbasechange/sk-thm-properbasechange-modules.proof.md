+++
kind = "proof"
of = "det-properbasechange-modules"
+++
*Part 1.* Restriction of scalars $\mathrm{res}$ is exact and conservative on
sheaves, so it reflects quasi-isomorphisms of complexes and isomorphisms in
$D^+$. It commutes with $u^{-1}$ and $u_*$ for every morphism $u$, because
inverse and direct image of module sheaves are computed on underlying
sheaves. Choose a bounded below complex $I^\bullet$ of injective
$\Lambda'$-module sheaves with $K\simeq I^\bullet$, and a quasi-isomorphism
$g'^{-1}I^\bullet\to J^\bullet$ into a bounded below complex of injective
$\Lambda'$-module sheaves on $X'$. By the resolution formula
[lemma-weil-pbc-derived-exchange-replacement], $\Ex^{\Lambda'}_{\square,K}$ is
represented by

$$
g^{-1}f_*I^\bullet\xrightarrow{\ \Ex^0_{\square,I^\bullet}\ }
f'_*g'^{-1}I^\bullet\longrightarrow f'_*J^\bullet .
$$

The underived exchange map is built from the unit, the square isomorphism and
the counit of the adjunctions $u^{-1}\dashv u_*$, and these are the same maps
of underlying sheaves for $\Lambda'$- and for $\Lambda$-module sheaves, so
$\mathrm{res}(\Ex^0_{\square,I^m})=\Ex^0_{\square,\mathrm{res}I^m}$ in every
degree. An injective $\Lambda'$-module sheaf has vanishing higher cohomology on
every étale $U$ when viewed as a $\Lambda$-module sheaf: both cohomologies are
computed on the underlying abelian sheaf, by parts (1) and (2) of
[det-pbc-conventions-module-cohomology] (for $\Lambda'$ and for $\Lambda$).
By part (3) there and the complex form of [lemma-weil-pbc-leray-acyclicity],
the terms of $\mathrm{res}I^\bullet$ and $\mathrm{res}J^\bullet$ are
$f_*$-acyclic resp. $f'_*$-acyclic, so $f_*\mathrm{res}I^\bullet$ and
$f'_*\mathrm{res}J^\bullet$ compute $Rf_*\mathrm{res}K$ and
$Rf'_*g'^{-1}\mathrm{res}K$. Comparing with injective resolutions
$\mathrm{res}I^\bullet\to I'^\bullet$ and $g'^{-1}I'^\bullet\to J'^\bullet$ of
$\Lambda$-module sheaves, with a compatible map
$\mathrm{res}J^\bullet\to J'^\bullet$ (it exists and is unique up to homotopy
because $J'^\bullet$ is a bounded below complex of injectives), naturality of
$\Ex^0$ gives a commutative diagram

$$
\begin{array}{ccccc}
g^{-1}f_*\mathrm{res}I^\bullet & \to & f'_*g'^{-1}\mathrm{res}I^\bullet & \to & f'_*\mathrm{res}J^\bullet\\
\downarrow & & \downarrow & & \downarrow\\
g^{-1}f_*I'^\bullet & \to & f'_*g'^{-1}I'^\bullet & \to & f'_*J'^\bullet
\end{array}
$$

whose outer vertical arrows are quasi-isomorphisms, by the acyclicity just
proved. The bottom row represents $\Ex^{\Lambda}_{\square,\mathrm{res}K}$ by
[lemma-weil-pbc-derived-exchange-replacement], and the top row is
$\mathrm{res}$ of the representative of $\Ex^{\Lambda'}_{\square,K}$. Hence
$\Ex^{\Lambda}_{\square,\mathrm{res}K}$ is an isomorphism if and only if
$\mathrm{res}(\Ex^{\Lambda'}_{\square,K})$ is, and since $\mathrm{res}$
reflects isomorphisms, if and only if $\Ex^{\Lambda'}_{\square,K}$ is.

*Part 2.* Apply part 1 to the unique ring map $\mathbf Z\to\Lambda$, for which
$\mathrm{res}$ is the forgetful functor to abelian sheaves. The cohomology
sheaves of $\mathrm{res}K$ are torsion, so
$\Ex^{\mathbf Z}_{\square,\mathrm{res}K}$ is an isomorphism by
[thm-weil-pbc-bounded-below]. By part 1, $\Ex^{\Lambda}_{\square,K}$ is an
isomorphism in $D^+(Y'_{\Et},\Lambda)$.
