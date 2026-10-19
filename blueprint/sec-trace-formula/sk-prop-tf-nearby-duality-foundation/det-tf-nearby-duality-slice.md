+++
id = "det-tf-nearby-duality-slice"
kind = "lemma"
title = "Nearby duality in a generic slice"
uses = ["det-tf-nearby-duality-proper", "det-tf-invariants-duality", "det-pd-generic-dualizing-twist", "det-pd-generic-closed-hom"]
+++
In the setting of [det-tf-nearby-duality-proper], let $b:X\to\mathbf A^1_S$ be a
coordinate map, let $s'$ be a geometric generic point of the special fibre
$\mathbf A^1_k$ and $S'=(\mathbf A^1_S)_{(s')}$ the strict localization, a strictly
henselian trait with the same uniformizer as $S$, and let $P$ be the pro-$p$ kernel of
the map of inertia groups $I'\to I$. Put $X'=X\times_{\mathbf A^1_S}S'$,
$M'=M|_{X'_{\bar\eta'}}$, and write $g_s,g_\eta$ for the two geometric
generic-coordinate pullbacks, so that the generic-slicing identification is
$g_s^*S_XM\simeq(S_{X'}M')^P$. Then $P$ acts trivially on $A(1)[2]$,

$$
 g_\eta^*\mathbb D_{X_{\bar\eta}}M\simeq \mathbb D_{X'_{\bar\eta'}}M'\otimes A(1)[2],
 \qquad
 g_s^*\mathbb D_{X_s}E\simeq \mathbb D_{X'_{s'}}(g_s^*E)\otimes A(1)[2]
 \tag{1}
$$

for $E\in D^b_{\mathrm{ctf}}(X_s,A)$, and under these identifications and
[det-tf-invariants-duality]

$$
 g_s^*\delta_{X,M}=(\delta_{X',M'})^P\otimes A(1)[2].
 \tag{2}
$$
