+++
kind  = "proof"
of    = "thm-cbc-finite-torsion"
+++
Fix a compactification $c=(j,p)$ of $f$ with base change
$c'=(j',p')$ as in [def-cbc-compact-support-square]. The map
$\operatorname{Ex}_!(K)$ of [def-cbc-exchange-map] is the
composite

$$
\begin{aligned}
g^{-1}Rf_!K&=g^{-1}Rp_*j_!K
&&\text{(definitions)}\\
&\xrightarrow{\ \sim\ }Rp'_*g^{-1}j_!K
&&\text{(\Cref{thm-weil-pbc-bounded-below} applied to the
proper \(p\))}\\
&\xrightarrow{\ \sim\ }Rp'_*j'_!g'^{-1}K
&&\text{(\Cref{cor-cbc-derived-extension-zero-base-change})}\\
&=Rf'_!g'^{-1}K &&\text{(definitions).}
\end{aligned}
$$

The first arrow is an isomorphism by the bounded-below proper base
change of the proper-base-change chapter ([thm-weil-pbc-bounded-below]; $p$ is
proper, $g$ arbitrary, $j_!K\in D^+(X_{\Et},\Lambda)$ because
$j_!$ is exact), the second by the extension-by-zero base change of
[cor-cbc-derived-extension-zero-base-change] applied to the
open-immersion square with $g_U=g'$ (the square of
[def-cbc-compact-support-square] is cartesian, so
$X'=U\times_{\overline X}\overline X'$ and the identification
$j'_!g'^{-1}K$ is the one of
[def-cbc-exchange-map]). Hence $\operatorname{Ex}_!(K)$ is an
isomorphism for the chosen compactification. For another
compactification $c_1$ with a refinement to $c_2$, the
comparison isomorphisms of the compact-support direct image of
[def-compact-support-direct-image-detailed] commute with the two displayed factors by
[prop-compactification-coherence-detailed] (the comparison of $Rf_!$
is $Ru_*j_{1!}\xrightarrow{\sim}j_{2!}$ composed with the
composition isomorphism of proper direct images, and both factors of
$\operatorname{Ex}_!$ are compatible with the refinement maps, as
the refined data are cartesian over the same base change and the maps
are mates of compatible data); hence $\operatorname{Ex}_!(K)$ is
independent of the compactification. Naturality in $K$, the
identity for identity base changes, and the pasting laws follow from
the corresponding properties of the two factors (the proper exchange
of [thm-weil-pbc-bounded-below] and the extension-by-zero
comparison of [cor-cbc-derived-extension-zero-base-change]),
which is the statement of [def-cbc-exchange-map].
