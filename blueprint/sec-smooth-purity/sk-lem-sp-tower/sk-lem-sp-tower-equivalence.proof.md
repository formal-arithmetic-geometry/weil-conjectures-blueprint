+++
kind = "proof"
of = "det-sp-normalized-equivalence"
uses = ["sk-prop-pe-replete", "sk-prop-integral-criterion", "det-sp-reduction-tower-normalized", "sk-prop-sp-integral-towers"]
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
$\Dbc(T,\mathcal O_E)$ are derived complete by the criterion
(1)$\Rightarrow$(2) of [sk-prop-integral-criterion].

*Counit.* For a normalized tower $C_\bullet$, the counit
$\operatorname{red}_T(R\varprojlim C_\bullet)\to C_\bullet$ is at level $m$ the map
$(R\varprojlim_nC_n)/\ell^m\to C_m$, an isomorphism by
[lem-coef-normalized-dvr-effectivity] (with $\pi_E$ replaced by $\ell$);
levelwise isomorphisms are isomorphisms of towers.

*Restriction.* $\operatorname{red}_T$ sends $\Dbc(T,\mathcal O_E)$ into normalized
constructible towers by [det-sp-reduction-tower-normalized] (part (1) of
[sk-prop-sp-integral-towers]). Conversely, let
$C_\bullet$ be a normalized constructible tower and $C=R\varprojlim_nC_n$. By the
counit isomorphism, $C$ is derived complete and $C/\ell\simeq C_1$ lies in
$\Dctf(T_{\mathrm{proét}},\mathcal O_E/\ell)$; since the $C_n$ have cohomology in a
common bounded interval and $T_{\mathrm{proét}}$ is replete
([sk-prop-pe-replete]), $C$ is bounded. So $C\in\Dbc(T,\mathcal O_E)$ by part (2) of
[sk-prop-sp-integral-towers]. With unit and counit isomorphisms on these
subcategories, the restricted functors are mutually inverse equivalences.
