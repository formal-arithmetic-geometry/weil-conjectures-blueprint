+++
id = "cor-pur-arbitrary-base-change"
kind = "theorem"
title = "Smooth base-change coherence needs no smoothness of the base change"
order = 3637
tags = ["latex:corollary"]
uses = ["cor-pur-vector-bundle-purity", "def-exchange-projection", "def-pur-conventions", "def-pur-smooth-purity-map", "def-sbc-smooth-morphisms", "lem-pur-diagonal-base-change", "lem-pur-smb-extraordinary", "thm-pur-cohomological-smoothness", "thm-pur-diagonal-dualizing-object", "thm-pur-dnc-invariance", "thm-pur-smooth-base-change-coherence"]
+++
In the purity conventions of this chapter ([def-pur-conventions] fixed setting),
let the Cartesian square

$$
\begin{array}{ccc}
X'&\xrightarrow{\ u\ }&X\\
f'\downarrow&&\downarrow f\\
Y'&\xrightarrow{\ v\ }&Y
\end{array}
$$

have $f$ smooth of pure relative dimension $d$, $f'$ its base
change, $v$ *arbitrary*, and let $K\in D^b_{ctf}(Y,\Lambda)$.
Then the square of [thm-pur-smooth-base-change-coherence] commutes
for this $v$, and its vertical exchange map

$$
\operatorname{Ex}^{!,\mathrm{sm}}_{f,v,K}:\
Lu^*Rf^!K\xrightarrow{\ \sim\ }Rf'^!Lv^*K
$$

is an isomorphism; in particular $Lu^*\omega_f\cong\omega_{f'}$ for
arbitrary base change. The smooth base-change lemma
[lem-pur-smb-extraordinary] supplies this exchange before an
orientation is chosen; the coherence theorem identifies its action
on the chosen orientation. Neither result requires the base change
to be smooth.

## Proof

The map $v$ is arbitrary already in
[lem-pur-smb-extraordinary]; that result makes the exceptional
exchange an isomorphism before an orientation is chosen.
The square comparing this exchange with the normalized purity maps
commutes by [thm-pur-smooth-base-change-coherence], which also
has no smoothness hypothesis on $v$. At $K=\Lambda_Y$ the
same square identifies $Lu^*\omega_f$ with $\omega_{f'}$.
