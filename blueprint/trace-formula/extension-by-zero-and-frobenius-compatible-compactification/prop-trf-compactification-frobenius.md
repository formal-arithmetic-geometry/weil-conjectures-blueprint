+++
id = "prop-trf-compactification-frobenius"
kind = "theorem"
title = "Compactification intertwines the Frobenius operators"
order = 3943
tags = ["latex:proposition"]
uses = ["def-exchange-projection", "def-trf-frobenius-operators", "def-trf-iterated-weil-map", "def-trf-weil-extension-zero", "def-weil-compact-support-candidate", "def-weil-compactifications-refinements", "def-weil-finite-coefficient-point", "def-weil-pbc-etale-origin-witness", "lem-trf-compactification-cohomology", "lem-trf-frobenius-open-square", "lem-trf-open-square-exchange", "lem-trf-weil-extension-iterates", "lem-weil-pbc-comparison-pullback"]
+++
Let $j_0:X_0\hookrightarrow\bar X_0$ be a
compactification
over $k_0$, and let $j$ be its base change to $k$.
For the Weil extension by
zero $(\bar K,\bar\varphi)$ of $(K,\varphi)$, assume $K$ has
an explicit etale-origin
witness. Then the comparison
$C_{j,K}$ of [lem-trf-compactification-cohomology]
intertwines $F_{c,K}^{\,m}$ with the
global Frobenius operator
on $R\Gamma(\bar X,\bar K)$ obtained from the
iterate $\bar\varphi^{[m]}$.
This holds for every $m\geq1$, as an equality of endomorphisms in
the derived coefficient
category over $s=\Spec k$.

## Proof

Write $\bar g=g_{\bar X}$, $g=g_X$, $g_s=\Spec(\gamma)$.
The Galois square for the structure map is Cartesian and
$\bar a\bar g^m=g_s^m\bar a$, by
[lem-trf-frobenius-open-square]. Pullbacks $Lg^{m*}K$
retain explicit etale-origin witnesses by
[lem-weil-pbc-comparison-pullback], so the comparisons below
stay in the domain of the proved compactification coherence.
In the compact-support
candidate of [def-weil-compact-support-candidate], the
base-change map is the following composite:

$$
\begin{aligned}
Lg_s^{m*}R\bar a_*j_!K
&\xrightarrow{\mathrm{Ex}_*}
R\bar a_*L\bar g^{m*}j_!K\\
&\xrightarrow{R\bar a_*b_{\bar g^m}}
R\bar a_*j_!Lg^{m*}K.
\end{aligned}
$$

The first arrow is the proper exchange of
[def-exchange-projection]; the second is the open-square
comparison of [lem-trf-open-square-exchange]. Because the
vertical Galois maps and the base map are isomorphisms, the
proper exchange here is also the ordinary change-of-variables
identification for direct images. On a site object its map is
the section map for the same Cartesian square, so this description
fixes the exchange map, not merely its isomorphism class.

Follow this composite by $R\bar a_*j_!\varphi^{[m]}$.
By [lem-trf-weil-extension-iterates], its last two arrows
combine to $R\bar a_*\bar\varphi^{[m]}$. The resulting composite

$$
Lg_s^{m*}R\bar a_*\bar K
\longrightarrow R\bar a_*L\bar g^{m*}\bar K
\xrightarrow{R\bar a_*\bar\varphi^{[m]}}
R\bar a_*\bar K
$$

is the ordinary Frobenius action for the proper scheme $\bar X$.
Apply the fiber functor of [def-weil-finite-coefficient-point].
On the constructible coefficient category over the algebraically
closed point, pulling back by $g_s^m$ fixes the constant
coefficient module, with its specified constant identification.
Thus both displayed source complexes identify with the same
coefficient complex. The first composite is the compact-support
Frobenius of [def-trf-frobenius-operators]; the second is the
ordinary one on the compactification.

The map $C_{j,K}$ of
[lem-trf-compactification-cohomology] is precisely the
identification with this candidate. The displayed calculation
therefore proves the intertwining equality. It keeps the
nontrivial base map $g_s$; no equality $a_Xg=a_X$ is used.
There is no trace class or Lefschetz–Verdier input in this proof.
