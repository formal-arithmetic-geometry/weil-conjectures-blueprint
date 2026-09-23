+++
id = "a33.-finite-compact-support-base-change"
kind = "section"
title = "A33. Finite compact-support base change"
order = 1925
+++
Continue with the same fixed $\Lambda_n$, ambient categories, and
noetherian finite-dimensional $Y,Y'$. Let $f:X\to Y$ be separated and
finitely presented, let the square in A31 be Cartesian, and let
$K\in D_c^+(X,\Lambda_n)$. For the dense compactification $C$ of
(BA43-DENSE-DATA), construct the raw one-model map as the following
two-arrow composite:

$$
\begin{split}
\operatorname{BC}^{C,\mathrm{raw}}_{f,g,K}:Lg^*F_C(K)
&\xrightarrow{\operatorname{BC}_{p_C,g,Rj_{C!}K}}
Rp^{\mathrm{raw}}_{C,g,*}L\bar g^*Rj_{C!}K\\
&\xrightarrow{Rp^{\mathrm{raw}}_{C,g,*}
(\beta^{\mathrm{open}}_{j_C,\bar g,K})}
Rp^{\mathrm{raw}}_{C,g,*}Rj^{\mathrm{raw}}_{C,g,!}Lg'^*K.
\end{split}
\tag{BA33-RAW-BC}
$$

Here the first arrow is the already constructed proper base-change mate and
the second is the derived open-extension exchange. By definition the name
$\operatorname{BC}^{C,\mathrm{raw}}$ denotes their composite, never the first
arrow alone. Before finite PBC is applied, the separate leaf
`CAT-GEO-BA33-OPEN-EXTENSION-CONSTRUCTIBILITY` must prove
$Rj_{C!}K\in D_c^+(\overline X_C,\Lambda_n)$.

The dense representative is

$$
\operatorname{BC}^{C,\mathrm{den}}_{f,g,K}
=\sigma_{C,g}^{-1}\circ
\operatorname{BC}^{C,\mathrm{raw}}_{f,g,K}:
Lg^*F_C(K)\longrightarrow
F_{C_g^{\mathrm{den}}}(Lg'^*K).
\tag{BA33-DEN-BC}
$$

For a refinement $q:D\to C$,
`OBL-BA33-REFINEMENT-BASECHANGE-NATURALITY` proves equality of the
two explicit composites built from $Lg^*(\rho_q)$,
$\rho_{q_g^{\mathrm{den}}}$, the two maps
(BA33-DEN-BC), and the densification comparison. The proof must
expand proper-base-change naturality, open-exchange naturality, and all four
densification diagrams; the equality is not supplied in a comparison record.

Only then may the $\kappa$ cocycle descend the representatives to

$$
Lg^*Rf_!K\longrightarrow Rf'_!Lg'^*K.
$$

Identity and horizontal/vertical pasting consume the corresponding proper,
open, densification, and $\kappa$ equations. Therefore
`OBL-BA33-FINITE-COMPACT-SUPPORT-BASE-CHANGE` remains
`OPEN/INCOMPLETE`. Geometric-fibre, Frobenius-equivariant, tower,
integral, and rational exports are outside this finite-level owner.
