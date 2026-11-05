+++
kind = "proof"
of = "lemma-lattices-lisse-e-sheaves--2"
order = 260004
uses = ["definition-ind-etale-pro-etale-weakly--1", "definition-ind-etale-pro-etale-weakly--2", "proposition-etale-implications--1", "lemma-stability--4", "lemma-stability--6", "lemma-stability--7", "proposition-pro-etale-coverings--2", "proposition-topos-functoriality--1", "definition-w-local-w-strictly-local--2", "definition-w-local-w-strictly-local--3", "definition-w-local-w-strictly-local--4", "proposition-w-local-components--1", "theorem-existence-contractible-covers--1", "proposition-pro-etale-affines-form-basis--2", "lemma-w-contractible-affines-projective--1", "definition-weak-contractibility--1", "theorem-classical-sheaves-essential-image--1", "proposition-sp-unique-adjoint--1"]
+++
By Remark [remark-constructible-sheaves-coefficient-rings--1](3), an $E_X$-module that is locally free of finite
rank is lisse, so clause [lemma-lattices-lisse-e-sheaves--1] applies to $L$. Let $Y\to X$ be the
separated surjective étale $X$-scheme representing the sheaf of lattices
in $L$, and let $M_Y\subset L|_Y$ be its universal lattice. Cover $Y$ by
affine open subschemes $Y_i$, $i\in I$, and let $f_i:Y_i\to X$ be the
composite. Each $f_i$ is étale, and together they are surjective because
$Y\to X$ is, so $\{f_i\}$ is an étale covering. Since $Y_i$ is étale
over $X$, it is an object of $X_{\mathrm{pro}\acute{e}t}$ and $f_i^{-1}L=L|_{Y_i}$. Put
$M_i=M_Y|_{Y_i}$. Since the lattices form a sheaf, $M_i$ is a lattice in
$L|_{Y_i}$: by Definition [definition-lattice--1] it is a lisse
$\mathcal O_{E,Y_i}$-submodule with $M_i[1/\ell]=L|_{Y_i}$.

The module $M_i$ is locally free of finite rank. Indeed, $\ell$ acts
invertibly on $L|_{Y_i}$, so multiplication by $\ell$ is injective on the
submodule $M_i$. Thus $M_i$ is a torsion free lisse
$\mathcal O_{E,Y_i}$-module, and such a module is locally free of finite rank
by Remark [remark-constructible-sheaves-coefficient-rings--1](6). Finally, $E_{Y_i}=\mathcal O_{E,Y_i}[1/\ell]$ by
clause [lemma-comparison-completed-coefficients--2], and localization is a filtered colimit, so
$M_i\otimes_{\mathcal O_{E,Y_i}}E_{Y_i}=M_i[1/\ell]$. Under this
identification the map induced by the inclusion $M_i\subset L|_{Y_i}$ is the
equality $M_i[1/\ell]=L|_{Y_i}$ in the definition of a lattice. This proves
the first assertion.

Now let the underlying space of $X$ be Noetherian, so that $X$ is
quasi-compact. Since étale morphisms are open, the images $f_i(Y_i)$ form
an open covering of $X$, and finitely many of them, say for $i\in I_0$,
already cover $X$. Put $U=\coprod_{i\in I_0}Y_i$, let $p$ be induced by the
$f_i$, and let $M$ be $M_i$ on $Y_i$. A finite disjoint union of affine
schemes is affine, so $U$ is quasi-compact and quasi-separated. The map $p$
is étale and surjective, and $M$ is locally free of finite rank with
$M\otimes_{\mathcal O_{E,U}}E_U\simeq p^{-1}L$, componentwise by the first
part. The argument nowhere uses that the rank is constant, and it applies
verbatim when $L=0$ or $X$ is empty.

*Source:* the proof of Lemma [lemma-lattices-lisse-e-sheaves].
