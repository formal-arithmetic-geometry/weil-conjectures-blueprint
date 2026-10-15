+++
kind = "proof"
of = "det-sp-normalized-equivalence"
+++
*Adjunction.* For $M\in D(T_{\mathrm{proét}},\mathcal O_E)$ and a tower
$C_\bullet$, a map $\operatorname{red}_TM\to C_\bullet$ is a compatible family of
maps $M/\ell^n\to C_n$ over $\mathcal O_E/\ell^n$, equivalently (by
extension–restriction of scalars) a compatible family $M\to C_n$ of
$\mathcal O_E$-linear maps, i.e. a map from the constant tower $M$ to $C_\bullet$;
and $R\varprojlim$ is right adjoint to the constant-tower functor. At the
derived level this is Bhatt–Scholze, Lemma 3.5.7.

*Unit.* The unit $M\to R\varprojlim_n M/\ell^n$ is the derived completion map,
an isomorphism exactly when $M$ is derived $\ell$-complete; objects of
$\Dbc(T,\mathcal O_E)$ are derived complete.

*Counit.* For a normalized tower $C_\bullet$, the counit
$\operatorname{red}_T(R\varprojlim C_\bullet)\to C_\bullet$ is at level $m$ the map
$(R\varprojlim_nC_n)/\ell^m\to C_m$, an isomorphism by the reconstruction lemma
(see also [lem-coef-normalized-dvr-effectivity]); levelwise isomorphisms are
isomorphisms of towers.

*Restriction.* $\operatorname{red}_T$ sends $\Dbc(T,\mathcal O_E)$ into normalized
constructible towers by [det-sp-reduction-tower-normalized], and
$R\varprojlim$ sends normalized constructible towers into $\Dbc(T,\mathcal O_E)$
by the reconstruction lemma. With unit and counit isomorphisms on these
subcategories, the restricted functors are mutually inverse equivalences.
