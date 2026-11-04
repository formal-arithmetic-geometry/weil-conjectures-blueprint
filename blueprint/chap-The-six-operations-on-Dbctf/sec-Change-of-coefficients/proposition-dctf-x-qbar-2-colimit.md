+++
id = "proposition-dctf-x-qbar-2-colimit"
kind = "proposition"
title = "$\\Dctf(X,\\Qbar)$ as a $2$-colimit"
order = 642
lean = ["AlgebraicGeometry.ProEtale.constructibleCocone", "AlgebraicGeometry.ProEtale.constructibleCocone_homSurj", "AlgebraicGeometry.ProEtale.constructibleCocone_homInj", "AlgebraicGeometry.ProEtale.constructibleCocone_essSurjObj", "AlgebraicGeometry.ProEtale.constructibleCocone_isFilteredTwoColimit"]
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability", "definition-small-pro-etale-site", "proposition-topos-functoriality", "definition-constructible-sheaves"]
+++
Extension of scalars identifies

$$
D^b_{\mathrm{ctf}}(X,\overline{\mathbf Q}_\ell)\simeq\mathop{\text{2-colim}}_{E\subset\overline{\mathbf Q}_\ell}D^b_{\mathrm{ctf}}(X,E)
$$

as ordinary categories. In other words, every object of $D^b_{\mathrm{ctf}}(X,\overline{\mathbf Q}_\ell)$ is isomorphic to
$K_{\overline{\mathbf Q}_\ell}$ for some finite $E$ and some $K\in D^b_{\mathrm{ctf}}(X,E)$, and for
$K,L\in D^b_{\mathrm{ctf}}(X,E)$ extension of scalars induces a bijection

$$
\varinjlim_{F\supset E}\Hom_{D^b_{\mathrm{ctf}}(X,F)}(K_F,L_F)
\xrightarrow{\sim}\Hom_{D^b_{\mathrm{ctf}}(X,\overline{\mathbf Q}_\ell)}(K_{\overline{\mathbf Q}_\ell},L_{\overline{\mathbf Q}_\ell}),
$$

the colimit running over finite extensions $F$ of $E$ in $\overline{\mathbf Q}_\ell$.
