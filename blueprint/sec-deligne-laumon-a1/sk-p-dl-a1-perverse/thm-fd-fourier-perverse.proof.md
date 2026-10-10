+++
kind  = "proof"
of    = "thm-fd-fourier-perverse"
+++
Let $K\in{}^pD^{\le0}(V)$ (respectively $K\in{}^pD^{\ge0}(V)$),
and put $X:=V\times_{k_0}V^\vee$. The projection $p_1$ is smooth
of constant relative dimension one, so the smooth-pullback exactness
[lem-per-smooth-pullback-t-exact] of the perverse-curve chapter gives

$$
Lp_1^*K\in{}^pD^{\le1}(X),\qquad
Lp_1^*K\in{}^pD^{\ge1}(X)
$$

for the corresponding side: with the shift convention
${}^pD^{\le n}={}^pD^{\le0}[-n]$, the direct statement is
$Lp_1^*[1]K\in{}^pD^{\le0}(X)$ and
$Lp_1^*[1]K\in{}^pD^{\ge0}(X)$, and the displayed inclusions are
the same statements after the $[-1]$-shift (the shift
$[-1]$ lowers both indices by one:
${}^pD^{\le0}[-1]={}^pD^{\le1}$,
${}^pD^{\ge0}[-1]={}^pD^{\ge1}$).

The kernel $\mathcal K_\psi$ is lisse of rank one [prop-kernel-lisse] (the pullback
$b^*\mathcal L_{\psi(b(x,\xi))}$ of the rank-one lisse
Artin–Schreier sheaf of [lem-fd-as-lisse]), so the lisse-tensor
permanence [lem-per-lisse-tensor-permanence] of the perverse-curve chapter
gives the same sidewise inclusions for
$Lp_1^*K\otimes^L\mathcal K_\psi$:

$$
Lp_1^*K\otimes^L\mathcal K_\psi\in{}^pD^{\le1}(X),
\qquad
Lp_1^*K\otimes^L\mathcal K_\psi\in{}^pD^{\ge1}(X).
$$

The projection $p_2$ is affine with fibers of dimension at most
one, so the affine pushforward amplitude
[lem-per-artin-gabber-affine-curve] of the perverse-curve chapter (relative
dimension $d=1$) gives $p_{2,!}\bigl({}^pD^{\le0}(X)\bigr) \subset{}^pD^{\le1}(V^\vee)$ and
$p_{2,!}\bigl({}^pD^{\ge0}(X)\bigr)\subset {}^pD^{\ge-1}(V^\vee)$; applied to the
$[-1]$-shifted objects of the two families above (the functor
$p_{2,!}$ commutes with shifts), this yields

$$
p_{2,!}\bigl(Lp_1^*K\otimes^L\mathcal K_\psi\bigr)
\in{}^pD^{\le2}(V^\vee),\qquad
\bigl(\,\cdot\,\bigr)\in{}^pD^{\ge0}(V^\vee)
$$

sidewise (the $\le$-bound increases the index by one for the
$[-1]$-shifted input, and the $\ge$-bound respectively). The
normalization $[1]$ of [def-fd-transform] lowers both indices
by one, since
${}^pD^{\le n}[1]={}^pD^{\le n-1}$ and
${}^pD^{\ge n}[1]={}^pD^{\ge n-1}$ by the shift convention of
[def-per-perverse-subcategories], so

$$
\operatorname{FT}_\psi(K)\in{}^pD^{\le1}(V^\vee),\qquad
\operatorname{FT}_\psi(K)\in{}^pD^{\ge-1}(V^\vee)
$$

for the two sides respectively, which is the asserted amplitude.
