+++
id = "prose-05-06"
kind = "hidden"
title = "Compactness of constructible complexes (2)"
order = 438
+++
The general argument rests on the same mechanism: a bound $d_C$, valid
for all [constructible](@definition-constructible-sheaves) targets at once, beyond which $\Ext^q(C,-)$
vanishes. Until the end of Section [sec-Compactness-of-constructible-complexes], $\Lambda$ is $E$
or $\overline{\mathbf Q}_\ell$, and we show that bounded [constructible complexes](@definition-constructible-sheaves) are compact
in [$\Loc(\Dbc(X,\Lambda))$](@definition-localizing-subcategory). Since $\href{@definition-constructible-sheaves}{D^b_{\mathrm{ctf}}(X,\Lambda)}=\href{@definition-constructible-sheaves}{\Dbc(X,\Lambda)}$,
these are the proposed compact generators. The advantage of working with [$\Dbc$](@definition-constructible-sheaves) is that we can use truncations
and the [constructible heart](@definition-constructible-sheaves), which is abelian by
Lemma [lemma-constructible-sheaves]. As for notation, $\Hom$ and
$\Ext$ without decoration are taken in $D(\href{@definition-small-pro-etale-site}{X_{\mathrm{pro}\acute{e}t}},\Lambda)$, also when both arguments are
[constructible sheaves](@definition-constructible-sheaves), and a subscript indicates the coefficient ring where
it changes, as in the [lattice](@definition-lattice) arguments over $\mathcal O_E$.

By dévissage it suffices to show, for a [constructible sheaf](@definition-constructible-sheaves) $C$ and a
family $(K_\lambda)$ of objects of [$\Loc(\Dbc(X,\Lambda))$](@definition-localizing-subcategory), that
$\bigoplus_\lambda\Hom(C,K_\lambda)\to\Hom(C,\bigoplus_\lambda K_\lambda)$
is bijective. Besides the uniform bound
$\Ext^q(C,N)=0$ for $q>d_C$ and all [constructible](@definition-constructible-sheaves) $N$
(Lemma [lemma-uniform-ext-bound] below), we use that $\Ext^q(C,-)$
commutes with filtered colimits of complexes that vanish below a fixed
degree, in particular of sheaves
(Lemma [lemma-continuity-ext-out-constructible-complex], proved in
Section [sec-Continuity-of-Ext]).
