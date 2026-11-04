+++
id = "prose-09-26"
kind = "hidden"
title = "Field coefficients (1)"
order = 780
+++
With coefficients in $E$ there is no tower to pass to the limit over, but none is
needed. An object of $\Dbc(T,E)$ comes from an integral complex by inverting $\ell$, and its Hom
groups are the integral Hom groups tensored with $E$ (9.21). An
adjunction over $\mathcal O_E$ is a natural bijection of Hom groups, and tensoring it
with $E$ gives an adjunction over $E$ (Proposition [proposition-sp-rational]). For $\overline{\mathbf Q}_\ell$
the Hom groups are colimits over finite extensions of $\mathbf Q_\ell$, and the adjunctions over
these fields pass to the colimit (Theorem [theorem-sp-qbar]). For each coefficient
ring we thus construct an explicit right adjoint of $Rf_!$, and we identify it with $f^!$
by the uniqueness of adjoints
(Proposition [proposition-sp-unique-adjoint]).

Every object of $\Dbc(T,E)$ is $K_0[1/\ell]$ for some $K_0\in\Dbc(T,\mathcal O_E)$, called an
integral model, and for integral models

$$
\Hom(K_0,L_0[q])\otimes_{\mathcal O_E}E
\xrightarrow{\sim}\Hom_{\Dbc(T,E)}\bigl(K_0[1/\ell],L_0[1/\ell][q]\bigr).
\tag{9.21}
$$

Both statements are Proposition [proposition-inverting-ell]: its essential
surjectivity provides the models, and (9.21) is its full
faithfulness. To see the latter directly, note that the target is $\Hom(K_0,L_0[1/\ell][q])$ by adjunction, and
$L_0[1/\ell]$ is the colimit of $L_0\xrightarrow{\ell}L_0\xrightarrow{\ell}\cdots$.
The left side is the colimit of the same system of Hom groups, so the claim
is that Hom out of $K_0$ commutes with this colimit. Both sides are
cohomological functors of $K_0$, so by the five lemma and
dévissage we may take $K_0=a_!C$ with $C$ dualizable on a stratum
(Lemma [lemma-structure-integral-constructible-complexes](3)). The stratum formula of
Lemma [lemma-sections-support-closed-subscheme](2), whose proof uses only that $C$ is dualizable,
turns Hom out of $a_!C$ into cohomology on a quasi-compact quasi-separated scheme, and
this commutes with the colimit by Corollary [corollary-continuity-cohomology]. On
models $f^*$ and $Rf_!$ are the integral functors with $\ell$ inverted, again because
$R\bar f_*$ commutes with the colimit along $\ell$.

With (9.21) the adjunction for $E$ becomes a matter of
inverting $\ell$ in the integral adjunction.
