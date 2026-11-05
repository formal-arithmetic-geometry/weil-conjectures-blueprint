+++
id = "lemma-artin-schreier-character-sheaf--1"
kind = "lemma"
title = "The lisse rank-one Weil sheaf"
order = 1217002
aliases = ["bp-r375-1"]
lean = ["AlgebraicGeometry.artinSchreier", "AlgebraicGeometry.isLisse_artinSchreier", "AlgebraicGeometry.WeilSheaf.finrank_stalk_artinSchreier", "AlgebraicGeometry.nonempty_artinSchreier_zero_iso_adicConstant"]
uses = ["definition-small-pro-etale-site", "definition-lisse-sheaves", "definition-weil-structure", "proposition-topos-functoriality"]
+++
Let $k_0=\Fq$, let $\ell\ne\operatorname{char}(k_0)$ be prime, and let
$\psi:k_0\to\Qbarl^\times$ be any additive character. The image of

$$
e_\psi=\frac1q\sum_{c\in k_0}\psi(-c)\tau_c^*
$$

on the direct image of the constant Weil sheaf under $u^q-u=x$
defines $\mathcal L_\psi$. For every $a\in k_0$, its pullback
$\mathcal L_{\psi(ax)}$ along $x\mapsto ax$ is a lisse Weil sheaf,
and its stalk at every closed point has dimension one over $\Qbarl$.
Moreover,

$$
\mathcal L_{\psi(0x)}\simeq\Qbarl_{\mathbf A^1_{k_0}}.
$$

This last assertion gives an isomorphism for the pullback along the
zero map. The Lean statements do not package a chosen trivialization
at zero together with normalized multiplication and duality isomorphisms.
