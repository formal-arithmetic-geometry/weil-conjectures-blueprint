+++
id = "sk-lem-integral-models"
kind = "lemma"
title = "Integral models"
order = 2310
uses = ["sk-def-sfb-constructible", "sk-prop-integral-criterion", "sk-lem-coefficient-heart"]
tags = ["sketch"]
+++
To deduce statements over $E$ and $\Qlb$ from statements over $\cO_E$, we need integral
objects that generate $\Dbc(X,E)$ and $\Dbc(X,\Qlb)$ ([sk-def-sfb-constructible]), and we want
to know that our integral constructible complexes are those of the Stacks Project, so that
results proved there apply. The next lemma provides both. Recall from
[sk-prop-integral-criterion] that an object lies in $\Dbc(X,\cO_E)=\Dctf(X,\cO_E)$ precisely
when it is derived complete and its reduction modulo $\pi_E$ is a bounded constructible complex
pulled back from $X_{\mathrm{ét}}$. The Stacks Project works instead with the category
$\Dc(X,\cO_E)$ of [Stacks, Tag 09C1](https://stacks.math.columbia.edu/tag/09C1), built from modules over the constant sheaf $\cO_E$ rather than
over $\cO_{E,X}$.

1. Restriction of scalars along the map from the constant sheaf $\cO_E$ to $\cO_{E,X}$ is an
   equivalence between the derived complete objects of $D(X_{\mathrm{proét}},\cO_E)$ and the
   derived complete complexes of modules over the constant sheaf $\cO_E$.
2. An object $K$ of $D(X_{\mathrm{proét}},\cO_E)$ lies in $\Dbc(X,\cO_E)$ if and only if its
   restriction of scalars lies in $\Dc(X,\cO_E)$.
3. $\Dbc(-,\cO_E)$ is preserved by
   $f^*\colon D(Y_{\mathrm{proét}},\cO_E)\to D(X_{\mathrm{proét}},\cO_E)$ for every morphism
   $f\colon X\to Y$, by $\otimes^{\mathbf L}_{\cO_{E,X}}$ on $D(X_{\mathrm{proét}},\cO_E)$, and by
   $a_!\colon D(S_{\mathrm{proét}},\cO_E)\to D(X_{\mathrm{proét}},\cO_E)$ ([sk-lem-coefficient-heart])
   for every locally closed immersion $a\colon S\hookrightarrow X$.
4. Every object of $\Dbc(X,E)$ is obtained by finitely many cones and shifts from objects
   $(a_!L_0)[1/\ell]$, where $a\colon S\hookrightarrow X$ is a locally closed immersion and $L_0$
   is a lisse finite free $\cO_{E,S}$-module. Every object of $\Dbc(X,\Qlb)$ is obtained in the
   same way from the objects $\QbarX\otimes_{\cO_{E,X}}a_!L_0$, for some finite $E/\mathbf Q_\ell$.
   The reductions of $a_!L_0$ modulo $\pi_E^n$ are bounded constructible complexes on
   $X_{\mathrm{proét}}$ with coefficients in $\cO_E/\pi_E^n$.
