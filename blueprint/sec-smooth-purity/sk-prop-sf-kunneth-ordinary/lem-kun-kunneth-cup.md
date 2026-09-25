+++
id = "lem-kun-kunneth-cup"
kind = "lemma"
title = "The Kunneth map via the relative cup product"
order = 1787
uses = ["def-kun-kunneth-map", "def-kun-rel-cup", "def-weil-pbc-cartesian-square", "def-weil-pbc-inverse-image", "lem-kun-inverse-image-monoidal", "lem-weil-derived-direct-image-composition"]
+++
In the situation of [def-kun-kunneth-map], the Kunneth map
$\kappa_{E,K}$ is equal to the composite

$$
Rf_*E\kunotimes{\Lambda}Rg_*K
\xrightarrow{\ u\otimes v\ }
Rc_*p^{-1}E\kunotimes{\Lambda}Rc_*q^{-1}K
\xrightarrow{\ \mathrm{cup}_{c}\ }
Rc_*\bigl(p^{-1}E\kunotimes{\Lambda}q^{-1}K\bigr),
$$

where $u:Rf_*E\to Rc_*p^{-1}E$ and
$v:Rg_*K\to Rc_*q^{-1}K$ are the canonical maps induced by the units
of [def-weil-pbc-inverse-image] via the identifications
$Rc_*=Rf_*\circ Rp_*$ (respectively $Rc_*=Rg_*\circ Rq_*$) of
[lem-weil-derived-direct-image-composition] (item (5)), and
$\mathrm{cup}_{c}$ is the relative cup product of
[def-kun-rel-cup] for $c$.

## Proof

It suffices to compare the adjoints of the two maps under
$c^{-1}\dashv Rc_*$. By [def-kun-rel-cup], the adjoint of
$\mathrm{cup}_{c}$ is

$$
(\varepsilon_c\otimes\varepsilon_c)\circ\mathrm{mon},
$$

where $\mathrm{mon}$ is the monoidal comparison of
[lem-kun-inverse-image-monoidal] for the inverse image;
applying $c^{-1}$ to $u\otimes v$ and composing gives

$$
c^{-1}\bigl(\mathrm{cup}_c\circ(u\otimes v)\bigr)
=
(\varepsilon_c\otimes\varepsilon_c)\circ\mathrm{mon}\circ
(c^{-1}u\otimes c^{-1}v).
$$

Now $c=f\circ p$, so under the canonical identification
$c^{-1}Rf_*E\cong p^{-1}f^{-1}Rf_*E$ of
[def-weil-pbc-cartesian-square], the map $c^{-1}u$ is the
composite

$$
p^{-1}f^{-1}Rf_*E\longrightarrow p^{-1}E
$$

induced by the counit $\varepsilon_f$ through the unit of
$p^{-1}\dashv Rp_*$ (and similarly for $v$ with $\varepsilon_g$).
The counit $\varepsilon_c$ for $c=f\circ p$ factors through the
composite counits of $p$ and $f$, so the displayed composite is
exactly

$$
(\varepsilon_f\otimes\varepsilon_g)\circ\mathrm{mon},
$$

which is the adjoint of $\kappa_{E,K}$ by
[def-kun-kunneth-map]. Since the adjunction bijection is
injective, the two maps agree.
